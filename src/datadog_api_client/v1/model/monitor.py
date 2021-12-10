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
    from datadog_api_client.v1.model.creator import Creator
    from datadog_api_client.v1.model.monitor_options import MonitorOptions
    from datadog_api_client.v1.model.monitor_overall_states import MonitorOverallStates
    from datadog_api_client.v1.model.monitor_state import MonitorState
    from datadog_api_client.v1.model.monitor_type import MonitorType

    globals()["Creator"] = Creator
    globals()["MonitorOptions"] = MonitorOptions
    globals()["MonitorOverallStates"] = MonitorOverallStates
    globals()["MonitorState"] = MonitorState
    globals()["MonitorType"] = MonitorType


class Monitor(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {
        "priority": {
            "inclusive_maximum": 5,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "created": (datetime,),
            "creator": (Creator,),
            "deleted": (
                datetime,
                none_type,
            ),
            "id": (int,),
            "message": (str,),
            "modified": (datetime,),
            "multi": (bool,),
            "name": (str,),
            "options": (MonitorOptions,),
            "overall_state": (MonitorOverallStates,),
            "priority": (
                int,
                none_type,
            ),
            "query": (str,),
            "restricted_roles": (
                [str],
                none_type,
            ),
            "state": (MonitorState,),
            "tags": ([str],),
            "type": (MonitorType,),
        }

    attribute_map = {
        "query": "query",
        "type": "type",
        "created": "created",
        "creator": "creator",
        "deleted": "deleted",
        "id": "id",
        "message": "message",
        "modified": "modified",
        "multi": "multi",
        "name": "name",
        "options": "options",
        "overall_state": "overall_state",
        "priority": "priority",
        "restricted_roles": "restricted_roles",
        "state": "state",
        "tags": "tags",
    }

    read_only_vars = {
        "created",
        "deleted",
        "id",
        "modified",
        "multi",
    }

    def __init__(self, query, type, *args, **kwargs):
        """Monitor - a model defined in OpenAPI

        Args:
            query (str): The monitor query.
            type (MonitorType):

        Keyword Args:
            created (datetime): [optional] Timestamp of the monitor creation.
            creator (Creator): [optional]
            deleted (datetime, none_type): [optional] Whether or not the monitor is deleted. (Always `null`)
            id (int): [optional] ID of this monitor.
            message (str): [optional] A message to include with notifications for this monitor.
            modified (datetime): [optional] Last timestamp when the monitor was edited.
            multi (bool): [optional] Whether or not the monitor is broken down on different groups.
            name (str): [optional] The monitor name.
            options (MonitorOptions): [optional]
            overall_state (MonitorOverallStates): [optional]
            priority (int, none_type): [optional] Integer from 1 (high) to 5 (low) indicating alert severity.
            restricted_roles ([str], none_type): [optional] A list of role identifiers that can be pulled from the Roles API. Cannot be used with `locked` option.
            state (MonitorState): [optional]
            tags ([str]): [optional] Tags associated to your monitor.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.query = query
        self.type = type

    @classmethod
    def _from_openapi_data(cls, query, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(Monitor, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.query = query
        self.type = type
        return self
