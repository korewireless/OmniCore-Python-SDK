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
from OmniCore.models.device import Device  # noqa: E501
from OmniCore.rest import ApiException

class TestDevice(unittest.TestCase):
    """Device unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Device
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Device`
        """
        model = OmniCore.models.device.Device()  # noqa: E501
        if include_optional :
            return Device(
                id = '012', 
                name = '', 
                num_id = '', 
                parent = '', 
                registry = '', 
                blocked = True, 
                capresent = True, 
                subscription = '', 
                created_on = '', 
                updated_on = '', 
                credentials = [
                    OmniCore.models.device_credential.DeviceCredential(
                        expiration_time = '', 
                        id = '', 
                        public_key = OmniCore.models.public_key_credential.PublicKeyCredential(
                            format = 'RSA_PEM', 
                            key = '', ), )
                    ], 
                gateway = [
                    ''
                    ], 
                gateway_config = OmniCore.models.gateway_config.GatewayConfig(
                    gateway_auth_method = 'GATEWAY_AUTH_METHOD_UNSPECIFIED', 
                    gateway_type = 'NON_GATEWAY', ), 
                is_gateway = True, 
                device_errors = '', 
                client_online = True, 
                last_config_ack_time = '', 
                last_config_send_time = '', 
                last_error_status = OmniCore.models.error_status.ErrorStatus(
                    code = 56, 
                    details = '', 
                    message = '', ), 
                last_error_time = '', 
                last_event_time = '', 
                last_heartbeat_time = '', 
                last_state_time = '', 
                log_level = 'INFO', 
                metadata = {
                    'key' : ''
                    }, 
                config = OmniCore.models.device_config.DeviceConfig(
                    acknowledged = True, 
                    binary_data = '', 
                    cloud_update_time = '', 
                    device_ack_time = '', 
                    version = 56, ), 
                state = OmniCore.models.device_state.DeviceState(
                    binary_data = '', 
                    update_time = '', ), 
                policy = OmniCore.models.policy.policy(
                    connect = True, 
                    publish_state = True, 
                    publish_events = True, 
                    publish_events_regex = '', 
                    publish_loopback = True, 
                    subscribe_command = True, 
                    subscribe_command_regex = '', 
                    subscribe_broadcast = True, 
                    subscribe_broadcast_regex = '', 
                    subscribe_config = True, )
            )
        else :
            return Device(
                id = '012',
        )
        """

    def testDevice(self):
        """Test Device"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
