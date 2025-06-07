import time

from server.utils.logger import logger
from server.utils.singleton import Singleton


class CronJobService(metaclass=Singleton):
    def __init__(self):
        logger.info("CronJobService initialized")

    @staticmethod
    def do_job():
        logger.info(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))
