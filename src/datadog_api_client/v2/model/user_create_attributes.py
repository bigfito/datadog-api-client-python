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


class UserCreateAttributes(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "email": (str,),
            "name": (str,),
            "title": (str,),
        }

    attribute_map = {
        "email": "email",
        "name": "name",
        "title": "title",
    }

    read_only_vars = {}

    def __init__(self, email, *args, **kwargs):
        """UserCreateAttributes - a model defined in OpenAPI

        Args:
            email (str): The email of the user.

        Keyword Args:
            name (str): [optional] The name of the user.
            title (str): [optional] The title of the user.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.email = email

    @classmethod
    def _from_openapi_data(cls, email, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UserCreateAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.email = email
        return self
