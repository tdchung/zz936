# -*- coding: utf-8 -*-
import sys, os
from pathlib import Path

import yaml
from loguru import logger

#####################################################################################
root = Path(__file__).resolve().parent
LOG_TEMPLATE = "mytemplate2"
LOG_CONFIG_PATH = root / "config_log.yaml"

# try :
#    os.environ['config_log']


#####################################################################################
def logger_setup(log_config_path: str = None, log_template: str = "default", **kwargs):
    """ Generic Logging setup
      Overide logging using loguru setup
      1) Default Config using log_level and log_format.
      2) Custom config from log_config_path .yaml file
      3) Use shortname log, log2, logw, loge for logging output

    Options
    #logger.add(log_file_name,level=level,format=format,
    #    rotation="30 days", filter=None, colorize=None, serialize=False, backtrace=True, enqueue=False, catch=True)

    Args:
        log_level:
        log_config_path:
        template_name:
        **kwargs:

    Returns:

    """
    try:
        with open(log_config_path, "r") as fp:
            cfg = yaml.safe_load(fp)

    except Exception as e:
        print(f"Cannot load yaml file {log_config_path}, Using Default logging setup")
        cfg = {"log_level": "INFO", "handlers": {"default": [{"sink": "sys.stdout"}]}}

    ########## Parse handlers  ####################################################
    globals_, handlers = cfg, cfg.pop("handlers")[log_template]

    rotation = globals_.pop("rotation")

    for handler in handlers:
        if handler["sink"] == "sys.stdout":
            handler["sink"] = sys.stdout

        elif handler["sink"] == "sys.stderr":
            handler["sink"] = sys.stderr

        elif  ".log" in handler["sink"] or ".txt" in handler["sink"]   :
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
    # severity levels table attached in config_log.yaml
    # logger.level("TIMEIT", no=22, color="<cyan>")
    logger.level("debug2", no=9, color="<cyan>")
    return logger


##### Initialization ####################################################
logger_setup(log_config_path=LOG_CONFIG_PATH, log_template=LOG_TEMPLATE)


def log(*s):
    logger.opt(depth=1).info(",".join([str(t) for t in s]))


def log2(*s):
    logger.opt(depth=1).debug(",".join([str(t) for t in s]))


def log3(*s):  ### Debuggine level 2
    # to enable debug2 logs set level: TRACE in config_log.yaml
    logger.opt(depth=1).log("debug2", ",".join([str(t) for t in s]))


def logw(*s):
    logger.opt(depth=1).warning(",".join([str(t) for t in s]))


def logc(*s):
    logger.opt(depth=1).critical(",".join([str(t) for t in s]))


def loge(*s):
    logger.opt(depth=1).error(",".join([str(t) for t in s]))


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
        loge("error", e)


if __name__ == "__main__":
    test()
