import os

from box import Box
from yamale import YamaleTestCase, YamaleError

from zz936.validators import validate_yaml_with_yamale


class TestYaml(YamaleTestCase):
    base_dir = os.path.dirname(os.path.realpath(__file__))
    schema = "test_data/schema.yaml"
    yaml = "test_data/data.yaml"

    def test_validate_yaml(self):
        result = validate_yaml_with_yamale(self.yaml, self.schema)
        self.assertIsInstance(result, Box)
        self.assertEqual(
            result, {"name": "Bill", "age": 26, "height": 6.2, "awesome": True}
        )

    def test_validate_yaml_failed(self):
        self.yaml = "test_data/invalid_data.yaml"
        with self.assertRaises(YamaleError) as exc:
            validate_yaml_with_yamale(self.yaml, self.schema)
            self.assertEqual(
                exc.results[0].errors[0], "age: 'this should be int' is not a int."
            )
