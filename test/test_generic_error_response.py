# coding: utf-8

"""
    OmniCore Model and State Management API

    This is an OmniCore Model and State Management server.  # noqa: E501

    The version of the OpenAPI document: 1.8.5
    Contact: omnicoresupport@korewireless.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import OmniCore
from OmniCore.models.generic_error_response import GenericErrorResponse  # noqa: E501
from OmniCore.rest import ApiException

class TestGenericErrorResponse(unittest.TestCase):
    """GenericErrorResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GenericErrorResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GenericErrorResponse`
        """
        model = OmniCore.models.generic_error_response.GenericErrorResponse()  # noqa: E501
        if include_optional :
            return GenericErrorResponse(
                error = OmniCore.models.error_frame.ErrorFrame(
                    code = 56, 
                    details = '', 
                    message = '', 
                    status = '', )
            )
        else :
            return GenericErrorResponse(
                error = OmniCore.models.error_frame.ErrorFrame(
                    code = 56, 
                    details = '', 
                    message = '', 
                    status = '', ),
        )
        """

    def testGenericErrorResponse(self):
        """Test GenericErrorResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
