


####################################################################################
####################################################################################
def config_load(config_path:str = None,
                path_default:str=None,
                config_default:dict=None,
                save_default:bool=False,
                to_dataclass:bool=True
                ):
    """Load Config file into a dict
    1) load config_path
    2) If not, load in USER/.myconfig/.config.yaml
    3) If not, create default save in USER/.myconfig/.config.yaml
    Args:
        config_path:   path of config or 'default' tag value
        path_default : path of default config
        config_default: dict value of default config
        save_default: save default config on disk 
    Returns: dict config
    """
    import json, yaml, pathlib

    #########Default value setup ###########################################
    path_default        = pathlib.Path.home() / ".myconfig" if path_default is None else path_default
    config_path_default = path_default / "config.yaml"
    if config_default is None :
        config_default = {
            "field1": "",
            "field2": {}
        }

    #########Config path setup #############################################
    if config_path is None or config_path == "default":
        log(f"Config: Using {config_path_default}" )
        config_path = config_path_default
    else :
        config_path = pathlib.Path(config_path)

    ######### Load Config ##################################################
    try:
        log("Config: Loading ", config_path)
        if config_path.endswith(".yaml") :
            cfg = yaml.safe_load(config_path.read_text())
            dd  = {}
            for x in cfg :   ### Map to dict
                for key,val in x.items():
                   dd[key] = val
            return cfg

        elif config_path.endswith(".json") :
           cfg = json.loads(config_path.read_text())

        elif config_path.endswith(".properties") or config_path.endswith(".ini") :
           from configparser import SafeConfigParser
           cfg = SafeConfigParser()
           cfg.read(str(config_path))

        elif config_path.endswith(".toml") :
           import toml 
           cfg = toml.loads(config_path.read_text())

        else :
           raise Exception( f'not supported file {config_path}')   

        class to_namespace(object):
            ### Dict into Namespace
            def __init__(self, d):
                self.__dict__ = d

        if to_dataclass :   ### myconfig.val  , myconfig.val2
            return to_namespace(cfg)
        return cfg


    except Exception as e:
        log(f"Config: Cannot read file {config_path}", e)

    ######################################################################
    log("Config: Using default config")
    log(config_default)
    if save_default:
        log(f"Config: Writingg config in {config_path_default}")
        os.makedirs(path_default, exist_ok=True)
        with open(config_path_default, mode="w") as fp:
            yaml.dump(config_default, fp)
    return config_default



def config_validate_pydantic(config_dict:dict = None,
                    pydantic_file_path:str='config.validate.myclassname.py',):
    #config_validate_path:=None,):
    """Validate configuration based on template type validator
        wiht Pydantic
        
    Returns: dict config
    """
    import json, yaml, pathlib
    
    
    
    
    
    

def config_validate(config_dict:dict = None,
                    config_validate_dict:dict=None,):
    #config_validate_path:=None,):
    """Validate configuration based on template type validator

        cfg_validator = {
      'f1' :{
         'v1':  'int,<=10,>=0',
         'v2':  'float,>-1.0,<100.5',
         'v3':  'bool',
         'v3':  'enum,one|two|three|',
         'v4':  'list',
         'v5':  'dict'
      }
    }
    Returns: dict config
    """
    import json, yaml, pathlib


    def is_valid(x, rules_str):

      r1    = rules_str.split(",")[0]
      type1 = r1[0]

      if type1 == 'bool':
        return isinstance(x, bool)

      elif type1 == 'int':
        if isinstance(x, float) :
            if len(r1)>=1 :
                res = eval( f"{x}{r1[1]}")
                if res and len(r1)>=2 :
                   res2 = eval( f"{x}{r1[2]}")
                   return res2
                else :
                   return res
            else :
                return True            


      elif type1 == 'float':
          if isinstance(x, float) :
            if len(r1)>=1 :
                res = eval( f"{x}{r1[1]}")
                if res and len(r1)>=2 :
                   res2 = eval( f"{x}{r1[2]}")
                   return res2
                else :
                   return res
            else :
                return True       
                      
          return False 
      else :
        return True


    #### Recursively parse a dict  ########################################
    cfg_val = {

      'f1' :{
         'v1':  'int,<=10,>=0',
         'v2':  'float,>-1.0,<100.5',
         'v3':  'bool',
         'v3':  'enum,one|two|three|',
         'v4':  'list',
         'v5':  'dict'
      }
    }
    
    cfg_list = to_list(config_dict)

    for i, (key,val) in enumerate(cfg_list):
       rulei = cfg_validate[key]
       assert is_valid(val, rulei) , f'{i}, {key}, {val} invalid: {rulei}'


    #######################################################################
    log("Config: Using default config")
    log(config_default)
    if save_default:
        log(f"Config: Writingg config in {config_path_default}")
        os.makedirs(path_default, exist_ok=True)
        with open(config_path_default, mode="w") as fp:
            yaml.dump(config_default, fp)
    return config_default









###########################################################################################################
###########################################################################################################
from loguru import logger

def logger_setup(log_level:str=None, log_template:str=None, log_config_path:str=None,
    backtrace=True, diagnose=True):
    """ Generic Logging setup
     logger.add(log_file_name,level=level,format=format, 
        rotation="30 days", filter=None, colorize=None, serialize=False, backtrace=True, enqueue=False, catch=True)
      Overried logging using loguru setup
      1) Default Config using log_level and log_format.
      2) Custom config from log_config_path .yaml file
      3) Use shortname log, log2, logw, loge for logging output


      log_config.yaml

        log_level : INFO

        log_format : format0
        handlers :
            handle1:
               sinK : std.out
               format : format1



        format_dict:
              'format0': "<green>{time:DD.MM.YY HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | <level>{message}</level>"
              'format1': "<green>{time:DD.MM.YY HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>",
              'format2': "<level>{level: <8}</level>|<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
              'format3': "<level>{level: <8}</level>|<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",     


    """
    import logging, sys
    from pathlib import Path
    from pprint import pformat
    # from loguru import logger
    from loguru._defaults import LOGURU_FORMAT
    import yaml 

    cfg        = yaml.safe_load(log_config_path) if log_config_path is not None else {}

    ########## Log: init variable  ################################################
    log_level    = log_level  if log_level  is not None else cfg.get('log_level', 'INFO')
    log_template = log_template if log_template is not None else 'template0'

    ########## Log: Format  ######################################################
    log_format = 'format0'
    format_dict = {
      'format0': "<green>{time:DD.MM.YY HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | <level>{message}</level>",
      'format1': "<green>{time:DD.MM.YY HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>",
      'format2': "<level>{level: <8}</level>|<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
      'format3': "<level>{level: <8}</level>|<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    }
    format_dict   = cfg.get('format_dict', format_dict)
    LOGURU_FORMAT = format_dict[log_format]


    ##############################################################################  
    class loggingInterceptHandler(logging.Handler):
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
            logger.opt(depth=depth, exception=record.exc_info).log( level, record.getMessage(),)


    def format_record_custom(record: dict) -> str:
        """ Custom format for loguru loggers.
        Uses pformat for log any data like request/response body during debug. Works with logging if loguru handler it.
        Example:
        >>> payload = [{"users":[{"name": "Nick", "age": 87, "is_active": True}, {"name": "Alex", "age": 27, "is_active": True}], "count": 2}]
        >>> logger.bind(payload=).debug("users payload")
        >>> [   {   'count': 2,
        >>>         'users': [   {'age': 87, 'is_active': True, 'name': 'Nick'},
        >>>                      {'age': 27, 'is_active': True, 'name': 'Alex'}]}]
        """
        format_string = LOGURU_FORMAT
        if record["extra"].get("payload") is not None:
            record["extra"]["payload"] = pformat( record["extra"]["payload"], indent=4, compact=True, width=88
            )
            format_string += "\n<level>{extra[payload]}</level>"

        format_string += "{exception}\n"
        return format_string


    def handler_custom():
        """Determines the file to write log to.
        The format of the filename is   The log file is stored in the 'data/log' directory.
        """
        data_root              = Path(__file__).resolve().parent / "data/log"
        today                  = datetime.now().strftime("%Y%m")
        data_file              = "{}.log".format(datetime.now().strftime("%Y%m%d"))
        data_dir               = data_root / today
        data_dir.mkdir(parents = True, exist_ok=True)
        dst                    = data_dir / data_file
        logger.remove()
        logger.add(str(dst), format="[{level} {time:YYYY-MM-DD HH:mm:ss:SSS}] {message}")


    def get_handlers(ddict):
        return ddict


    def loguru_setup():
        # intercept everything at the root logger
        logging.root.handlers = [ loggingInterceptHandler()]
        logging.root.setLevel(log_level)

        # Remove every other logger's handlers and propagate to root logger
        for name in logging.root.manager.loggerDict.keys():
            logging.getLogger(name).handlers = []
            logging.getLogger(name).propagate = True

        # configure loguru  from Config File  
        handlers_default = [
             {   "sink": sys.stdout, "level": logging.DEBUG,  # "format": format_record_custom,
                 "format": "format1"   },
             {   "sink": sys.stderr, "level": logging.DEBUG,  "format": "format1"   },
        ]
        handlers = get_handlers(cfg.get('handlers', None))


        if handlers is None :
            logger.configure( handlers= handlers_default ,  backtrace=backtrace, diagnose=diagnose )            
            logger.level("TIMEIT", no=22, color="<cyan>")
        else :
            logger.configure( handlers= handlers_default,  backtrace=backtrace, diagnose=diagnose  ) 
        
    return loguru_setup()



##### Usage   
from loguru import logger
logger_setup(log_level='INFO', log_template='template0', log_config_path=None)


def log(*s):  
  logger.info(",".join([str(t) for t in s]))

def log2(*s): 
  logger.debug(",".join([str(t) for t in s]))

def logw(*s): 
  logger.warning(",".join([str(t) for t in s]))

def logc(*s): 
  logger.critical(",".join([str(t) for t in s]))

def loge(*s): 
   logger.error(",".join([str(t) for t in s]))





























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
                config_default:dict=None,
                save_default=False):
    """Load Config file into a dict
    1) load config_path
    2) If not, load in HOME USER
    3) If not, create default one
    Args:
        config_path: path of config or 'default' tag value
    Returns: dict config
    """
    import json, yaml, pathlib
    path_default        = pathlib.Path.home() / ".myconfig" if path_default is None else path_default
    config_path_default = path_default / "config.yaml"
    if config_default is None :
        config_default = {
            "current_dataset": "",
            "datasets": {}
        }

    #####################################################################
    if config_path is None or config_path == "default":
        log(f"Using config: {config_path_default}" )
        config_path = config_path_default
    else :
        config_path = pathlib.Path(config_path)

    try:
        log("loading config", config_path)
        if config_path.endswith(".yaml") :
            cfg = yaml.safe_load(config_path.read_text())
            dd = {}
            for x in cfg :   ### Map to dict
                for key,val in x.items():
                   dd[key] = val
            return cfg

        elif config_path.endswith(".json") :
           return json.loads(config_path.read_text())

        elif config_path.endswith(".properties") or config_path.endswith(".ini") :
           from configparser import SafeConfigParser
           cfg = SafeConfigParser()
           cfg.read(str(config_path))
           return cfg  ### Can be used as dict

    except Exception as e:
        log(f"Cannot read yaml/json file {config_path}", e)

    #####################################################################
    log("#### Using default configuration")
    log(config_default)
    if save_default:
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
    
    
    
    

        
#############################################################################################        
# pylint: disable=C0321,C0103,E1221,C0301,E1305,E1121,C0302,C0330
# -*- coding: utf-8 -*-
"""
https://docs.python-guide.org/writing/logging/
https://docs.python.org/3/howto/logging-cookbook.html

python util_log.py test_log


"""
import logging
import os
import random
import socket
import sys
from logging.handlers import TimedRotatingFileHandler
import datetime
import yaml

################### Logs #################################################################
APP_ID  = __file__ + "_" + str(os.getpid()) + "_" + str(socket.gethostname())
APP_ID2 = str(os.getpid()) + "_" + str(socket.gethostname())

LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logfile.log")

FORMATTER_0 = logging.Formatter("%(message)s")
FORMATTER_1 = logging.Formatter("%(asctime)s,  %(name)s, %(levelname)s, %(message)s")
FORMATTER_2 = logging.Formatter("%(asctime)s.%(msecs)03dZ %(levelname)s %(message)s")
FORMATTER_3 = logging.Formatter("%(asctime)s  %(levelname)s %(message)s")
FORMATTER_4 = logging.Formatter("%(asctime)s, %(process)d, %(filename)s,    %(message)s")

FORMATTER_5 = logging.Formatter(
    "%(asctime)s, %(process)d, %(pathname)s%(filename)s, %(funcName)s, %(lineno)s,  %(message)s"
)


#########################################################################################
def create_appid(filename):
    # appid  = filename + ',' + str(os.getpid()) + ',' + str( socket.gethostname() )
    appid = filename + "," + str(os.getpid())
    return appid


def create_logfilename(filename):
    return filename.split("/")[-1].split(".")[0] + ".log"


def create_uniqueid():
    return datetime.datetime.now().strftime(  "_%Y%m%d%H%M%S_"  )   + str(random.randint(1000, 9999))
    # return arrow.utcnow().to("Japan").format("_YYYYMMDDHHmmss_") + str(random.randint(1000, 9999))


########################################################################################
################### Logger #############################################################
class logger_class(object):
    """
    Higher level of verbosity =1, 2, 3
    logger = logger_class()

    def log(*s):
        logger.log(*s, level=1)

    def log1(*s):
        logger.log(*s, level=1)

    """
    def __init__(self, config_file=None, verbose=True) :
        self.config     = self.load_config(config_file)
        if verbose: print(self.config)
        d = self.config['logger_config']
        self.logger     = logger_setup( **d )
        self.level_max  = self.config.get('verbosity', 1)


    def load_config(self, config_file_path=None) :
        try :
            if config_file_path is None :
                config_file_path = 'config.yaml'

            with open(config_file_path, 'r') as f:
                return yaml.load(f)

        except Exception as e :
            return {'logger_config': {}, 'verbosity': 1}  ## Default parameters


    def log(self,*s, level=1) :
        if level <= self.level_max : 
            self.logger.info(*s)


    def debug(self,*s, level=1) :
        if level <= self.level_max : 
            self.logger.debug(*s)



##########################################################################################
##########################################################################################
def logger_setup(logger_name=None, log_file=None, formatter='FORMATTER_0', isrotate=False, 
    isconsole_output=True, logging_level='info',):
    """
    my_logger = util_log.logger_setup("my module name", log_file="")
    APP_ID    = util_log.create_appid(__file__ )
    def log(*argv):
      my_logger.info(",".join([str(x) for x in argv]))
  
   """
    logging_level = {  'info':logging.INFO, 'debug' : logging.DEBUG }[logging_level]
    formatter     = {'FORMATTER_0': FORMATTER_0, 'FORMATTER_1': FORMATTER_1}.get(formatter, formatter)

    if logger_name is None:
        logger = logging.getLogger()  # Gets the root logger
    else:
        logger = logging.getLogger(logger_name)

    logger.setLevel(logging_level)  # better to have too much log than not enough

    if isconsole_output:
        logger.addHandler(logger_handler_console(formatter))

    if log_file is not None:
        logger.addHandler(
            logger_handler_file(formatter=formatter, log_file_used=log_file, isrotate=isrotate)
        )

    # with this pattern, rarely necessary to propagate the error up to parent
    logger.propagate = False
    return logger


def logger_handler_console(formatter=None):
    formatter = FORMATTER_1 if formatter is None else formatter
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    return console_handler


def logger_handler_file(isrotate=False, rotate_time="midnight", formatter=None, log_file_used=None):
    formatter = FORMATTER_1 if formatter is None else formatter
    log_file_used = LOG_FILE if log_file_used is None else log_file_used
    if isrotate:
        print("Rotate log", rotate_time)
        fh = TimedRotatingFileHandler(log_file_used, when=rotate_time)
        fh.setFormatter(formatter)
        return fh
    else:
        fh = logging.FileHandler(log_file_used)
        fh.setFormatter(formatter)
        return fh


def logger_setup2(name=__name__, level=None):
    _ = level

    # logger defines
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter()
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger




###########################################################################################################
def test_log():
    logger =logger_class(verbose=True)

    def log(*s):
       logger.log(*s, level=1)

    def log2(*s):
       logger.log(*s, level=2)

    def log3(*s):
       logger.log(*s, level=3)

    log( "level 1"  )
    log2( "level 2"  )
    log3( "level 3"  )




  
  
  
