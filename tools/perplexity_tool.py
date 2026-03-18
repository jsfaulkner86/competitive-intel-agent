import httpx
from config.settings import settings

PERPLEXITY_URL = "https://api.perplexity.ai/chat/completions"

def research_competitor(query: str) -> str:
    headers = {
        "Authorization": f"Bearer {settings.perplexity_api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "sonar",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a competitive intelligence analyst for women's health tech. "
                    "Research and summarize: funding rounds, product launches, partnership announcements, "
                    "executive hires/departures, M&A activity, and pricing changes. "
                    "Always include dates, source URLs, and signal type classification. "
                    "Be factual. Do not speculate. If a signal is unconfirmed, mark it as 'unconfirmed'."
                ),
            },
            {"role": "user", "content": query},
        ],
    }
    response = httpx.post(PERPLEXITY_URL, json=payload, headers=headers, timeout=30)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
