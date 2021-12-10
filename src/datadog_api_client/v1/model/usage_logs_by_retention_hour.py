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


class UsageLogsByRetentionHour(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "indexed_events_count": (int,),
            "live_indexed_events_count": (int,),
            "rehydrated_indexed_events_count": (int,),
            "retention": (str,),
        }

    attribute_map = {
        "indexed_events_count": "indexed_events_count",
        "live_indexed_events_count": "live_indexed_events_count",
        "rehydrated_indexed_events_count": "rehydrated_indexed_events_count",
        "retention": "retention",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """UsageLogsByRetentionHour - a model defined in OpenAPI

        Keyword Args:
            indexed_events_count (int): [optional] Total logs indexed with this retention period during a given hour.
            live_indexed_events_count (int): [optional] Live logs indexed with this retention period during a given hour.
            rehydrated_indexed_events_count (int): [optional] Rehydrated logs indexed with this retention period during a given hour.
            retention (str): [optional] The retention period in days or \"custom\" for all custom retention usage.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageLogsByRetentionHour, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
