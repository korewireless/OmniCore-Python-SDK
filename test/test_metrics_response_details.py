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
from OmniCore.models.metrics_response_details import MetricsResponseDetails  # noqa: E501
from OmniCore.rest import ApiException

class TestMetricsResponseDetails(unittest.TestCase):
    """MetricsResponseDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MetricsResponseDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MetricsResponseDetails`
        """
        model = OmniCore.models.metrics_response_details.MetricsResponseDetails()  # noqa: E501
        if include_optional :
            return MetricsResponseDetails(
                subscription_id = '', 
                no_of_files = 56, 
                file_size = 1.337, 
                noofoperations = 56, 
                no_of_replays = 56, 
                no_of_exports = 56, 
                operations = [
                    OmniCore.models.operation_metrics.OperationMetrics(
                        no_of_files = 56, 
                        file_size = 1.337, 
                        operation = '', 
                        noofoperations = 56, 
                        updatedon = '', 
                        registryid = '', )
                    ], 
                details_for_time_period = OmniCore.models.metrics_data.MetricsData(
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
                    total_replay_size = 1.337, )
            )
        else :
            return MetricsResponseDetails(
        )
        """

    def testMetricsResponseDetails(self):
        """Test MetricsResponseDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
