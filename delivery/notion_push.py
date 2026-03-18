from notion_client import Client
from config.settings import settings

notion = Client(auth=settings.notion_api_key)

def push_briefing_to_notion(client_id: str, founder_name: str, briefing_text: str, period: str) -> str:
    props = {
        "Title": {"title": [{"text": {"content": f"Competitive Briefing — {founder_name} — {period}"}}]},
        "Client": {"rich_text": [{"text": {"content": client_id}}]},
        "Period": {"rich_text": [{"text": {"content": period}}]},
        "Status": {"select": {"name": "New"}},
    }
    page = notion.pages.create(
        parent={"database_id": settings.notion_database_id},
        properties=props,
        children=[
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {"rich_text": [{"type": "text", "text": {"content": briefing_text}}]},
            }
        ],
    )
    return page["url"]
