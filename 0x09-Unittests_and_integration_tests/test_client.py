#!/usr/bin/env python3
"""Unit tests for client module
"""
import unittest
from unittest import mock
from unittest.mock import PropertyMock, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Testing GithubOrgClient class
    """
    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": True}),
    ])
    @mock.patch("client.get_json")
    def test_org(self, url, payload, mock_get_json):
        """Testing GithubOrgClient class
        """
        mock_get_json.return_value = payload
        g_client = GithubOrgClient(url)
        res = g_client.org
        self.assertEqual(res, payload)
        mock_get_json.assert_called_once()

    def test_public_repos_url(self):
        """Testing public_repos_url
        """
        with mock.patch.object(GithubOrgClient,
                               "org",
                               new_callable=PropertyMock) as mock_org:
            test_json = {"url": "facebook", "repos_url": "http://testurl.com"}
            mock_org.return_value = test_json
            g_client = GithubOrgClient(test_json.get("url"))
            res = g_client._public_repos_url
            mock_org.assert_called_once()
            self.assertEqual(res, test_json.get("repos_url"))


if __name__ == '__main__':
    unittest.main()
