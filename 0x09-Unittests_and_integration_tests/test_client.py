#!/usr/bin/env python3
"""Unit tests for client module
"""
import unittest
from unittest import mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Testing GithubOrgClient class
    """
    @parameterized.expand([
        ("facebook", {"payload": True}),
        ("twitter", {"payload": True}),
        ("invalid", {"payload": False})
    ])
    @mock.patch("utils.requests.get")
    def test_org(self, url, payload, mock_get_json):
        """Testing GithubOrgClient class
        """
        mock_get_json.return_value.ok = payload.get("payload")
        mock_get_json.return_value.json.return_value = payload
        g_client = GithubOrgClient(url)
        res = g_client.org
        self.assertEqual(res, payload)
        mock_get_json.assert_called_once()


if __name__ == '__main__':
    unittest.main()
