#
# python util_config.py test
#
from typing import Union
import fire
import yamale
import yaml
from box import Box
import os

#########################################################################################################
def log(*s):
    print(*s, flush=True)


def loge(*s):
    print(*s, flush=True)


#########################################################################################################
def config_load(
    config_path: str = None,
    path_default: str = None,
    config_default: dict = None,
    save_default: bool = False,
    to_dataclass: bool = True,
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
    path_default = (
        pathlib.Path.home() / ".myconfig" if path_default is None else path_default
    )
    config_path_default = path_default / "config.yaml"
    if config_default is None:
        config_default = {"field1": "", "field2": {}}

    #########Config path setup #############################################
    if config_path is None or config_path == "default":
        log(f"Config: Using {config_path_default}")
        config_path = config_path_default
    else:
        config_path = pathlib.Path(config_path)

    ######### Load Config ##################################################
    try:
        log("Config: Loading ", config_path)
        if config_path.endswith(".yaml"):
            cfg = yaml.safe_load(config_path.read_text())
            dd = {}
            for x in cfg:  ### Map to dict
                for key, val in x.items():
                    dd[key] = val
            return cfg

        elif config_path.endswith(".json"):
            cfg = json.loads(config_path.read_text())

        elif config_path.endswith(".properties") or config_path.endswith(".ini"):
            from configparser import SafeConfigParser

            cfg = SafeConfigParser()
            cfg.read(str(config_path))

        elif config_path.endswith(".toml"):
            import toml

            cfg = toml.loads(config_path.read_text())

        else:
            raise Exception(f"not supported file {config_path}")

        if to_dataclass:  ### myconfig.val  , myconfig.val2
            return Box(cfg)
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


def dict_to_yamale(cfg_dict: dict = None):
    """
    from . import readers
    raw_data = readers.parse_yaml(path, parser, content=content)
    if len(raw_data) == 0:
        return [({}, path)]
    return [(d, path) for d in raw_data]
    """
    return [(cfg_dict, "")]


def config_isvalid(config_dict: dict, schema_path: str, silent: bool = False) -> bool:
    """Validate using a  yaml file
    Args:
        config_dict:
        schema_path:
        silent:
    Returns: True/False
    """

    schema = yamale.make_schema(schema_path)
    # data = yamale.make_data(config_path)
    data = dict_to_yamale(config_dict)

    try:
        yamale.validate(schema, data)
        return True

    except yamale.YamaleError as e:
        for result in e.results:
            loge(f"Error validating data '{result.data}' with '{result.schema}'\n\t")
            for error in result.errors:
                loge(f"\t{error}")

        return False


def config_validate(
    config_path: str, schema_path: str, silent: bool = False
) -> Union[Box, None]:

    schema = yamale.make_schema(schema_path)
    data = yamale.make_data(config_path)

    try:
        yamale.validate(schema, data)
        return _yaml_to_box(config_path)

    except yamale.YamaleError as e:
        print("Validation failed!\n")
        for result in e.results:
            print(f"Error validating data '{result.data}' with '{result.schema}'\n\t")
            for error in result.errors:
                print(f"\t{error}")
        if not silent:
            raise e


def config_validate_pydantic(
    config_dict: dict = None,
    pydantic_file_path: str = "config.validate.myclassname.py",
):
    # config_validate_path:=None,):
    """Validate configuration based on template type validator
        wiht Pydantic

    Returns: dict config
    """
    import json, yaml, pathlib


def _yaml_to_box(yaml_path: str) -> Box:
    with open(yaml_path) as f:
        data = yaml.load(f)

    return Box(data)


#########################################################################################################
def test():
    config_validate("actual_data.yaml", "template.yaml", silent=True)


def test2():
    cfg_dict = config_load("config.yaml")
    isok = config_isvalid(cfg_dict, "config_val.yaml")
    log(isok)




def test_example():
    ss = """
string: ok
regex:  abcd
number: 6.7
integer: 3
boolean: True
list: [1,2,3]
enum: 'one'
map:
null:
date:
nest:
    integer: 7
    nest:
        string: "ok"

    """
    return ss




if __name__ == "__main__":
    fire.Fire()
