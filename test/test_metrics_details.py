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
from OmniCore.models.metrics_details import MetricsDetails  # noqa: E501
from OmniCore.rest import ApiException

class TestMetricsDetails(unittest.TestCase):
    """MetricsDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MetricsDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MetricsDetails`
        """
        model = OmniCore.models.metrics_details.MetricsDetails()  # noqa: E501
        if include_optional :
            return MetricsDetails(
                no_of_messages_for30_minutes = [
                    None
                    ], 
                no_of_messages_for48_hours = [
                    None
                    ], 
                billable_bytes_received = 56, 
                billable_bytes_sent = 56, 
                billable_message_size = 56, 
                bytes_received = 56, 
                bytes_sent = 56, 
                message_size = 56, 
                no_of_ack_messages = 56, 
                no_of_command_messages = 56, 
                no_of_config_messages = 56, 
                no_of_device_connections_failed = 56, 
                no_of_devices = 56, 
                no_of_dis_connections = 56, 
                no_of_event_messages = 56, 
                no_of_gateway_connections_failed = 56, 
                no_of_gateways = 56, 
                no_of_loop_back_messages = 56, 
                no_of_messages = 56, 
                no_of_publish_errors = 56, 
                no_of_registries = 56, 
                no_of_state_messages = 56, 
                no_of_subscribe = 56, 
                no_of_successful_connections = 56, 
                no_of_un_subscribe = 56, 
                subscription_id = ''
            )
        else :
            return MetricsDetails(
        )
        """

    def testMetricsDetails(self):
        """Test MetricsDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
