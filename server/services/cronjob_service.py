import time

from server.utils.logger import logger


class CronJobService:

    @staticmethod
    def do_job():
        logger.error(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))
