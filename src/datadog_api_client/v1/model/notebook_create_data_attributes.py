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
    from datadog_api_client.v1.model.notebook_cell_create_request import NotebookCellCreateRequest
    from datadog_api_client.v1.model.notebook_global_time import NotebookGlobalTime
    from datadog_api_client.v1.model.notebook_metadata import NotebookMetadata
    from datadog_api_client.v1.model.notebook_status import NotebookStatus

    globals()["NotebookCellCreateRequest"] = NotebookCellCreateRequest
    globals()["NotebookGlobalTime"] = NotebookGlobalTime
    globals()["NotebookMetadata"] = NotebookMetadata
    globals()["NotebookStatus"] = NotebookStatus


class NotebookCreateDataAttributes(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {
        "name": {
            "max_length": 80,
            "min_length": 0,
        },
    }

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "cells": ([NotebookCellCreateRequest],),
            "metadata": (NotebookMetadata,),
            "name": (str,),
            "status": (NotebookStatus,),
            "time": (NotebookGlobalTime,),
        }

    attribute_map = {
        "cells": "cells",
        "name": "name",
        "time": "time",
        "metadata": "metadata",
        "status": "status",
    }

    read_only_vars = {}

    def __init__(self, cells, name, time, *args, **kwargs):
        """NotebookCreateDataAttributes - a model defined in OpenAPI

        Args:
            cells ([NotebookCellCreateRequest]): List of cells to display in the notebook.
            name (str): The name of the notebook.
            time (NotebookGlobalTime):

        Keyword Args:
            metadata (NotebookMetadata): [optional]
            status (NotebookStatus): [optional]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.cells = cells
        self.name = name
        self.time = time

    @classmethod
    def _from_openapi_data(cls, cells, name, time, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(NotebookCreateDataAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.cells = cells
        self.name = name
        self.time = time
        return self
