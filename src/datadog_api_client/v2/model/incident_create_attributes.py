# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (  # noqa: F401
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
    from datadog_api_client.v2.model.incident_field_attributes import IncidentFieldAttributes
    from datadog_api_client.v2.model.incident_notification_handle import IncidentNotificationHandle
    from datadog_api_client.v2.model.incident_timeline_cell_create_attributes import (
        IncidentTimelineCellCreateAttributes,
    )

    globals()["IncidentFieldAttributes"] = IncidentFieldAttributes
    globals()["IncidentNotificationHandle"] = IncidentNotificationHandle
    globals()["IncidentTimelineCellCreateAttributes"] = IncidentTimelineCellCreateAttributes


class IncidentCreateAttributes(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "customer_impacted": (bool,),
            "fields": ({str: (IncidentFieldAttributes,)},),
            "initial_cells": ([IncidentTimelineCellCreateAttributes],),
            "notification_handles": ([IncidentNotificationHandle],),
            "title": (str,),
        }

    attribute_map = {
        "customer_impacted": "customer_impacted",
        "title": "title",
        "fields": "fields",
        "initial_cells": "initial_cells",
        "notification_handles": "notification_handles",
    }

    read_only_vars = {}

    def __init__(self, customer_impacted, title, *args, **kwargs):
        """IncidentCreateAttributes - a model defined in OpenAPI

        Args:
            customer_impacted (bool): A flag indicating whether the incident caused customer impact.
            title (str): The title of the incident, which summarizes what happened.

        Keyword Args:
            fields ({str: (IncidentFieldAttributes,)}): [optional] A condensed view of the user-defined fields for which to create initial selections.
            initial_cells ([IncidentTimelineCellCreateAttributes]): [optional] An array of initial timeline cells to be placed at the beginning of the incident timeline.
            notification_handles ([IncidentNotificationHandle]): [optional] Notification handles that will be notified of the incident at creation.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.customer_impacted = customer_impacted
        self.title = title

    @classmethod
    def _from_openapi_data(cls, customer_impacted, title, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(IncidentCreateAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.customer_impacted = customer_impacted
        self.title = title
        return self
