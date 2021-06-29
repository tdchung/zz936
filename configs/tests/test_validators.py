import datetime
import os

from box import Box
from yamale import YamaleTestCase, YamaleError

from zz936.configs.util_config import validate_yaml_config


class TestYaml(YamaleTestCase):
    base_dir = os.path.dirname(os.path.realpath(__file__))
    schema = "fixtures/simple.yaml"
    yaml = "fixtures/simple_good_data.yaml"

    def test_validate_yaml(self):
        result = validate_yaml_config(self.yaml, self.schema)
        self.assertIsInstance(result, Box)
        self.assertEqual(
            result, {"name": "Bill", "age": 26, "height": 6.2, "awesome": True}
        )

    def test_validate_yaml_failed(self):
        self.yaml = "fixtures/simple_bad_data.yaml"
        with self.assertRaises(YamaleError) as exc:
            validate_yaml_config(self.yaml, self.schema)
        self.assertEqual(
            exc.exception.results[0].errors[0],
            "age: 'this should be int' is not a int.",
        )

    def test_validate_yaml_failed_silent(self):
        self.yaml = "fixtures/simple_bad_data.yaml"
        result = validate_yaml_config(self.yaml, self.schema, silent=True)
        self.assertIsNone(result)

    def test_validate_yaml_syntax_error(self):
        self.schema = "fixtures/bad_schema.yaml"
        with self.assertRaises(SyntaxError) as exc:
            validate_yaml_config(self.yaml, self.schema)
        self.assertIn(
            "Invalid schema expression: 'enum('one, True, 1)'", exc.exception.msg
        )

    def test_validate_yaml_types(self):
        self.yaml = "fixtures/types_good_data.yaml"
        self.schema = "fixtures/types.yaml"
        result = validate_yaml_config(self.yaml, self.schema)
        self.assertIsInstance(result, Box)
        self.assertEqual(
            result,
            {
                "string": "hello",
                "regex": "abcde",
                "number": 12.1,
                "integer": 2,
                "boolean": True,
                "list": ["hi"],
                "enum": 1,
                "map": {"hello": 1, "another": "hi"},
                None: None,
            },
        )

    def test_validate_yaml_types_failed(self):
        self.yaml = "fixtures/types_bad_data.yaml"
        self.schema = "fixtures/types.yaml"

        expected = [
            "string: '1' is not a str.",
            "regex: 'edcba' is not a regex match.",
            "number: 'nan' is not a num.",
            "integer: '1.4' is not a int.",
            "boolean: '0' is not a bool.",
            "list: 'list?' is not a list.",
            "enum: 'False' not in ('one', True, 1)",
            "map: 'hello' is not a map.",
            "None: 'null' is not a null.",
        ]

        with self.assertRaises(YamaleError) as exc:
            validate_yaml_config(self.yaml, self.schema)
        actual = exc.exception.results[0].errors
        self.assertEqual(sorted(actual), sorted(expected))

    def test_validate_yaml_nested(self):
        self.yaml = "fixtures/nested_good_data.yaml"
        self.schema = "fixtures/nested.yaml"
        result = validate_yaml_config(self.yaml, self.schema)
        self.assertIsInstance(result, Box)
        self.assertEqual(
            result,
            {
                "boolean": True,
                "date": datetime.date(2015, 1, 1),
                "datetime": datetime.datetime(
                    2015,
                    1,
                    1,
                    0,
                    0,
                    tzinfo=datetime.timezone(datetime.timedelta(seconds=3600)),
                ),
                "integer": 3,
                "list": [
                    "yay",
                    True,
                    datetime.datetime(2015, 1, 1, 0, 0),
                    {"integer": 1, "string": "sup"},
                ],
                "nest": {
                    "integer": 1,
                    "nest": {
                        "date": datetime.date(2015, 2, 1),
                        "number": 4,
                        "string": "nested",
                    },
                },
                "number": 12,
                "string": "hello",
            },
        )

    def test_validate_yaml_nested_failed(self):
        self.yaml = "fixtures/nested_bad_data.yaml"
        self.schema = "fixtures/nested.yaml"

        expected = [
            "list.1: 'NOT A BOOL' is not a bool.",
            "list.2: '2015-01-01 00:00' is not a timestamp.",
        ]

        with self.assertRaises(YamaleError) as exc:
            validate_yaml_config(self.yaml, self.schema)
        actual = exc.exception.results[0].errors
        self.assertEqual(sorted(actual), sorted(expected))
