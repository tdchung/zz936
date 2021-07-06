# -*- coding: utf-8 -*-
"""
Usage :
  from util_log import log,log2,loge,logw
  log('ok1', 'ok2')

Severity levels
# Level name    Severity value  Logger method
# TRACE         5               logger.trace()
# DEBUG         10              logger.debug()
# INFO          20              logger.info()
# SUCCESS       25              logger.success()
# WARNING       30              logger.warning()
# ERROR         40              logger.error()
# CRITICAL      50              logger.critical()
"""
import sys
import logging
from logging.handlers import SocketHandler
from pathlib import Path

import yaml
from loguru import logger

#####################################################################################
root = Path(__file__).resolve().parent
LOG_CONFIG_PATH = root / "config_log.yaml"


# "socket_test", 'default'  'debug0;
LOG_TEMPLATE = "debug0"



#####################################################################################
def logger_setup(log_config_path: str = None, log_template: str = "default", **kwargs):
    """ Generic Logging setup
      Overide logging using loguru setup
      1) Custom config from log_config_path .yaml file
      2) Use shortname log, log2, logw, loge for logging output
    Args:
        log_config_path:
        template_name:
        **kwargs:
    Returns:None

    TODO:

    """
    try:
        with open(log_config_path, "r") as fp:
            cfg = yaml.safe_load(fp)

    except Exception as e:
        logging.getLogger().warning(f"Cannot load yaml file {log_config_path}, Using Default logging setup")
        cfg = {"log_level": "DEBUG", "handlers": {"default": [{"sink": "sys.stdout"}]}}

    ########## Parse handlers  ####################################################
    globals_, handlers = cfg, cfg.pop("handlers")[log_template]

    rotation = globals_.pop("rotation")

    for handler in handlers:
        if 'sink' not in handler : continue

        if handler["sink"] == "sys.stdout":
            handler["sink"] = sys.stdout

        elif handler["sink"] == "sys.stderr":
            handler["sink"] = sys.stderr

        elif handler["sink"].startswith("socket"):
            sink_data = handler["sink"].split(",")
            ip        = sink_data[1]
            port      = int(sink_data[2])
            handler["sink"] = SocketHandler(ip, port)

        elif ".log" in handler["sink"] or ".txt" in handler["sink"]:
            handler["rotation"] = handler.get("rotation", rotation)

        # override globals values
        for key, value in handler.items():
            if key in globals_:
                globals_[key] = value

        handler.update(globals_)

    ########## Addon config  ##############################################
    logger.configure(handlers=handlers)


    ########## Custom log levels  #########################################
    # configure log level in config_log.yaml to be able to use logs depends on severity value
    # if no=9 it means that you should set log level below DEBUG to see logs,
    try:
        logger.level("DEBUG_2", no=9, color="<cyan>")

    except Exception as e:
        ### Error when re=-defining level
        print('warning', e)

    return logger


#######################################################################################
##### Initialization root logger at the module level (singleton-like) #################
logger_setup(log_config_path=LOG_CONFIG_PATH, log_template=LOG_TEMPLATE)


#######################################################################################
##### Alias ###########################################################################
def log(*s):
    logger.opt(depth=1, lazy=True).info(",".join([str(t) for t in s]))


def log2(*s):
    logger.opt(depth=1, lazy=True).debug(",".join([str(t) for t in s]))


def log3(*s):  ### Debuggine level 2
    # to enable debug2 logs set level: TRACE in config_log.yaml
    logger.opt(depth=1, lazy=True).log("DEBUG_2", ",".join([str(t) for t in s]))


def logw(*s):
    logger.opt(depth=1, lazy=True).warning(",".join([str(t) for t in s]))


def logc(*s):
    logger.opt(depth=1, lazy=True).critical(",".join([str(t) for t in s]))


def loge(*s):
    logger.opt(depth=1, lazy=True).exception(",".join([str(t) for t in s]))


def logr(*s):
    logger.opt(depth=1, lazy=True).error(",".join([str(t) for t in s]))


#########################################################################################
def test():
    log3("debug2")
    log2("debug")
    log("info")
    logw("warning")
    loge("error")
    logc("critical")

    try:
        a = 1 / 0
    except Exception as e:
        logr("error", e)
        loge("Catcch"), e


#######################################################################################
#######################################################################################
def z_logger_stdout_override():
    """ Redirect stdout --> logger
    Returns:
    """
    import contextlib
    import sys
    class StreamToLogger:
        def __init__(self, level="INFO"):
            self._level = level

        def write(self, buffer):
            for line in buffer.rstrip().splitlines():
                logger.opt(depth=1).log(self._level, line.rstrip())

        def flush(self):
            pass

    logger.remove()
    logger.add(sys.__stdout__)

    stream = StreamToLogger()
    with contextlib.redirect_stdout(stream):
        print("Standard output is sent to added handlers.")


def z_logger_custom_1():
    import logging
    import sys
    from pprint import pformat
    from loguru._defaults import LOGURU_FORMAT

    # LOGURU_FORMAT = "<green>{time:DD.MM.YY HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | <level>{message}</level>"
    LOGURU_FORMAT = "<green>{time:DD.MM.YY HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>"

    class InterceptHandler(logging.Handler):
        """Logs to loguru from Python logging module"""

        def emit(self, record: logging.LogRecord) -> None:
            try:
                level = logger.level(record.levelname).name
            except ValueError:
                level = str(record.levelno)

            frame, depth = logging.currentframe(), 2
            while frame.f_code.co_filename == logging.__file__:  # noqa: WPS609
                # frame = cast(FrameType, frame.f_back)
                frame = frame.f_back
                depth += 1

            logger.opt(depth=depth, exception=record.exc_info).log(
                level,
                record.getMessage(),
            )

    def format_record(record: dict) -> str:
        """
        Custom format for loguru loggers.
        Uses pformat for log any data like request/response body during debug.
        Works with logging if loguru handler it.
        Example:
        >>> payload = [{"users":[{"name": "Nick", "age": 87, "is_active": True}, {"name": "Alex", "age": 27, "is_active": True}], "count": 2}]
        >>> logger.bind(payload=).debug("users payload")
        >>> [   {   'count': 2,
        >>>         'users': [   {'age': 87, 'is_active': True, 'name': 'Nick'},
        >>>                      {'age': 27, 'is_active': True, 'name': 'Alex'}]}]
        """

        format_string = LOGURU_FORMAT
        if record["extra"].get("payload") is not None:
            record["extra"]["payload"] = pformat(
                record["extra"]["payload"], indent=4, compact=True, width=88
            )
            format_string += "\n<level>{extra[payload]}</level>"

        format_string += "{exception}\n"
        return format_string

    def setup_logging():
        # intercept everything at the root logger
        logging.root.handlers = [InterceptHandler()]
        logging.root.setLevel("INFO")

        # remove every other logger's handlers
        # and propagate to root logger
        for name in logging.root.manager.loggerDict.keys():
            logging.getLogger(name).handlers = []
            logging.getLogger(name).propagate = True

        # configure loguru
        logger.configure(
            handlers=[
                {
                    "sink": sys.stdout,
                    "level": logging.DEBUG,
                    "format": format_record,
                }
            ]
        )
        logger.level("TIMEIT", no=22, color="<cyan>")



def z_logging_only():
    """ Logging utilities. """
    import logging
    import os
    from logging import CRITICAL  # NOQA
    from logging import DEBUG  # NOQA
    from logging import ERROR  # NOQA
    from logging import FATAL  # NOQA
    from logging import INFO  # NOQA
    from logging import NOTSET  # NOQA
    from logging import WARN  # NOQA
    from logging import WARNING  # NOQA
    from typing import Optional

    log_levels = {
        "debug": logging.DEBUG,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "info": logging.INFO,
        "critical": logging.CRITICAL,
    }

    _default_log_level = logging.WARNING


    def _get_default_logging_level():
        """
        If DATASETS_VERBOSITY env var is set to one of the valid choices return that as the new default level.
        If it is not - fall back to ``_default_log_level``
        """
        env_level_str = os.getenv("DATASETS_VERBOSITY", None)
        if env_level_str:
            if env_level_str in log_levels:
                return log_levels[env_level_str]
            else:
                logging.getLogger().warning(
                    f"Unknown option DATASETS_VERBOSITY={env_level_str}, "
                    f"has to be one of: { ', '.join(log_levels.keys()) }"
                )
        return _default_log_level


    def _get_library_name() -> str:
        return __name__.split(".")[0]


    def _get_library_root_logger() -> logging.Logger:
        return logging.getLogger(_get_library_name())


    def _configure_library_root_logger() -> None:
        # Apply our default configuration to the library root logger.
        library_root_logger = _get_library_root_logger()
        library_root_logger.setLevel(_get_default_logging_level())


    def _reset_library_root_logger() -> None:
        library_root_logger = _get_library_root_logger()
        library_root_logger.setLevel(logging.NOTSET)


    def get_logger(name: Optional[str] = None) -> logging.Logger:
        """Return a logger with the specified name.
        This function can be used in dataset and metrics scripts.
        """
        if name is None:
            name = _get_library_name()
        return logging.getLogger(name)


    def get_verbosity() -> int:
        """Return the current level for the library's root logger.
        """
        return _get_library_root_logger().getEffectiveLevel()


    def set_verbosity(verbosity: int) -> None:
        """Set the level for the library's root logger.
        Args:
            verbosity:
                Logging level, e.g., ``datasets.logging.DEBUG`` and ``datasets.logging.INFO``.
        """
        _get_library_root_logger().setLevel(verbosity)


    def set_verbosity_info():
        """Set the level for the library's root logger to INFO.
        """
        return set_verbosity(INFO)


    def set_verbosity_warning():
        """Set the level for the library's root logger to WARNING.
        """
        return set_verbosity(WARNING)


    def set_verbosity_debug():
        """Set the level for the library's root logger to DEBUG.
        """
        return set_verbosity(DEBUG)


    def set_verbosity_error():
        """Set the level for the library's root logger to ERROR.
        """
        return set_verbosity(ERROR)


    def disable_propagation() -> None:
        """Disable propagation of the library log outputs.
        Note that log propagation is disabled by default.
        """
        _get_library_root_logger().propagate = False


    def enable_propagation() -> None:
        """Enable propagation of the library log outputs.
        Please disable the library's default handler to prevent double logging if the root logger has
        been configured.
        """
        _get_library_root_logger().propagate = True


    # Configure the library root logger at the module level (singleton-like)
    _configure_library_root_logger()





############################################################################
if __name__ == "__main__":
    test()
