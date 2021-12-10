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


class AzureAccount(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "automute": (bool,),
            "client_id": (str,),
            "client_secret": (str,),
            "errors": ([str],),
            "host_filters": (str,),
            "new_client_id": (str,),
            "new_tenant_name": (str,),
            "tenant_name": (str,),
        }

    attribute_map = {
        "automute": "automute",
        "client_id": "client_id",
        "client_secret": "client_secret",
        "errors": "errors",
        "host_filters": "host_filters",
        "new_client_id": "new_client_id",
        "new_tenant_name": "new_tenant_name",
        "tenant_name": "tenant_name",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """AzureAccount - a model defined in OpenAPI

        Keyword Args:
            automute (bool): [optional] Silence monitors for expected Azure VM shutdowns.
            client_id (str): [optional] Your Azure web application ID.
            client_secret (str): [optional] Your Azure web application secret key.
            errors ([str]): [optional] Errors in your configuration.
            host_filters (str): [optional] Limit the Azure instances that are pulled into Datadog by using tags. Only hosts that match one of the defined tags are imported into Datadog.
            new_client_id (str): [optional] Your New Azure web application ID.
            new_tenant_name (str): [optional] Your New Azure Active Directory ID.
            tenant_name (str): [optional] Your Azure Active Directory ID.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(AzureAccount, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
