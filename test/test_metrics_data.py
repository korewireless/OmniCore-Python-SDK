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
from OmniCore.models.metrics_data import MetricsData  # noqa: E501
from OmniCore.rest import ApiException

class TestMetricsData(unittest.TestCase):
    """MetricsData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MetricsData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MetricsData`
        """
        model = OmniCore.models.metrics_data.MetricsData()  # noqa: E501
        if include_optional :
            return MetricsData(
                data = [
                    OmniCore.models.metrics_logs.MetricsLogs(
                        no_of_files = 56, 
                        file_size = 1.337, 
                        noofoperations = 56, 
                        updatedon = '', 
                        replay_file_size = 1.337, 
                        export_file_size = 1.337, )
                    ], 
                total_export_size = 1.337, 
                total_replay_size = 1.337
            )
        else :
            return MetricsData(
        )
        """

    def testMetricsData(self):
        """Test MetricsData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
