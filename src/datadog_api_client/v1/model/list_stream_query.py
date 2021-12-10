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
    from datadog_api_client.v1.model.list_stream_source import ListStreamSource

    globals()["ListStreamSource"] = ListStreamSource


class ListStreamQuery(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "data_source": (ListStreamSource,),
            "indexes": ([str],),
            "query_string": (str,),
        }

    attribute_map = {
        "data_source": "data_source",
        "query_string": "query_string",
        "indexes": "indexes",
    }

    read_only_vars = {}

    def __init__(self, data_source, query_string, *args, **kwargs):
        """ListStreamQuery - a model defined in OpenAPI

        Args:
            data_source (ListStreamSource):
            query_string (str): Widget query.

        Keyword Args:
            indexes ([str]): [optional] List of indexes.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.data_source = data_source
        self.query_string = query_string

    @classmethod
    def _from_openapi_data(cls, data_source, query_string, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(ListStreamQuery, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.data_source = data_source
        self.query_string = query_string
        return self
