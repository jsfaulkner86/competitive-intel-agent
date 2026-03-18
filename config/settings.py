from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    openai_api_key: str
    perplexity_api_key: str
    crunchbase_api_key: str
    supabase_url: str
    supabase_key: str
    resend_api_key: str
    intel_from_email: str = "intel@thefaulknergroupadvisors.com"
    notion_api_key: str
    notion_database_id: str
    run_cadence_days: int = 14
    focus_area: str = "womens_health"

    class Config:
        env_file = ".env"

settings = Settings()
