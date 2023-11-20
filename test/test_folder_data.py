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
from OmniCore.models.folder_data import FolderData  # noqa: E501
from OmniCore.rest import ApiException

class TestFolderData(unittest.TestCase):
    """FolderData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FolderData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FolderData`
        """
        model = OmniCore.models.folder_data.FolderData()  # noqa: E501
        if include_optional :
            return FolderData(
                details = [
                    OmniCore.models.folder.Folder(
                        no_of_files = 56, 
                        file_size = 1.337, 
                        noofoperations = 56, 
                        updatedon = '', 
                        registryid = '', )
                    ]
            )
        else :
            return FolderData(
        )
        """

    def testFolderData(self):
        """Test FolderData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()