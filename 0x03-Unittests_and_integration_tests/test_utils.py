#!/usr/bin/env python3
""" unit test """

import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """ test the utils module"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, mapp, pat, expected):
        """ test """
        self.assertEqual(access_nested_map(mapp, pat), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, m, p, expected):
        """test 2 """
        with self.assertRaises(KeyError):
            access_nested_map(m, p)


if __name__ == "__main__":
    unittest.main()
