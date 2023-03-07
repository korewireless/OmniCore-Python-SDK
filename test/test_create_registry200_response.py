# coding: utf-8

"""
    OmniCore Model and State Management API

    This is an OmniCore Model and State Management server.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@korewireless.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import OmniCore
from OmniCore.models.create_registry200_response import CreateRegistry200Response  # noqa: E501
from OmniCore.rest import ApiException

class TestCreateRegistry200Response(unittest.TestCase):
    """CreateRegistry200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateRegistry200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateRegistry200Response`
        """
        model = OmniCore.models.create_registry200_response.CreateRegistry200Response()  # noqa: E501
        if include_optional :
            return CreateRegistry200Response(
                id = '012', 
                name = '', 
                parent = '', 
                created_on = '', 
                updated_on = '', 
                credentials = [
                    OmniCore.models.registry_credential.RegistryCredential(
                        public_key_certificate = OmniCore.models.public_key_certificate.PublicKeyCertificate(
                            certificate = '', 
                            format = 'X509_CERTIFICATE_PEM', 
                            x509_details = OmniCore.models.x509_certificate_details.X509CertificateDetails(
                                expiry_time = '', 
                                issuer = '', 
                                public_key_type = '', 
                                signature_algorithm = '', 
                                start_time = '', 
                                subject = '', ), ), )
                    ], 
                http_config = OmniCore.models.http_config.HttpConfig(
                    http_enabled_state = 'HTTP_ENABLED', ), 
                mqtt_config = OmniCore.models.mqtt_config.MqttConfig(
                    mqtt_enabled_state = 'MQTT_ENABLED', ), 
                log_level = 'INFO', 
                event_notification_configs = [
                    OmniCore.models.event_notification_config.EventNotificationConfig(
                        pubsub_topic_name = '', 
                        subfolder_matches = '', )
                    ], 
                log_notification_config = OmniCore.models.notification_config.NotificationConfig(
                    pubsub_topic_name = '', ), 
                state_notification_config = OmniCore.models.notification_config.NotificationConfig(
                    pubsub_topic_name = '', ), 
                number_of_devices = 56, 
                number_of_gateways = 56
            )
        else :
            return CreateRegistry200Response(
                id = '012',
                parent = '',
        )
        """

    def testCreateRegistry200Response(self):
        """Test CreateRegistry200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
