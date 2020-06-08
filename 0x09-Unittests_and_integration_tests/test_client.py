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
        ("valid_org", ("facebook", {"payload": True})),
        ("valid_org_1", ("twitter", {"payload": True})),
        ("invalid_org", ("invalid", {"payload": False}))
    ])
    @mock.patch("utils.requests.get")
    def test_org(self, name, input, mock_get_json):
        """Testing GithubOrgClient class
        """
        mock_get_json.return_value.ok = input[1].get("payload")
        mock_get_json.return_value.json.return_value = input[1]
        g_client = GithubOrgClient(input[0])
        res = g_client.org
        self.assertEqual(res, input[1])
        mock_get_json.assert_called_once()
