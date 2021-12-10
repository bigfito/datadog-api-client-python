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


def lazy_import():
    from datadog_api_client.v1.model.monitor_overall_states import MonitorOverallStates

    globals()["MonitorOverallStates"] = MonitorOverallStates


class MonitorGroupSearchResult(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "group": (str,),
            "group_tags": ([str],),
            "last_nodata_ts": (int,),
            "last_triggered_ts": (
                int,
                none_type,
            ),
            "monitor_id": (int,),
            "monitor_name": (str,),
            "status": (MonitorOverallStates,),
        }

    attribute_map = {
        "group": "group",
        "group_tags": "group_tags",
        "last_nodata_ts": "last_nodata_ts",
        "last_triggered_ts": "last_triggered_ts",
        "monitor_id": "monitor_id",
        "monitor_name": "monitor_name",
        "status": "status",
    }

    read_only_vars = {
        "group",
        "group_tags",
        "last_nodata_ts",
        "last_triggered_ts",
        "monitor_id",
        "monitor_name",
    }

    def __init__(self, *args, **kwargs):
        """MonitorGroupSearchResult - a model defined in OpenAPI

        Keyword Args:
            group (str): [optional] The name of the group.
            group_tags ([str]): [optional] The list of tags of the monitor group.
            last_nodata_ts (int): [optional] Latest timestamp the monitor group was in NO_DATA state.
            last_triggered_ts (int, none_type): [optional] Latest timestamp the monitor group triggered.
            monitor_id (int): [optional] The ID of the monitor.
            monitor_name (str): [optional] The name of the monitor.
            status (MonitorOverallStates): [optional]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MonitorGroupSearchResult, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
