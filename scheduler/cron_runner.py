from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
from pipelines.biweekly_intel_run import run_pipeline
from config.settings import settings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("CompetitiveIntelScheduler")

scheduler = BlockingScheduler()
scheduler.add_job(
    func=run_pipeline,
    trigger=IntervalTrigger(days=settings.run_cadence_days),
    id="biweekly_competitive_pipeline",
    name="Bi-Weekly Competitive Intelligence Pipeline",
    replace_existing=True,
)

if __name__ == "__main__":
    logger.info(f"Competitive Intel Scheduler starting — every {settings.run_cadence_days} days.")
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        logger.info("Scheduler stopped.")
