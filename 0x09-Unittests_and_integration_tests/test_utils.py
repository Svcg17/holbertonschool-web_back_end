import unittest
from parameterized import parameterized
from utils import access_nested_map
"""Unit tests for utils module
"""

class TestAccessNestedMap(unittest.TestCase):
    """ Tests for access nested map class
    """
    @parameterized.expand([
        ("len_1", ({"a": 1}, ("a",)), 1),
        ("len_2", (({"a": {"b": 2}}, ("a",))), {'b': 2}),
        ("access_nested", (({"a": {"b": 2}}, ("a", "b"))), 2)
    ])
    def test_access_nested_map(self, name, input, expected):
        """
        Testing for access_nested_map method
        """
        self.assertEqual(access_nested_map(*input), expected)