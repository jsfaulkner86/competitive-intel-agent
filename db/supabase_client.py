from supabase import create_client, Client
from config.settings import settings

supabase: Client = create_client(settings.supabase_url, settings.supabase_key)

def upsert_signal(signal: dict) -> dict:
    result = (
        supabase.table("competitive_signals")
        .upsert(signal, on_conflict="signal_id")
        .execute()
    )
    return result.data

def get_existing_signal_ids() -> list[str]:
    result = supabase.table("competitive_signals").select("signal_id").execute()
    return [row["signal_id"] for row in result.data]

def save_briefing(briefing: dict) -> dict:
    result = supabase.table("competitive_briefings").insert(briefing).execute()
    return result.data
