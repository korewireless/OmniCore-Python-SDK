# coding: utf-8

"""
    OmniCore Model and State Management API

    This is an OmniCore Model and State Management server.  # noqa: E501

    The version of the OpenAPI document: 1.8.11
    Contact: omnicoresupport@korewireless.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import OmniCore
from OmniCore.models.device_state import DeviceState  # noqa: E501
from OmniCore.rest import ApiException

class TestDeviceState(unittest.TestCase):
    """DeviceState unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DeviceState
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceState`
        """
        model = OmniCore.models.device_state.DeviceState()  # noqa: E501
        if include_optional :
            return DeviceState(
                binary_data = '', 
                update_time = ''
            )
        else :
            return DeviceState(
        )
        """

    def testDeviceState(self):
        """Test DeviceState"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
