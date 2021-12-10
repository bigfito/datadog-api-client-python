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
    from datadog_api_client.v1.model.usage_indexed_spans_hour import UsageIndexedSpansHour

    globals()["UsageIndexedSpansHour"] = UsageIndexedSpansHour


class UsageIndexedSpansResponse(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "usage": ([UsageIndexedSpansHour],),
        }

    attribute_map = {
        "usage": "usage",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """UsageIndexedSpansResponse - a model defined in OpenAPI

        Keyword Args:
            usage ([UsageIndexedSpansHour]): [optional] Array with the number of hourly traces indexed for a given organization.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageIndexedSpansResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
