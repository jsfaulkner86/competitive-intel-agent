import httpx
from config.settings import settings

CRUNCHBASE_BASE = "https://api.crunchbase.com/api/v4"

def get_recent_funding_rounds(company_name: str) -> list[dict]:
    """Fetch recent funding rounds for a named company via Crunchbase."""
    params = {"user_key": settings.crunchbase_api_key}
    # Search for org first
    search_resp = httpx.post(
        f"{CRUNCHBASE_BASE}/searches/organizations",
        json={"field_ids": ["identifier", "short_description"], "query": [{"type": "predicate", "field_id": "facet_ids", "operator_id": "includes", "values": ["company"]}, {"type": "predicate", "field_id": "name", "operator_id": "contains", "values": [company_name]}], "limit": 1},
        params=params,
        timeout=15,
    )
    results = search_resp.json().get("entities", [])
    if not results:
        return []
    org_id = results[0]["identifier"]["permalink"]
    # Fetch funding rounds
    rounds_resp = httpx.get(
        f"{CRUNCHBASE_BASE}/entities/organizations/{org_id}/funding_rounds",
        params=params,
        timeout=15,
    )
    rounds_resp.raise_for_status()
    return rounds_resp.json().get("entities", [])
