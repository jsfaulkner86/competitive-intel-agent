# Each client profile includes their direct competitors and adjacent players to monitor.
# The agent tracks all signals for every company in the competitors list.

FOUNDER_PROFILES = [
    {
        "client_id": "client_001",
        "company": "Example Women's Health Co.",
        "founder_name": "Founder Name",
        "email": "founder@example.com",
        "indication": "maternal health",
        "product_category": "digital therapeutic",
        "stage": "Seed",
        "key_differentiators": [
            "AI-powered personalization",
            "clinical evidence from RCT",
            "payer-contracted reimbursement",
        ],
        "competitors": [
            # Add direct competitors by company name
            # e.g. "Ovia Health", "Wildflower Health", "Babyscripts"
        ],
        "adjacent_companies": [
            # Companies not direct competitors but in adjacent women's health spaces
        ],
        "monitor_keywords": [
            "maternal health digital",
            "pregnancy remote monitoring",
            "postpartum digital health",
        ],
    },
]
