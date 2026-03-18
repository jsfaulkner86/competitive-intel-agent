import httpx
from bs4 import BeautifulSoup

def scrape_press_page(url: str) -> str:
    """Scrape a competitor's press/news page for recent announcements."""
    headers = {"User-Agent": "Mozilla/5.0 (compatible; CompetitiveIntelAgent/1.0)"}
    response = httpx.get(url, headers=headers, timeout=15, follow_redirects=True)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()
    return " ".join(soup.get_text(separator=" ").split())[:5000]
