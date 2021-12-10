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
    from datadog_api_client.v1.model.log_stream_widget_definition import LogStreamWidgetDefinition
    from datadog_api_client.v1.model.notebook_cell_time import NotebookCellTime
    from datadog_api_client.v1.model.notebook_distribution_cell_attributes import NotebookDistributionCellAttributes
    from datadog_api_client.v1.model.notebook_graph_size import NotebookGraphSize
    from datadog_api_client.v1.model.notebook_heat_map_cell_attributes import NotebookHeatMapCellAttributes
    from datadog_api_client.v1.model.notebook_log_stream_cell_attributes import NotebookLogStreamCellAttributes
    from datadog_api_client.v1.model.notebook_markdown_cell_attributes import NotebookMarkdownCellAttributes
    from datadog_api_client.v1.model.notebook_split_by import NotebookSplitBy
    from datadog_api_client.v1.model.notebook_timeseries_cell_attributes import NotebookTimeseriesCellAttributes
    from datadog_api_client.v1.model.notebook_toplist_cell_attributes import NotebookToplistCellAttributes

    globals()["LogStreamWidgetDefinition"] = LogStreamWidgetDefinition
    globals()["NotebookCellTime"] = NotebookCellTime
    globals()["NotebookDistributionCellAttributes"] = NotebookDistributionCellAttributes
    globals()["NotebookGraphSize"] = NotebookGraphSize
    globals()["NotebookHeatMapCellAttributes"] = NotebookHeatMapCellAttributes
    globals()["NotebookLogStreamCellAttributes"] = NotebookLogStreamCellAttributes
    globals()["NotebookMarkdownCellAttributes"] = NotebookMarkdownCellAttributes
    globals()["NotebookSplitBy"] = NotebookSplitBy
    globals()["NotebookTimeseriesCellAttributes"] = NotebookTimeseriesCellAttributes
    globals()["NotebookToplistCellAttributes"] = NotebookToplistCellAttributes


class NotebookCellCreateRequestAttributes(ModelComposed):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        return {}

    def __init__(self, *args, **kwargs):
        """NotebookCellCreateRequestAttributes - a model defined in OpenAPI

        Keyword Args:
            graph_size (NotebookGraphSize): [optional]
            split_by (NotebookSplitBy): [optional]
            time (NotebookCellTime): [optional]
            definition (LogStreamWidgetDefinition): [optional]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(NotebookCellCreateRequestAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
            "anyOf": [],
            "allOf": [],
            "oneOf": [
                NotebookDistributionCellAttributes,
                NotebookHeatMapCellAttributes,
                NotebookLogStreamCellAttributes,
                NotebookMarkdownCellAttributes,
                NotebookTimeseriesCellAttributes,
                NotebookToplistCellAttributes,
            ],
        }
