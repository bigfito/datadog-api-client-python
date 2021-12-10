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
    from datadog_api_client.v1.model.widget_comparator import WidgetComparator
    from datadog_api_client.v1.model.widget_palette import WidgetPalette

    globals()["WidgetComparator"] = WidgetComparator
    globals()["WidgetPalette"] = WidgetPalette


class WidgetConditionalFormat(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "comparator": (WidgetComparator,),
            "custom_bg_color": (str,),
            "custom_fg_color": (str,),
            "hide_value": (bool,),
            "image_url": (str,),
            "metric": (str,),
            "palette": (WidgetPalette,),
            "timeframe": (str,),
            "value": (float,),
        }

    attribute_map = {
        "comparator": "comparator",
        "palette": "palette",
        "value": "value",
        "custom_bg_color": "custom_bg_color",
        "custom_fg_color": "custom_fg_color",
        "hide_value": "hide_value",
        "image_url": "image_url",
        "metric": "metric",
        "timeframe": "timeframe",
    }

    read_only_vars = {}

    def __init__(self, comparator, palette, value, *args, **kwargs):
        """WidgetConditionalFormat - a model defined in OpenAPI

        Args:
            comparator (WidgetComparator):
            palette (WidgetPalette):
            value (float): Value for the comparator.

        Keyword Args:
            custom_bg_color (str): [optional] Color palette to apply to the background, same values available as palette.
            custom_fg_color (str): [optional] Color palette to apply to the foreground, same values available as palette.
            hide_value (bool): [optional] True hides values.
            image_url (str): [optional] Displays an image as the background.
            metric (str): [optional] Metric from the request to correlate this conditional format with.
            timeframe (str): [optional] Defines the displayed timeframe.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.comparator = comparator
        self.palette = palette
        self.value = value

    @classmethod
    def _from_openapi_data(cls, comparator, palette, value, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(WidgetConditionalFormat, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.comparator = comparator
        self.palette = palette
        self.value = value
        return self
