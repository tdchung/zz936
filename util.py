
""""
gin usage


congig.gin

import use_gin
my_other_func.a = -2.9
my_other_func.b = 9.3

# Comments!
my_other_func.c = 'Oh, Dear.'
test.py

import gin
gin.parse_config_file('config.gin')
import use_gin
print(use_gin.my_other_func())
use_gin.py

import gin
@gin.configurable
def my_other_func(a, b, c):
  return a, b, c



"""



def example_gin():
  import ginin
  
  name = "prod/config_gin"
  
  gin.parse_config_file( f"config/{name}" )
  """
  ### config/config_gin.gin
  myfun.a1 = [1,2,3]
  myfun.a3 = True



  """

  @gin.configurable
  def myfun(a1=1,a2=2):
     return a1,a2



  
  

def config_load(config_path:str = None, 
                path_default:str=None, 
                config_default:dict=None):
    """Load Config file into a dict
    1) load config_path
    2) If not, load in HOME USER
    3) If not, create default one
    Args:
        config_path: path of config or 'default' tag value
    Returns: dict config
    """
    import json, yaml
    from Path import pathlib

    path_default        = pathlib.Path.home() / ".mygenerator" if path_default is None else path_default
    config_path_default = path_default / "config.yaml"
    if config_default is None :
        config_default = {
            "current_dataset": "mnist",
            "datasets": {
                "mnist": {
                    "url": "/mnist_png.tar.gz",
                    "path": ""),
                }
            },
        }

    #####################################################################
    if config_path is None or config_path == "default":
        log(f"Using config: {config_path_default}")
        config_path = config_path_default
    else :
        config_path = pathlib.Path(config_path)
        
    try:
        log("loading config", config_path)
        if ".yaml" in config_path :
            cfg = yaml.load(config_path.read_text(), Loader=yaml.Loader)
            dd = {}
            for x in cfg :   ### Map to dict
                for key,val in x.items():
                   dd[key] = val
            return cfg

        if ".json" in config_path :
           return json.load(config_path.read_text())

    except Exception as e:
        log(f"Cannot read yaml/json file {config_path}", e)


    log("#### Using default configuration")
    log(config_default)
    log(f"Creating config file in {config_path_default}")
    os.makedirs(path_default, exist_ok=True)
    with open(config_path_default, mode="w") as fp:
        yaml.dump(config_default, fp)
    return config_default


class to_namespace(object):
    ### Dict into Namespace
    def __init__(self, d):
        self.__dict__ = d
        
  
  
  
  
  
from loguru import logger

##########################################################################################
################### Logs Wrapper #########################################################
def log(*s):
    logger.info(",".join([str(t) for t in s]))


def log2(*s):
    logger.debug(",".join([str(t) for t in s]))


def logw(*s):
    logger.warning(",".join([str(t) for t in s]))


def loge(*s):
    logger.error(",".join([str(t) for t in s]))


def logger_setup():
    config = {
        "handlers": [
            {
                "sink": sys.stdout,
                "format": "<level>{level: <8}</level>| <level>{message}</level>",
            }
        ]
    }
    logger.configure(**config)


logger_setup()

  
  
  
config2 = {
    "handlers": [
        { "sink": sys.stdout,
          "format": "<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        },

        {
            "sink": sys.stderr,
            "format": "<level>{level: <8}</level>|<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        }


    ]
}









class Logger_setup():
    """Logging class with loguru module.
    """

    def logger_setup(self):
        data_root = Path(__file__).resolve().parent / "data/log"
        today = datetime.now().strftime("%Y%m")
        data_file = "{}.log".format(datetime.now().strftime("%Y%m%d"))
        data_dir = data_root / today
        dst = data_dir / data_file
        data_dir.mkdir(parents=True, exist_ok=True)
        logger.add(dst, format="[{level} {time:YYYY-MM-dd HH:mm:ss:SSS}] {message}")

    def get_log_dst(self):
        """Determines the file to write log to.
        The format of the filename is   The log file is stored in the 'data/log' directory.
        """
        data_root = Path(__file__).resolve().parent / "data/log"
        today = datetime.now().strftime("%Y%m")
        data_file = "{}.log".format(datetime.now().strftime("%Y%m%d"))
        data_dir = data_root / today
        data_dir.mkdir(parents=True, exist_ok=True)
        dst = data_dir / data_file
        logger.remove()
        logger.add(str(dst), format="[{level} {time:YYYY-MM-DD HH:mm:ss:SSS}] {message}")

    def log(self, level: str='info', msg:str=''):
        """Writes a message to log file.
        The message is written to the file determined in the 'get_log_dst`. The
        logging level shows the importtance of the message and is classfied by
        as follows.
            - info : Information
            - success: Operation success such as login and logout
            - error: Operation failure such as login and logout
        Args:
            msg (str)): A message to write
            level (str): Logging level
        """
        self.get_log_dst()
        if level == "info":
            logger.info(msg)
        elif level == "success":
            logger.success(msg)
        elif level == "error":
            logger.error(msg)
        elif level == "warning":
            logger.warning(msg)
            
            
            
def logger_setup3():  
    import logging
    import sys
    from pprint import pformat
    from loguru import logger
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
    
    
    
    
    
##########################################################################################
def config_load(config_path:str='config.yaml'):
    """  Load Config file into a dict
    Args:
        config_path: path of config
    Returns: dict config
    """
    #Load the yaml config file
    with open(config_path, "r") as yamlfile:
        config_data = yaml.load(yamlfile, Loader=yaml.FullLoader)

    dd = {}
    for x in config_data :
        for key,val in x.items():
           dd[key] = val

    return dd


##########################################################################################


  
  
  
  
