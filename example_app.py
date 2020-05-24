import logging
import socket
import sys

from colargulog import ColorizedArgsFormatter
from colargulog import BraceFormatStyleFormatter


def init_logging():
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    console_level = "DEBUG"
    console_handler = logging.StreamHandler(stream=sys.stdout)
    console_handler.setLevel(console_level)
    console_format = "%(asctime)s - %(levelname)-8s - %(name)-25s - %(message)s"
    colored_formatter = ColorizedArgsFormatter(console_format)
    console_handler.setFormatter(colored_formatter)
    root_logger.addHandler(console_handler)

    file_handler = logging.FileHandler("app.log")
    file_level = "DEBUG"
    file_handler.setLevel(file_level)
    file_format = "%(asctime)s - %(name)s (%(lineno)s) - %(levelname)-8s - %(threadName)-12s - %(message)s"
    file_handler.setFormatter(BraceFormatStyleFormatter(file_format))
    root_logger.addHandler(file_handler)


init_logging()
logger = logging.getLogger(__name__)
logger.info("Hello World")
logger.info("Request from {} handled in {:.3f} ms", socket.gethostname(), 11)
logger.info("Request from {} handled in {:.3f} ms", "127.0.0.1", 33.1)
logger.info("My favorite drinks are {}, {}, {}, {}", "milk", "wine", "tea", "beer")
logger.debug("this is a {} message", logging.getLevelName(logging.DEBUG))
logger.info("this is a {} message", logging.getLevelName(logging.INFO))
logger.warning("this is a {} message", logging.getLevelName(logging.WARNING))
logger.error("this is a {} message", logging.getLevelName(logging.ERROR))
logger.critical("this is a {} message", logging.getLevelName(logging.CRITICAL))
logger.info("Does old-style formatting also work? %s it is, but no colors (yet)", True)
