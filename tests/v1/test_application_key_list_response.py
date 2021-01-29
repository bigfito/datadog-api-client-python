# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1

try:
    from datadog_api_client.v1.model import application_key
except ImportError:
    application_key = sys.modules["datadog_api_client.v1.model.application_key"]
from datadog_api_client.v1.model.application_key_list_response import ApplicationKeyListResponse


class TestApplicationKeyListResponse(unittest.TestCase):
    """ApplicationKeyListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApplicationKeyListResponse(self):
        """Test ApplicationKeyListResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ApplicationKeyListResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
