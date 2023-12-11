# coding: utf-8

"""
    OmniCore Model and State Management API

    This is an OmniCore Model and State Management server.  # noqa: E501

    The version of the OpenAPI document: 1.8.7
    Contact: omnicoresupport@korewireless.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import OmniCore
from OmniCore.models.metrics_logs import MetricsLogs  # noqa: E501
from OmniCore.rest import ApiException

class TestMetricsLogs(unittest.TestCase):
    """MetricsLogs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MetricsLogs
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MetricsLogs`
        """
        model = OmniCore.models.metrics_logs.MetricsLogs()  # noqa: E501
        if include_optional :
            return MetricsLogs(
                no_of_files = 56, 
                file_size = 1.337, 
                noofoperations = 56, 
                updatedon = '', 
                replay_file_size = 1.337, 
                export_file_size = 1.337
            )
        else :
            return MetricsLogs(
        )
        """

    def testMetricsLogs(self):
        """Test MetricsLogs"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
