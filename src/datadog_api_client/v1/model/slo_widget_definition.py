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
    from datadog_api_client.v1.model.slo_widget_definition_type import SLOWidgetDefinitionType
    from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1.model.widget_time_windows import WidgetTimeWindows
    from datadog_api_client.v1.model.widget_view_mode import WidgetViewMode

    globals()["SLOWidgetDefinitionType"] = SLOWidgetDefinitionType
    globals()["WidgetTextAlign"] = WidgetTextAlign
    globals()["WidgetTimeWindows"] = WidgetTimeWindows
    globals()["WidgetViewMode"] = WidgetViewMode


class SLOWidgetDefinition(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "global_time_target": (str,),
            "show_error_budget": (bool,),
            "slo_id": (str,),
            "time_windows": ([WidgetTimeWindows],),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (SLOWidgetDefinitionType,),
            "view_mode": (WidgetViewMode,),
            "view_type": (str,),
        }

    attribute_map = {
        "type": "type",
        "view_type": "view_type",
        "global_time_target": "global_time_target",
        "show_error_budget": "show_error_budget",
        "slo_id": "slo_id",
        "time_windows": "time_windows",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "view_mode": "view_mode",
    }

    read_only_vars = {}

    def __init__(self, type, *args, **kwargs):
        """SLOWidgetDefinition - a model defined in OpenAPI

        Args:
            type (SLOWidgetDefinitionType):

        Keyword Args:
            view_type (str): Type of view displayed by the widget. Defaults to "detail".
            global_time_target (str): [optional] Defined global time target.
            show_error_budget (bool): [optional] Defined error budget.
            slo_id (str): [optional] ID of the SLO displayed.
            time_windows ([WidgetTimeWindows]): [optional] Times being monitored.
            title (str): [optional] Title of the widget.
            title_align (WidgetTextAlign): [optional]
            title_size (str): [optional] Size of the title.
            view_mode (WidgetViewMode): [optional]
        """
        super().__init__(kwargs)

        view_type = kwargs.get("view_type", "detail")

        self._check_pos_args(args)

        self.type = type
        self.view_type = view_type

    @classmethod
    def _from_openapi_data(cls, type, *args, **kwargs):
        """Helper creating a new instance from a response."""
        view_type = kwargs.get("view_type", "detail")

        self = super(SLOWidgetDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.type = type
        self.view_type = view_type
        return self
