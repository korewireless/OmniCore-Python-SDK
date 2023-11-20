# coding: utf-8

"""
    OmniCore Model and State Management API

    This is an OmniCore Model and State Management server.  # noqa: E501

    The version of the OpenAPI document: 1.8.3
    Contact: omnicoresupport@korewireless.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import OmniCore
from OmniCore.models.public_key_credential import PublicKeyCredential  # noqa: E501
from OmniCore.rest import ApiException

class TestPublicKeyCredential(unittest.TestCase):
    """PublicKeyCredential unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PublicKeyCredential
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PublicKeyCredential`
        """
        model = OmniCore.models.public_key_credential.PublicKeyCredential()  # noqa: E501
        if include_optional :
            return PublicKeyCredential(
                format = 'RSA_PEM', 
                key = ''
            )
        else :
            return PublicKeyCredential(
                format = 'RSA_PEM',
        )
        """

    def testPublicKeyCredential(self):
        """Test PublicKeyCredential"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
