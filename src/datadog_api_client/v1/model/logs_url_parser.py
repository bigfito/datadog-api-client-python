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
    from datadog_api_client.v1.model.logs_url_parser_type import LogsURLParserType

    globals()["LogsURLParserType"] = LogsURLParserType


class LogsURLParser(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "is_enabled": (bool,),
            "name": (str,),
            "normalize_ending_slashes": (
                bool,
                none_type,
            ),
            "sources": ([str],),
            "target": (str,),
            "type": (LogsURLParserType,),
        }

    attribute_map = {
        "sources": "sources",
        "target": "target",
        "type": "type",
        "is_enabled": "is_enabled",
        "name": "name",
        "normalize_ending_slashes": "normalize_ending_slashes",
    }

    read_only_vars = {}

    def __init__(self, type, *args, **kwargs):
        """LogsURLParser - a model defined in OpenAPI

        Args:
            type (LogsURLParserType):

        Keyword Args:
            sources ([str]): Array of source attributes. Defaults to ["http.url"].
            target (str): Name of the parent attribute that contains all the extracted details from the `sources`. Defaults to "http.url_details".
            is_enabled (bool): [optional] Whether or not the processor is enabled. If omitted the server will use the default value of False.
            name (str): [optional] Name of the processor.
            normalize_ending_slashes (bool, none_type): [optional] Normalize the ending slashes or not. If omitted the server will use the default value of False.
        """
        super().__init__(kwargs)

        sources = kwargs.get("sources", ["http.url"])
        target = kwargs.get("target", "http.url_details")

        self._check_pos_args(args)

        self.sources = sources
        self.target = target
        self.type = type

    @classmethod
    def _from_openapi_data(cls, type, *args, **kwargs):
        """Helper creating a new instance from a response."""
        sources = kwargs.get("sources", ["http.url"])
        target = kwargs.get("target", "http.url_details")

        self = super(LogsURLParser, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.sources = sources
        self.target = target
        self.type = type
        return self
