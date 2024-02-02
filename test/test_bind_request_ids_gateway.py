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
import datetime

import OmniCore
from OmniCore.models.bind_request_ids_gateway import BindRequestIdsGateway  # noqa: E501
from OmniCore.rest import ApiException

class TestBindRequestIdsGateway(unittest.TestCase):
    """BindRequestIdsGateway unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BindRequestIdsGateway
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BindRequestIdsGateway`
        """
        model = OmniCore.models.bind_request_ids_gateway.BindRequestIdsGateway()  # noqa: E501
        if include_optional :
            return BindRequestIdsGateway(
                device_ids = [
                    ''
                    ], 
                gateway_id = ''
            )
        else :
            return BindRequestIdsGateway(
                device_ids = [
                    ''
                    ],
                gateway_id = '',
        )
        """

    def testBindRequestIdsGateway(self):
        """Test BindRequestIdsGateway"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
