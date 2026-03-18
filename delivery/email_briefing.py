import resend
from config.settings import settings

resend.api_key = settings.resend_api_key

def send_competitive_briefing(recipient_email: str, founder_name: str, briefing_html: str, period: str):
    html_body = f"""
    <html><body style='font-family:sans-serif;max-width:700px;margin:auto'>
      <h2 style='color:#1a237e'>🔍 Competitive Intelligence Briefing</h2>
      <p style='color:#555'>{period} — prepared for <strong>{founder_name}</strong> by The Faulkner Group</p>
      <hr/>
      {briefing_html}
      <hr/>
      <p style='font-size:12px;color:#999'>Powered by Competitive Intel Agent — The Faulkner Group Advisors</p>
    </body></html>
    """
    resend.Emails.send({
        "from": settings.intel_from_email,
        "to": recipient_email,
        "subject": f"Your Competitive Intelligence Briefing — {period}",
        "html": html_body,
    })
    print(f"Competitive briefing sent to {recipient_email}")
