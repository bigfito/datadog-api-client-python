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
    from datadog_api_client.v1.model.logs_attribute_remapper_type import LogsAttributeRemapperType
    from datadog_api_client.v1.model.target_format_type import TargetFormatType

    globals()["LogsAttributeRemapperType"] = LogsAttributeRemapperType
    globals()["TargetFormatType"] = TargetFormatType


class LogsAttributeRemapper(ModelNormal):
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
            "override_on_conflict": (bool,),
            "preserve_source": (bool,),
            "source_type": (str,),
            "sources": ([str],),
            "target": (str,),
            "target_format": (TargetFormatType,),
            "target_type": (str,),
            "type": (LogsAttributeRemapperType,),
        }

    attribute_map = {
        "sources": "sources",
        "target": "target",
        "type": "type",
        "is_enabled": "is_enabled",
        "name": "name",
        "override_on_conflict": "override_on_conflict",
        "preserve_source": "preserve_source",
        "source_type": "source_type",
        "target_format": "target_format",
        "target_type": "target_type",
    }

    read_only_vars = {}

    def __init__(self, sources, target, type, *args, **kwargs):
        """LogsAttributeRemapper - a model defined in OpenAPI

        Args:
            sources ([str]): Array of source attributes.
            target (str): Final attribute or tag name to remap the sources to.
            type (LogsAttributeRemapperType):

        Keyword Args:
            is_enabled (bool): [optional] Whether or not the processor is enabled. If omitted the server will use the default value of False.
            name (str): [optional] Name of the processor.
            override_on_conflict (bool): [optional] Override or not the target element if already set, If omitted the server will use the default value of False.
            preserve_source (bool): [optional] Remove or preserve the remapped source element. If omitted the server will use the default value of False.
            source_type (str): [optional] Defines if the sources are from log `attribute` or `tag`. If omitted the server will use the default value of "attribute".
            target_format (TargetFormatType): [optional]
            target_type (str): [optional] Defines if the final attribute or tag name is from log `attribute` or `tag`. If omitted the server will use the default value of "attribute".
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.sources = sources
        self.target = target
        self.type = type

    @classmethod
    def _from_openapi_data(cls, sources, target, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsAttributeRemapper, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.sources = sources
        self.target = target
        self.type = type
        return self
