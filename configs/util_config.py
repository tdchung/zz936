from typing import Union

import yamale
import yaml
from box import Box


def validate_yaml_config(
    yaml_path: str, schema_path: str, silent: bool = False
) -> Union[Box, None]:
    try:
        schema = yamale.make_schema(schema_path)
    except SyntaxError as e:
        print(f"Syntax Error: {e.msg}")
        raise e

    data = yamale.make_data(yaml_path)

    try:
        yamale.validate(schema, data)
        print("Validation success!")

        return _yaml_to_box(yaml_path)
    except yamale.YamaleError as e:
        print("Validation failed!\n")
        for result in e.results:
            print(
                "Error validating data '%s' with '%s'\n\t"
                % (result.data, result.schema)
            )
            for error in result.errors:
                print("\t%s" % error)
        if not silent:
            raise e


def _yaml_to_box(yaml_path: str) -> Box:
    with open(yaml_path) as f:
        data = yaml.load(f)

    return Box(data)


if __name__ == "__main__":
    validate_yaml_config("actual_data.yaml", "template.yaml", silent=True)
