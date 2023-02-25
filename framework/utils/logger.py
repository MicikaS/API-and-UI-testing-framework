from loguru import logger
import sys

LOGS = "logs/"
FORMAT = "<cyan>[{level}]</cyan> -  <yellow>{time:YYYY-MM-DD at HH:mm:ss}</yellow> - <white>{function}</white> - <blue>{message}</blue> "


def set_file_logger(test_name: str):
    handler_id = logger.add(LOGS + test_name + ".log", format=FORMAT)
    return logger, handler_id


def set_console_logger():
    logger.remove()
    logger.add(sys.stdout, format=FORMAT, colorize=True)
