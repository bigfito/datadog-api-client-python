# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v2

try:
    from datadog_api_client.v2.model import logs_aggregate_bucket_value_timeseries
except ImportError:
    logs_aggregate_bucket_value_timeseries = sys.modules[
        "datadog_api_client.v2.model.logs_aggregate_bucket_value_timeseries"
    ]
from datadog_api_client.v2.model.logs_aggregate_bucket_value import LogsAggregateBucketValue


class TestLogsAggregateBucketValue(unittest.TestCase):
    """LogsAggregateBucketValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsAggregateBucketValue(self):
        """Test LogsAggregateBucketValue"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsAggregateBucketValue()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
