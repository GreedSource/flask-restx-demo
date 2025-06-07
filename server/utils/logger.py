import logging

from server.utils.singleton import Singleton


class ANSIColorFormatter(logging.Formatter, metaclass=Singleton):
    COLORS = {
        logging.DEBUG: "\033[96m",  # Cyan for DEBUG
        logging.INFO: "\033[92m",  # Green for INFO
        logging.WARNING: "\033[93m",  # Yellow for WARNING
        logging.ERROR: "\033[31m",  # Brighter Red for ERROR
        logging.CRITICAL: "\033[95m",  # Magenta for CRITICAL
    }
    LEVELNAME_COLOR = (
        "\033[38;5;214m"  # Orange color for levelname (using ANSI 256 colors)
    )
    RESET = "\033[0m"  # Reset color

    def format(self, record):
        # Colorize the levelname with the orange color and wrap it in brackets
        levelname_colored = f"{self.LEVELNAME_COLOR}[{record.levelname}]{self.RESET}"

        # Format the log message (without levelname color)
        log_message = super().format(record)

        # Replace %(levelname)s with the colorized levelname inside brackets
        log_message = log_message.replace(record.levelname, levelname_colored, 1)

        # Wrap the **entire message** (timestamp, levelname, and message content) with the log level color
        colored_message = (
            self.COLORS.get(record.levelno, self.RESET) + log_message + self.RESET
        )

        return colored_message


# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.propagate = False


# Create a console handler and set the formatter to the custom formatter
console_handler = logging.StreamHandler()
console_handler.setFormatter(
    ANSIColorFormatter(
        "%(asctime)s %(levelname)s %(filename)s:%(lineno)d in %(funcName)s() - %(message)s"
    )
)

# Add the handler to the logger
logger.addHandler(console_handler)
