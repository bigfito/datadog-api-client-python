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


class LogsArchiveIntegrationS3(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "account_id": (str,),
            "role_name": (str,),
        }

    attribute_map = {
        "account_id": "account_id",
        "role_name": "role_name",
    }

    read_only_vars = {}

    def __init__(self, account_id, role_name, *args, **kwargs):
        """LogsArchiveIntegrationS3 - a model defined in OpenAPI

        Args:
            account_id (str): The account ID for the integration.
            role_name (str): The path of the integration.

        Keyword Args:
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.account_id = account_id
        self.role_name = role_name

    @classmethod
    def _from_openapi_data(cls, account_id, role_name, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsArchiveIntegrationS3, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.account_id = account_id
        self.role_name = role_name
        return self
