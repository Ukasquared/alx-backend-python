#!/usr/bin/env python3
""" unit test """

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import Mock, patch


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


class TestGetJson(unittest.TestCase):
    """testing http request """

    @patch('requests.get')
    def test_get_json(self, mock_it):
        """ test an http request """
        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]

        for test_url, test_payload in test_cases:
            # Configure the mock to return the test_payload
            mock_it.return_value.json.return_value = test_payload

            # Call the function
            result = get_json(test_url)

            # Assert the mocked get method was called exactly once with the test_url
            mock_it.assert_called_once_with(test_url)

            # Assert that the output is equal to test_payload
            self.assertEqual(result, test_payload)

if __name__ == "__main__":
    unittest.main()
