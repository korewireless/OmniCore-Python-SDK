# coding: utf-8

"""
    OmniCore Model and State Management API

    This is an OmniCore Model and State Management server.  # noqa: E501

    The version of the OpenAPI document: 1.8.10
    Contact: omnicoresupport@korewireless.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import OmniCore
from OmniCore.api.device_api import DeviceApi  # noqa: E501
from OmniCore.rest import ApiException


class TestDeviceApi(unittest.TestCase):
    """DeviceApi unit test stubs"""

    def setUp(self):
        self.api = OmniCore.api.device_api.DeviceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_bind_device(self):
        """Test case for bind_device

        """
        pass

    def test_bind_devices(self):
        """Test case for bind_devices

        """
        pass

    def test_block_device_communcation(self):
        """Test case for block_device_communcation

        """
        pass

    def test_create_device(self):
        """Test case for create_device

        """
        pass

    def test_delete_device(self):
        """Test case for delete_device

        """
        pass

    def test_get_config(self):
        """Test case for get_config

        """
        pass

    def test_get_device(self):
        """Test case for get_device

        """
        pass

    def test_get_devices(self):
        """Test case for get_devices

        """
        pass

    def test_get_states(self):
        """Test case for get_states

        """
        pass

    def test_get_subscription_devices(self):
        """Test case for get_subscription_devices

        """
        pass

    def test_send_command_to_device(self):
        """Test case for send_command_to_device

        """
        pass

    def test_un_bind_device(self):
        """Test case for un_bind_device

        """
        pass

    def test_un_bind_devices(self):
        """Test case for un_bind_devices

        """
        pass

    def test_update_configuration_to_device(self):
        """Test case for update_configuration_to_device

        """
        pass

    def test_update_custom_onboard_request(self):
        """Test case for update_custom_onboard_request

        """
        pass

    def test_update_device(self):
        """Test case for update_device

        """
        pass


if __name__ == '__main__':
    unittest.main()
