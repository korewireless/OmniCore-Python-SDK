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
from OmniCore.models.registry_credential import RegistryCredential  # noqa: E501
from OmniCore.rest import ApiException

class TestRegistryCredential(unittest.TestCase):
    """RegistryCredential unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RegistryCredential
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RegistryCredential`
        """
        model = OmniCore.models.registry_credential.RegistryCredential()  # noqa: E501
        if include_optional :
            return RegistryCredential(
                public_key_certificate = OmniCore.models.public_key_certificate.PublicKeyCertificate(
                    certificate = '', 
                    format = 'X509_CERTIFICATE_PEM', 
                    x509_details = OmniCore.models.x509_certificate_details.X509CertificateDetails(
                        expiry_time = '', 
                        issuer = '', 
                        public_key_type = '', 
                        signature_algorithm = '', 
                        start_time = '', 
                        subject = '', ), ), 
                id = ''
            )
        else :
            return RegistryCredential(
        )
        """

    def testRegistryCredential(self):
        """Test RegistryCredential"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
