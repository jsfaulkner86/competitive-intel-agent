from crewai import Crew, Task
from agents.funding_tracker_agent import funding_tracker_agent
from agents.product_tracker_agent import product_tracker_agent
from agents.signal_tracker_agent import signal_tracker_agent
from agents.landscape_agent import landscape_agent, LANDSCAPE_PROMPT
from db.supabase_client import save_briefing
from delivery.notion_push import push_briefing_to_notion
from delivery.email_briefing import send_competitive_briefing
from profiles.founder_profiles import FOUNDER_PROFILES
from datetime import datetime
import json

def run_pipeline():
    period = datetime.now().strftime("%B %d, %Y")
    print(f"[CompetitiveIntelAgent] Starting bi-weekly run — {period}")

    for profile in FOUNDER_PROFILES:
        competitors = profile.get("competitors", [])
        adjacent = profile.get("adjacent_companies", [])
        keywords = profile.get("monitor_keywords", [])
        all_companies = competitors + adjacent

        competitor_query = (
            f"Research recent news (past 14 days) for these women's health companies: "
            f"{', '.join(all_companies)}. "
            f"Also search for: {', '.join(keywords)}. "
            f"Cover: funding rounds, product launches, partnerships, executive hires, M&A."
        ) if all_companies else (
            f"Research top women's health tech companies in {profile['indication']} — "
            f"funding, launches, partnerships, executive moves in the past 14 days."
        )

        funding_task = Task(
            description=f"Track funding activity: {competitor_query}",
            agent=funding_tracker_agent,
            expected_output="List of funding signals with company, amount, investors, date, and source URL.",
        )
        product_task = Task(
            description=f"Track product and feature launches: {competitor_query}",
            agent=product_tracker_agent,
            expected_output="List of product signals with company, launch type, description, date, and URL.",
        )
        signal_task = Task(
            description=f"Track executive moves, partnerships, and M&A: {competitor_query}",
            agent=signal_tracker_agent,
            expected_output="List of market signals with company, signal type, description, date, and URL.",
        )
        landscape_task = Task(
            description=(
                f"Synthesize all signals for {profile['founder_name']} at {profile['company']}.\n"
                f"Their key differentiators: {profile.get('key_differentiators', [])}.\n"
                f"Use this structure:\n{LANDSCAPE_PROMPT}"
            ),
            agent=landscape_agent,
            expected_output="A structured competitive landscape briefing in HTML format.",
        )

        crew = Crew(
            agents=[funding_tracker_agent, product_tracker_agent, signal_tracker_agent, landscape_agent],
            tasks=[funding_task, product_task, signal_task, landscape_task],
            verbose=True,
        )
        briefing_html = crew.kickoff()
        briefing_str = briefing_html if isinstance(briefing_html, str) else str(briefing_html)

        save_briefing({"client_id": profile["client_id"], "period": period, "briefing": briefing_str})
        notion_url = push_briefing_to_notion(
            client_id=profile["client_id"],
            founder_name=profile["founder_name"],
            briefing_text=briefing_str,
            period=period,
        )
        send_competitive_briefing(
            recipient_email=profile["email"],
            founder_name=profile["founder_name"],
            briefing_html=briefing_str,
            period=period,
        )
        print(f"[CompetitiveIntelAgent] Done for {profile['founder_name']} — Notion: {notion_url}")

    print("[CompetitiveIntelAgent] Bi-weekly run complete.")

if __name__ == "__main__":
    run_pipeline()
