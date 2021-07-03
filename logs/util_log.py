# -*- coding: utf-8 -*-
"""
# The severity levels
# Level name	Severity value	Logger method
# TRACE	        5	            logger.trace()
# DEBUG	        10	            logger.debug()
# INFO	        20	            logger.info()
# SUCCESS	    25	            logger.success()
# WARNING	    30	            logger.warning()
# ERROR	        40	            logger.error()
# CRITICAL	    50	            logger.critical()
"""
import sys, os
from pathlib import Path

import yaml
from loguru import logger
from logging.handlers import SocketHandler


#####################################################################################
root = Path(__file__).resolve().parent
LOG_CONFIG_PATH = root / "config_log.yaml"

# "socket_test", 'default'
#
#
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
        print(f"Cannot load yaml file {log_config_path}, Using Default logging setup")
        cfg = {"log_level": "DEBUG", "handlers": {"default": [{"sink": "sys.stdout"}]}}

    ########## Parse handlers  ####################################################
    globals_, handlers = cfg, cfg.pop("handlers")[log_template]

    rotation = globals_.pop("rotation")

    for handler in handlers:
        if handler["sink"] == "sys.stdout":
            handler["sink"] = sys.stdout

        elif handler["sink"] == "sys.stderr":
            handler["sink"] = sys.stderr
        
        elif handler["sink"].startswith("socket"):
            sink_data = handler["sink"].split(",")
            ip = sink_data[1]
            port = int(sink_data[2])
            handler["sink"] = SocketHandler(ip, port)

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
    try :
       logger.level("DEBUG_2", no=9, color="<cyan>")

    except Exception as e:
       ### Error when re=-defining
       print('warning', e)


    return logger




def logger_stdout_override():
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




############################################################################
##### Initialization #######################################################
logger_setup(log_config_path=LOG_CONFIG_PATH, log_template=LOG_TEMPLATE)



############################################################################
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


############################################################################
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



############################################################################
if __name__ == "__main__":
    test()
