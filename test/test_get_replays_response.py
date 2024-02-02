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
from OmniCore.models.get_replays_response import GetReplaysResponse  # noqa: E501
from OmniCore.rest import ApiException

class TestGetReplaysResponse(unittest.TestCase):
    """GetReplaysResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetReplaysResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetReplaysResponse`
        """
        model = OmniCore.models.get_replays_response.GetReplaysResponse()  # noqa: E501
        if include_optional :
            return GetReplaysResponse(
                details = [
                    OmniCore.models.replay.Replay(
                        id = 56, 
                        registry = '', 
                        start_time = 56, 
                        end_time = 56, 
                        subscription = '', 
                        destination = '', 
                        source = '', 
                        status = '', 
                        size = 56, 
                        count = 56, )
                    ]
            )
        else :
            return GetReplaysResponse(
        )
        """

    def testGetReplaysResponse(self):
        """Test GetReplaysResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
