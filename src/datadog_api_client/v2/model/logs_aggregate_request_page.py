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


class LogsAggregateRequestPage(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "cursor": (str,),
        }

    attribute_map = {
        "cursor": "cursor",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """LogsAggregateRequestPage - a model defined in OpenAPI

        Keyword Args:
            cursor (str): [optional] The returned paging point to use to get the next results
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsAggregateRequestPage, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
