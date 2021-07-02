from loguru import logger
import yaml
from yaml import YAMLError
import sys

def get_logger(config_path, template):
    """
    logger function creates a logging instance globally per process.
    """
    try:
        with open(config_path, "r") as fp:
            config = yaml.safe_load(fp)

    except YAMLError as err:
        config = {"log_level": "INFO", "handlers": {"default": [{"sink": "sys.stdout"}]}}
        print("Exception : {} ".format(err))


    handlers = config['handlers'][template]

    for i, handler in enumerate(handlers):
        if handler["sink"] == "sys.stdout":
            handler["sink"] = sys.stdout
        elif handler["sink"] == "sys.stderr":
            handler["sink"] = sys.stderr

        handlers[i] = handler


    logger.configure(handlers=handlers)
    logger.add(level=config['log_level'])

    return logger


def asdasdad(asd='s',
                zczxc='asd'):
    pass