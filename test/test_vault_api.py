# coding: utf-8

"""
    OmniCore Model and State Management API

    This is an OmniCore Model and State Management server.  # noqa: E501

    The version of the OpenAPI document: 1.8.9
    Contact: omnicoresupport@korewireless.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import OmniCore
from OmniCore.api.vault_api import VaultApi  # noqa: E501
from OmniCore.rest import ApiException


class TestVaultApi(unittest.TestCase):
    """VaultApi unit test stubs"""

    def setUp(self):
        self.api = OmniCore.api.vault_api.VaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_vault_configuration(self):
        """Test case for create_vault_configuration

        """
        pass

    def test_create_vault_key(self):
        """Test case for create_vault_key

        """
        pass

    def test_delete_configuration(self):
        """Test case for delete_configuration

        """
        pass

    def test_delete_vault_key(self):
        """Test case for delete_vault_key

        """
        pass

    def test_enable_encryption(self):
        """Test case for enable_encryption

        """
        pass

    def test_get_exports(self):
        """Test case for get_exports

        """
        pass

    def test_get_registry_data(self):
        """Test case for get_registry_data

        """
        pass

    def test_get_replays(self):
        """Test case for get_replays

        """
        pass

    def test_get_vault_audit(self):
        """Test case for get_vault_audit

        """
        pass

    def test_get_vault_configurations(self):
        """Test case for get_vault_configurations

        """
        pass

    def test_get_vault_files(self):
        """Test case for get_vault_files

        """
        pass

    def test_get_vault_keys(self):
        """Test case for get_vault_keys

        """
        pass

    def test_get_vault_metrics(self):
        """Test case for get_vault_metrics

        """
        pass

    def test_get_vault_status(self):
        """Test case for get_vault_status

        """
        pass

    def test_set_retention(self):
        """Test case for set_retention

        """
        pass

    def test_start_export(self):
        """Test case for start_export

        """
        pass

    def test_start_replay(self):
        """Test case for start_replay

        """
        pass


if __name__ == '__main__':
    unittest.main()
