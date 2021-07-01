import logging
import traceback
from datetime import datetime
from logging.config import fileConfig


def get_logger():
    """
    logger function creates a logging instance globally per process.
    """
    fileConfig("config_log.ini")

    return logging


def add_handler(handler, level="info", format=None):
    """
    Adds a logging handler

    Args:
    handler:  Accepts a new handler class
    level:    Accepts any level
    format:   Accepts message format, None by default

    example:  add_handler(logging.StreamHandler(), level='info')
    """
    logging.debug(
        "Handler requested to add in logging instance -> {}".format(type(handler))
    )
    numeric_level = getattr(logging, level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError("Invalid log level: %s" % loglevel)

    try:
        handler.setLevel(numeric_level)
        handler.setFormatter(format)
        handler.flush()
        logging.getLogger().addHandler(handler)
    except Exception as e:
        print(
            "Exception occurred while adding a handler to logger instance -> ",
            traceback.format_exc(),
        )
        raise Exception("Could not add handler. Exiting...")


def remove_handler(handler):
    """
    Removes a logging handler

    Args:
    handler:  Accepts a handler class to remove

    example:  remove_handler(logging.StreamHandler()
    """
    logging.debug(
        "Handler requested to remove from logging instance -> {}".format(type(handler))
    )
    try:
        if logging.getLogger().hasHandlers():
            for count, h in enumerate(logging.getLogger().handlers):
                if type(h) == type(handler):
                    logging.getLogger().removeHandler(
                        logging.getLogger().handlers[count]
                    )
    except Exception as e:
        print(
            "Exception occurred while removing a handler from logger instance -> ",
            traceback.format_exc(),
        )
        raise Exception("Could not remove a handler. Exiting...")

    logging.debug("Remaining log handlers -> {}".format(logging.getLogger().handlers))
