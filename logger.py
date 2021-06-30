import sys

import yaml
from loguru import logger
from yaml import YAMLError


def logger_setup(
    log_level: str = None,
    log_config_path: str = None,
    template_name: str = "default",
    backtrace=True,
    diagnose=True,
    **kwargs,
):
    """ Generic Logging setup

      Overide logging using loguru setup
      1) Default Config using log_level and log_format.
      2) Custom config from log_config_path .yaml file
      3) Use shortname log, log2, logw, loge for logging output


      config_log.yaml


     Options
    #logger.add(log_file_name,level=level,format=format,
    #    rotation="30 days", filter=None, colorize=None, serialize=False, backtrace=True, enqueue=False, catch=True)


    """
    try:
        with open(log_config_path, "r") as fp:
            cfg = yaml.safe_load(fp)

    except YAMLError as e:
        cfg = {"log_level": "INFO", "handlers": {"default": [{"sink": "sys.stdout"}]}}
        print(f"Could not load {log_config_path}: {e!r}. Using default {cfg}")

    ########## Parse handlers  ####################################################
    handlers = cfg["handlers"][template_name]

    for i, handler in enumerate(handlers):
        if handler["sink"] == "sys.stdout":
            handler["sink"] = sys.stdout
        elif handler["sink"] == "sys.stderr":
            handler["sink"] = sys.stderr

        handlers[i] = handler

    ########## Create loguru config  ##############################################
    logger.configure(handlers=handlers)
    logger.level("TIMEIT", no=22, color="<cyan>")

    return logger


def test_logger_setup():
    logger_setup(log_config_path="config_log.yaml", template_name="mytemplate3")
    logger.info("info level")
    logger.error("error level")
