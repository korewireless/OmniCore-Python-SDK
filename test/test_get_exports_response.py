# coding: utf-8

"""
    OmniCore Model and State Management API

    This is an OmniCore Model and State Management server.  # noqa: E501

    The version of the OpenAPI document: 1.8.6
    Contact: omnicoresupport@korewireless.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import OmniCore
from OmniCore.models.get_exports_response import GetExportsResponse  # noqa: E501
from OmniCore.rest import ApiException

class TestGetExportsResponse(unittest.TestCase):
    """GetExportsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetExportsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetExportsResponse`
        """
        model = OmniCore.models.get_exports_response.GetExportsResponse()  # noqa: E501
        if include_optional :
            return GetExportsResponse(
                details = [
                    OmniCore.models.export_detail.ExportDetail(
                        subscription = '', 
                        name = '', 
                        source = '', 
                        status = '', 
                        destination = '', 
                        created_on = '', 
                        nooffiles = 56, 
                        file_size = 1.337, 
                        done = True, )
                    ]
            )
        else :
            return GetExportsResponse(
        )
        """

    def testGetExportsResponse(self):
        """Test GetExportsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
