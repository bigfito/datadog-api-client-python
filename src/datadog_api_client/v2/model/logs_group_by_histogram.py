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


class LogsGroupByHistogram(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "interval": (float,),
            "max": (float,),
            "min": (float,),
        }

    attribute_map = {
        "interval": "interval",
        "max": "max",
        "min": "min",
    }

    read_only_vars = {}

    def __init__(self, interval, max, min, *args, **kwargs):
        """LogsGroupByHistogram - a model defined in OpenAPI

        Args:
            interval (float): The bin size of the histogram buckets
            max (float): The maximum value for the measure used in the histogram (values greater than this one are filtered out)
            min (float): The minimum value for the measure used in the histogram (values smaller than this one are filtered out)

        Keyword Args:
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.interval = interval
        self.max = max
        self.min = min

    @classmethod
    def _from_openapi_data(cls, interval, max, min, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsGroupByHistogram, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.interval = interval
        self.max = max
        self.min = min
        return self
