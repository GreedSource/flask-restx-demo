import time
from functools import wraps

from server.utils.logger import logger


def execution_time(label="Execution"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            duration = time.time() - start
            logger.debug(f"{label} completed in {duration:,.2f} seconds")
            return result

        return wrapper

    return decorator
