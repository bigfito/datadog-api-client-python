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


def lazy_import():
    from datadog_api_client.v2.model.logs_archive_destination_azure_type import LogsArchiveDestinationAzureType
    from datadog_api_client.v2.model.logs_archive_integration_azure import LogsArchiveIntegrationAzure

    globals()["LogsArchiveDestinationAzureType"] = LogsArchiveDestinationAzureType
    globals()["LogsArchiveIntegrationAzure"] = LogsArchiveIntegrationAzure


class LogsArchiveDestinationAzure(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "container": (str,),
            "integration": (LogsArchiveIntegrationAzure,),
            "path": (str,),
            "region": (str,),
            "storage_account": (str,),
            "type": (LogsArchiveDestinationAzureType,),
        }

    attribute_map = {
        "container": "container",
        "integration": "integration",
        "storage_account": "storage_account",
        "type": "type",
        "path": "path",
        "region": "region",
    }

    read_only_vars = {}

    def __init__(self, container, integration, storage_account, type, *args, **kwargs):
        """LogsArchiveDestinationAzure - a model defined in OpenAPI

        Args:
            container (str): The container where the archive will be stored.
            integration (LogsArchiveIntegrationAzure):
            storage_account (str): The associated storage account.
            type (LogsArchiveDestinationAzureType):

        Keyword Args:
            path (str): [optional] The archive path.
            region (str): [optional] The region where the archive will be stored.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.container = container
        self.integration = integration
        self.storage_account = storage_account
        self.type = type

    @classmethod
    def _from_openapi_data(cls, container, integration, storage_account, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsArchiveDestinationAzure, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.container = container
        self.integration = integration
        self.storage_account = storage_account
        self.type = type
        return self
