# coding: utf-8

"""
    OmniCore Model and State Management API

    This is an OmniCore Model and State Management server.  # noqa: E501

    The version of the OpenAPI document: 1.8.6
    Contact: omnicoresupport@korewireless.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import OmniCore
from OmniCore.api.metrics_api import MetricsApi  # noqa: E501
from OmniCore.rest import ApiException


class TestMetricsApi(unittest.TestCase):
    """MetricsApi unit test stubs"""

    def setUp(self):
        self.api = OmniCore.api.metrics_api.MetricsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_metrics(self):
        """Test case for get_metrics

        """
        pass


if __name__ == '__main__':
    unittest.main()
