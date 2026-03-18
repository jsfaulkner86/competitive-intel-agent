# 🔍 Competitive Intelligence Agent — Women's Health Landscape Monitor

An agentic AI system built for **The Faulkner Group** advisory clients — women's health tech founders who need continuous visibility into competitor moves, market consolidation, and landscape shifts.

This agent runs bi-weekly and delivers a structured competitive landscape briefing so founders always know where they stand and what differentiators to sharpen.

---

## 🎯 What This Agent Tracks

| Signal Type | What It Catches |
|---|---|
| Funding rounds | Competitor raises, new investors entering the space |
| Product launches | New features, FDA clearances, market expansions |
| Partnerships | Health system deals, payer contracts, strategic alliances |
| Executive moves | C-suite hires, departures, board additions |
| M&A activity | Acquisitions, mergers, strategic exits |
| Conference presence | Speaking slots, awards, industry recognition |
| Pricing signals | Published pricing changes, new pricing models |

---

## 🏗 Architecture

```
competitive-intel-agent/
├── agents/
│   ├── funding_tracker_agent.py   # Tracks competitor fundraising
│   ├── product_tracker_agent.py   # Monitors product + feature launches
│   ├── signal_tracker_agent.py    # Exec moves, partnerships, M&A
│   └── landscape_agent.py         # Synthesizes full landscape briefing
├── tools/
│   ├── perplexity_tool.py         # Web research for all signal types
│   ├── crunchbase_tool.py         # Funding round data
│   └── web_scraper_tool.py        # Competitor website + press monitoring
├── pipelines/
│   └── biweekly_intel_run.py      # Full orchestration pipeline
├── db/
│   └── supabase_client.py
├── delivery/
│   ├── email_briefing.py
│   └── notion_push.py
├── profiles/
│   └── founder_profiles.py        # Competitor lists per client
├── scheduler/
│   └── cron_runner.py
├── config/
│   └── settings.py
├── .github/
│   └── workflows/
│       ├── competitive-pipeline.yml
│       └── manual-test-run.yml
├── .env.example
├── requirements.txt
└── README.md
```

---

## 🚀 Setup

```bash
git clone https://github.com/jsfaulkner86/competitive-intel-agent
cd competitive-intel-agent
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python pipelines/biweekly_intel_run.py
```

---

*Built by The Faulkner Group — Agentic AI for Women's Health Founders*
