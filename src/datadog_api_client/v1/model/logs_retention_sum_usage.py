# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    date,
    datetime,
    file_type,
    none_type,
)


class LogsRetentionSumUsage(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "logs_indexed_logs_usage_sum": (int,),
            "logs_live_indexed_logs_usage_sum": (int,),
            "logs_rehydrated_indexed_logs_usage_sum": (int,),
            "retention": (str,),
        }

    attribute_map = {
        "logs_indexed_logs_usage_sum": "logs_indexed_logs_usage_sum",
        "logs_live_indexed_logs_usage_sum": "logs_live_indexed_logs_usage_sum",
        "logs_rehydrated_indexed_logs_usage_sum": "logs_rehydrated_indexed_logs_usage_sum",
        "retention": "retention",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """LogsRetentionSumUsage - a model defined in OpenAPI

        Keyword Args:
            logs_indexed_logs_usage_sum (int): [optional] Total indexed logs for this retention period.
            logs_live_indexed_logs_usage_sum (int): [optional] Live indexed logs for this retention period.
            logs_rehydrated_indexed_logs_usage_sum (int): [optional] Rehydrated indexed logs for this retention period.
            retention (str): [optional] The retention period in days or \"custom\" for all custom retention periods.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsRetentionSumUsage, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
