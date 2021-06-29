from typing import Union

import yamale
import yaml
from box import Box


def validate_yaml_config(
    yaml_path: str, schema_path: str, silent: bool = False
) -> Union[Box, None]:
    schema = yamale.make_schema(schema_path)
    data = yamale.make_data(yaml_path)

    try:
        yamale.validate(schema, data)
        print("Validation success!")

        return _yaml_to_box(yaml_path)
    except yamale.YamaleError as e:
        print("Validation failed!\n")
        for result in e.results:
            print(f"Error validating data '{result.data}' with '{result.schema}'\n\t")
            for error in result.errors:
                print(f"\t{error}")
        if not silent:
            raise e


def _yaml_to_box(yaml_path: str) -> Box:
    with open(yaml_path) as f:
        data = yaml.load(f)

    return Box(data)


if __name__ == "__main__":
    validate_yaml_config("actual_data.yaml", "template.yaml", silent=True)
