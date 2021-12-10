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
    from datadog_api_client.v1.model.synthetics_global_variable_parse_test_options_type import (
        SyntheticsGlobalVariableParseTestOptionsType,
    )
    from datadog_api_client.v1.model.synthetics_variable_parser import SyntheticsVariableParser

    globals()["SyntheticsGlobalVariableParseTestOptionsType"] = SyntheticsGlobalVariableParseTestOptionsType
    globals()["SyntheticsVariableParser"] = SyntheticsVariableParser


class SyntheticsGlobalVariableParseTestOptions(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "field": (str,),
            "parser": (SyntheticsVariableParser,),
            "type": (SyntheticsGlobalVariableParseTestOptionsType,),
        }

    attribute_map = {
        "parser": "parser",
        "type": "type",
        "field": "field",
    }

    read_only_vars = {}

    def __init__(self, parser, type, *args, **kwargs):
        """SyntheticsGlobalVariableParseTestOptions - a model defined in OpenAPI

        Args:
            parser (SyntheticsVariableParser):
            type (SyntheticsGlobalVariableParseTestOptionsType):

        Keyword Args:
            field (str): [optional] When type is `http_header`, name of the header to use to extract the value.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.parser = parser
        self.type = type

    @classmethod
    def _from_openapi_data(cls, parser, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsGlobalVariableParseTestOptions, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.parser = parser
        self.type = type
        return self
