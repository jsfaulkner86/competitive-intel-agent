from crewai import Agent

LANDSCAPE_STRUCTURE = """
Synthesize all competitive signals into a structured bi-weekly landscape briefing:

## 🔥 Hot Signals (high-impact moves requiring founder awareness this week)
## 💰 Funding Activity (rounds closed, amounts, lead investors)
## 🚀 Product & Feature Launches (new releases, FDA clearances, market expansions)
## 🤝 Partnership & M&A (health system deals, payer contracts, acquisitions)
## 👤 Executive Moves (key hires, departures, board changes)
## 🏆 Your Competitive Position (how these signals affect the client's differentiation)

For 'Your Competitive Position': reference the founder's key differentiators and assess 
whether competitor moves strengthen or threaten each one. Be direct and strategic.
"""

landscape_agent = Agent(
    role="Competitive Landscape Strategist",
    goal=(
        "Synthesize all competitive intelligence signals into a strategic briefing "
        "that tells founders not just WHAT happened, but WHAT IT MEANS for their "
        "positioning, fundraising narrative, and product roadmap."
    ),
    backstory=(
        "You are a competitive strategy advisor to women's health tech founders. "
        "You don't just report news — you interpret it. You help founders understand "
        "how market moves affect their story and what they should do about it."
    ),
    tools=[],
    verbose=True,
    allow_delegation=False,
)

LANDSCAPE_PROMPT = LANDSCAPE_STRUCTURE
