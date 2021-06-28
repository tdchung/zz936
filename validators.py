import inspect
import json
import pathlib
import subprocess

import yaml


def validate_yaml(yaml_path: str, template_path: str) -> None:
    data = _load_yaml_file(yaml_path)

    json_template_path = _yaml_to_json(template_path)
    _create_pydantic_models(json_template_path)

    _create_pydantic_instances()


def _load_yaml_file(file_path: str) -> dict:
    with open(file_path) as f:
        return yaml.load(f)


def _yaml_to_json(file_path: str) -> str:
    with open(file_path) as f:
        data = yaml.load(f)

    json_path = f"{file_path.split('.')[0]}.json"

    with open(json_path, "w") as f:
        json.dump(data, f, indent=2)

    return json_path


def _create_pydantic_models(json_file_path: str) -> None:

    path = pathlib.Path(__file__).parent.resolve()
    subprocess.call(
        f"json2models "
        f"-m Template {path / json_file_path} "
        f"-f pydantic "
        f"--max-strings-literals 0 "
        f" > {path / json_file_path.split('.')[0]}.py",
        shell=True,
    )


def _create_pydantic_instances(actual_data=1):
    import template

    for name, data in inspect.getmembers(template, inspect.isclass):
        pass


if __name__ == "__main__":
    validate_yaml("actual_data.yaml", "template.yaml")
