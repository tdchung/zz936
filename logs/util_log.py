# -*- coding: utf-8 -*-
import sys
import yaml
from loguru import logger

#####################################################################################
LOG_TEMPLATE = 'template2'
LOG_CONFIG_PATH= 'config_log.yaml'



#####################################################################################
def logger_setup(log_level:str=None,
                 log_config_path:str=None,
                 template_name:str='default',
                 backtrace=True, diagnose=True, **kwargs):
    """ Generic Logging setup

      Overide logging using loguru setup
      1) Default Config using log_level and log_format.
      2) Custom config from log_config_path .yaml file
      3) Use shortname log, log2, logw, loge for logging output

    Options
    #logger.add(log_file_name,level=level,format=format,
    #    rotation="30 days", filter=None, colorize=None, serialize=False, backtrace=True, enqueue=False, catch=True)


    """
    try :
        with open(log_config_path, "r") as fp:
            cfg = yaml.safe_load(fp)

    except Exception as e:
         print("Using Default hardcooded")
         cfg = {
            'log_level' : 'INFO',
            'handlers'  : {'default' : [{'sink' : 'sys.stdout'}]}
         }

    ########## Parse handlers  ####################################################
    handlers  =  cfg["handlers"][template_name]

    for i, hndl in enumerate( handlers) :
        if hndl["sink"] == "sys.stdout":
                hndl["sink"] = sys.stdout

        elif hndl["sink"] == "sys.stderr":
                hndl["sink"] = sys.stderr

        handlers[i] = hndl


    ########## Create loguru config  ##############################################
    logger.configure(handlers= handlers )
    logger.level("TIMEIT", no=22, color="<cyan>")

    return logger



##### Initialization ####################################################
logger_setup(log_template=LOG_TEMPLATE , log_config_path= LOG_CONFIG_PATH)


def log(*s):
  logger.info(",".join([str(t) for t in s]))


def log2(*s):
  logger.debug(",".join([str(t) for t in s]))


def log3(*s):  ### Debuggine level 2
  logger.log("debug2", ",".join([str(t) for t in s]))


def logw(*s):
  logger.warning(",".join([str(t) for t in s]))


def logc(*s):
  logger.critical(",".join([str(t) for t in s]))


def loge(*s):
   logger.error(",".join([str(t) for t in s]))










