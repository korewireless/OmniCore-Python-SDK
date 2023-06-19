# coding: utf-8

"""
    OmniCore Model and State Management API

    This is an OmniCore Model and State Management server.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: omnicoresupport@korewireless.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import OmniCore
from OmniCore.models.list_sinks_sinks_inner import ListSinksSinksInner  # noqa: E501
from OmniCore.rest import ApiException

class TestListSinksSinksInner(unittest.TestCase):
    """ListSinksSinksInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListSinksSinksInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListSinksSinksInner`
        """
        model = OmniCore.models.list_sinks_sinks_inner.ListSinksSinksInner()  # noqa: E501
        if include_optional :
            return ListSinksSinksInner(
                id = '', 
                subscription = '', 
                sink = 'pubsub', 
                config = OmniCore.models.list_sinks_sinks_inner_config.ListSinks_sinks_inner_config(
                    connection_parameter = '', ), 
                status = True, 
                createdon = '', 
                updatedon = ''
            )
        else :
            return ListSinksSinksInner(
        )
        """

    def testListSinksSinksInner(self):
        """Test ListSinksSinksInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
