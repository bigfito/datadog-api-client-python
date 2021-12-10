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


class UsageCustomReportsAttributes(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "computed_on": (str,),
            "end_date": (str,),
            "size": (int,),
            "start_date": (str,),
            "tags": ([str],),
        }

    attribute_map = {
        "computed_on": "computed_on",
        "end_date": "end_date",
        "size": "size",
        "start_date": "start_date",
        "tags": "tags",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """UsageCustomReportsAttributes - a model defined in OpenAPI

        Keyword Args:
            computed_on (str): [optional] The date the specified custom report was computed.
            end_date (str): [optional] The ending date of custom report.
            size (int): [optional] size
            start_date (str): [optional] The starting date of custom report.
            tags ([str]): [optional] A list of tags to apply to custom reports.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageCustomReportsAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
