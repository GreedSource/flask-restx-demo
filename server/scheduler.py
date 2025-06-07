import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from .services.cronjob_service import CronJobService
from .utils.logger import logger


def init_scheduler():
    """Initialize the scheduler and add jobs, ensuring it's only initialized once."""
    global scheduler_instance

    logger.debug(
        f"Initializing scheduler. Current scheduler_instance: {scheduler_instance}"
    )

    if scheduler_instance is not None:
        # If already initialized, return the existing instance
        logger.info("Scheduler already initialized.")
        return scheduler_instance

    # Create a new scheduler instance
    scheduler = BackgroundScheduler()

    # Check if the job exists, and remove it if needed
    if scheduler.get_job("log_time_task"):
        logger.debug("Removing existing log_time_task job.")
        scheduler.remove_job("log_time_task")

    # Add a job to run every 10 seconds
    logger.debug("Adding log_time_task job.")
    scheduler.add_job(
        id="log_time_task", func=CronJobService.do_job, trigger="interval", seconds=10
    )

    # Start the scheduler
    logger.debug("Starting scheduler.")
    scheduler.start()

    # Register the scheduler to shut down gracefully on app exit
    atexit.register(lambda: scheduler.shutdown())

    # Store the scheduler instance in the global variable
    scheduler_instance = scheduler

    logger.debug(f"Scheduler initialized successfully: {scheduler_instance}")
    return scheduler
