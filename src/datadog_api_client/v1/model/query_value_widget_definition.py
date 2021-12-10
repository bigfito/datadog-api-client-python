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
    from datadog_api_client.v1.model.query_value_widget_definition_type import QueryValueWidgetDefinitionType
    from datadog_api_client.v1.model.query_value_widget_request import QueryValueWidgetRequest
    from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
    from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1.model.widget_time import WidgetTime

    globals()["QueryValueWidgetDefinitionType"] = QueryValueWidgetDefinitionType
    globals()["QueryValueWidgetRequest"] = QueryValueWidgetRequest
    globals()["WidgetCustomLink"] = WidgetCustomLink
    globals()["WidgetTextAlign"] = WidgetTextAlign
    globals()["WidgetTime"] = WidgetTime


class QueryValueWidgetDefinition(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {
        "requests": {
            "max_items": 1,
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "autoscale": (bool,),
            "custom_links": ([WidgetCustomLink],),
            "custom_unit": (str,),
            "precision": (int,),
            "requests": ([QueryValueWidgetRequest],),
            "text_align": (WidgetTextAlign,),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (QueryValueWidgetDefinitionType,),
        }

    attribute_map = {
        "requests": "requests",
        "type": "type",
        "autoscale": "autoscale",
        "custom_links": "custom_links",
        "custom_unit": "custom_unit",
        "precision": "precision",
        "text_align": "text_align",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
    }

    read_only_vars = {}

    def __init__(self, requests, type, *args, **kwargs):
        """QueryValueWidgetDefinition - a model defined in OpenAPI

        Args:
            requests ([QueryValueWidgetRequest]): Widget definition.
            type (QueryValueWidgetDefinitionType):

        Keyword Args:
            autoscale (bool): [optional] Whether to use auto-scaling or not.
            custom_links ([WidgetCustomLink]): [optional] List of custom links.
            custom_unit (str): [optional] Display a unit of your choice on the widget.
            precision (int): [optional] Number of decimals to show. If not defined, the widget uses the raw value.
            text_align (WidgetTextAlign): [optional]
            time (WidgetTime): [optional]
            title (str): [optional] Title of your widget.
            title_align (WidgetTextAlign): [optional]
            title_size (str): [optional] Size of the title.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.requests = requests
        self.type = type

    @classmethod
    def _from_openapi_data(cls, requests, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(QueryValueWidgetDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.requests = requests
        self.type = type
        return self
