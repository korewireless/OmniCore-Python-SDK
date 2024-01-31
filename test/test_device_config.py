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
import datetime

import OmniCore
from OmniCore.models.device_config import DeviceConfig  # noqa: E501
from OmniCore.rest import ApiException

class TestDeviceConfig(unittest.TestCase):
    """DeviceConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DeviceConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceConfig`
        """
        model = OmniCore.models.device_config.DeviceConfig()  # noqa: E501
        if include_optional :
            return DeviceConfig(
                acknowledged = True, 
                binary_data = '', 
                cloud_update_time = '', 
                device_ack_time = '', 
                version = 56
            )
        else :
            return DeviceConfig(
        )
        """

    def testDeviceConfig(self):
        """Test DeviceConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
