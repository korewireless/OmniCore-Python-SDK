# coding: utf-8

"""
    OmniCore Model and State Management API

    This is an OmniCore Model and State Management server.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@korewireless.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import OmniCore
from OmniCore.api.registry_api import RegistryApi  # noqa: E501
from OmniCore.rest import ApiException


class TestRegistryApi(unittest.TestCase):
    """RegistryApi unit test stubs"""

    def setUp(self):
        self.api = OmniCore.api.registry_api.RegistryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_registry(self):
        """Test case for create_registry

        """
        pass

    def test_delete_registry(self):
        """Test case for delete_registry

        """
        pass

    def test_get_registries(self):
        """Test case for get_registries

        """
        pass

    def test_get_registry(self):
        """Test case for get_registry

        """
        pass

    def test_update_registry(self):
        """Test case for update_registry

        """
        pass


if __name__ == '__main__':
    unittest.main()
