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
    from datadog_api_client.v1.model.log_stream_widget_definition_type import LogStreamWidgetDefinitionType
    from datadog_api_client.v1.model.widget_field_sort import WidgetFieldSort
    from datadog_api_client.v1.model.widget_message_display import WidgetMessageDisplay
    from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1.model.widget_time import WidgetTime

    globals()["LogStreamWidgetDefinitionType"] = LogStreamWidgetDefinitionType
    globals()["WidgetFieldSort"] = WidgetFieldSort
    globals()["WidgetMessageDisplay"] = WidgetMessageDisplay
    globals()["WidgetTextAlign"] = WidgetTextAlign
    globals()["WidgetTime"] = WidgetTime


class LogStreamWidgetDefinition(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "columns": ([str],),
            "indexes": ([str],),
            "logset": (str,),
            "message_display": (WidgetMessageDisplay,),
            "query": (str,),
            "show_date_column": (bool,),
            "show_message_column": (bool,),
            "sort": (WidgetFieldSort,),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (LogStreamWidgetDefinitionType,),
        }

    attribute_map = {
        "type": "type",
        "columns": "columns",
        "indexes": "indexes",
        "logset": "logset",
        "message_display": "message_display",
        "query": "query",
        "show_date_column": "show_date_column",
        "show_message_column": "show_message_column",
        "sort": "sort",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
    }

    read_only_vars = {}

    def __init__(self, type, *args, **kwargs):
        """LogStreamWidgetDefinition - a model defined in OpenAPI

        Args:
            type (LogStreamWidgetDefinitionType):

        Keyword Args:
            columns ([str]): [optional] Which columns to display on the widget.
            indexes ([str]): [optional] An array of index names to query in the stream. Use [] to query all indexes at once.
            logset (str): [optional] ID of the log set to use.
            message_display (WidgetMessageDisplay): [optional]
            query (str): [optional] Query to filter the log stream with.
            show_date_column (bool): [optional] Whether to show the date column or not
            show_message_column (bool): [optional] Whether to show the message column or not
            sort (WidgetFieldSort): [optional]
            time (WidgetTime): [optional]
            title (str): [optional] Title of the widget.
            title_align (WidgetTextAlign): [optional]
            title_size (str): [optional] Size of the title.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.type = type

    @classmethod
    def _from_openapi_data(cls, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogStreamWidgetDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.type = type
        return self
