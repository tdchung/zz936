import datetime

import pytest
from box import Box
from yamale import YamaleError

from zz936.configs.util_config import validate_yaml_config


def test_validate_yaml_types():
    yaml = "fixtures/types_good_data.yaml"
    schema = "fixtures/types.yaml"
    result = validate_yaml_config(yaml, schema)

    assert isinstance(result, Box)
    assert result == {
        None: None,
        "boolean": True,
        "date": datetime.date(2015, 1, 1),
        "enum": 1,
        "integer": 2,
        "list": ["hi"],
        "map": {"hello": 1, "another": "hi"},
        "nest": {"integer": 1, "nest": {"string": "nested"}},
        "number": 13.12,
        "regex": "abcde",
        "string": "hello",
    }


def test_validate_yaml_types_failed():
    yaml = "fixtures/types_bad_data.yaml"
    schema = "fixtures/types.yaml"

    expected = [
        "string: '1' is not a str.",
        "regex: 'edcba' is not a regex match.",
        "number: 14 is greater than 13.12",
        "integer: '1.4' is not a int.",
        "boolean: '0' is not a bool.",
        "list: 'list?' is not a list.",
        "enum: 'False' not in ('one', True, 1)",
        "map: 'hello' is not a map.",
        "None: 'null' is not a null.",
    ]

    with pytest.raises(YamaleError) as exc:
        validate_yaml_config(yaml, schema)
    actual = exc.value.results[0].errors
    assert sorted(actual) == sorted(expected)


def test_validate_yaml_failed_silent():
    yaml = "fixtures/types_bad_data.yaml"
    schema = "fixtures/types.yaml"
    result = validate_yaml_config(yaml, schema, silent=True)
    assert result is None


def test_validate_yaml_syntax_error():
    yaml = "fixtures/types_bad_data.yaml"
    schema = "fixtures/bad_schema.yaml"
    with pytest.raises(SyntaxError) as exc:
        validate_yaml_config(yaml, schema)
    assert "Invalid schema expression: 'enum('one, True, 1)'" in exc.value.msg
