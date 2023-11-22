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
from OmniCore.models.sink import Sink  # noqa: E501
from OmniCore.rest import ApiException

class TestSink(unittest.TestCase):
    """Sink unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Sink
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Sink`
        """
        model = OmniCore.models.sink.Sink()  # noqa: E501
        if include_optional :
            return Sink(
                id = '', 
                subscription = '', 
                sink = 'pubsub', 
                config = OmniCore.models.config.Config(
                    connection_parameter = '', ), 
                status = True, 
                createdon = '', 
                updatedon = ''
            )
        else :
            return Sink(
        )
        """

    def testSink(self):
        """Test Sink"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
