#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map
"""Unit tests for utils module
"""


class TestAccessNestedMap(unittest.TestCase):
    """ A class for testing access_nested_map method
    """
    @parameterized.expand([
        ("len_1", ({"a": 1}, ("a",)), 1),
        ("len_2", (({"a": {"b": 2}}, ("a",))), {'b': 2}),
        ("access_nested", (({"a": {"b": 2}}, ("a", "b"))), 2)
    ])
    def test_access_nested_map(self, name, input, expected):
        """Sucess testing for access_nested_map method
        """
        self.assertEqual(access_nested_map(*input), expected)

    @parameterized.expand([
        ("empty_map", ({}, ("a",)), "a"),
        ("non_existent_path", ({"a": 1}, ("a", "b")), "b")
    ])
    def test_access_nested_map_exception(self, name, input, error):
        """Testing failure of access_nested_map method
        """
        with self.assertRaises(KeyError):
            try:
                access_nested_map(*input)
            except KeyError as e:
                self.assertEqual(e.args[0], error)
                raise
