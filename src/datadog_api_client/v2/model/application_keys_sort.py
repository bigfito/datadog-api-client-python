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


class ApplicationKeysSort(ModelSimple):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    allowed_values = {
        "value": {
            "CREATED_AT_ASCENDING": "created_at",
            "CREATED_AT_DESCENDING": "-created_at",
            "LAST4_ASCENDING": "last4",
            "LAST4_DESCENDING": "-last4",
            "NAME_ASCENDING": "name",
            "NAME_DESCENDING": "-name",
        },
    }

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "value": (str,),
        }

    def __init__(self, *args, **kwargs):
        """ApplicationKeysSort - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str): Sorting options If omitted defaults to "name". Must be one of ["created_at", "-created_at", "last4", "-last4", "name", "-name"].

        Keyword Args:
            value (str): Sorting options If omitted defaults to "name". Must be one of ["created_at", "-created_at", "last4", "-last4", "name", "-name"].
        """
        super().__init__(kwargs)

        if "value" in kwargs:
            value = kwargs.pop("value")
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            value = "name"

        self._check_pos_args(args)

        self.value = value

        self._check_kw_args(kwargs)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""
        return cls(*args, **kwargs)
