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
    from datadog_api_client.v1.model.synthetics_device import SyntheticsDevice
    from datadog_api_client.v1.model.synthetics_step_detail import SyntheticsStepDetail

    globals()["SyntheticsDevice"] = SyntheticsDevice
    globals()["SyntheticsStepDetail"] = SyntheticsStepDetail


class SyntheticsBrowserTestResultData(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "browser_type": (str,),
            "browser_version": (str,),
            "device": (SyntheticsDevice,),
            "duration": (float,),
            "error": (str,),
            "passed": (bool,),
            "received_email_count": (int,),
            "start_url": (str,),
            "step_details": ([SyntheticsStepDetail],),
            "thumbnails_bucket_key": (bool,),
            "time_to_interactive": (float,),
        }

    attribute_map = {
        "browser_type": "browserType",
        "browser_version": "browserVersion",
        "device": "device",
        "duration": "duration",
        "error": "error",
        "passed": "passed",
        "received_email_count": "receivedEmailCount",
        "start_url": "startUrl",
        "step_details": "stepDetails",
        "thumbnails_bucket_key": "thumbnailsBucketKey",
        "time_to_interactive": "timeToInteractive",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """SyntheticsBrowserTestResultData - a model defined in OpenAPI

        Keyword Args:
            browser_type (str): [optional] Type of browser device used for the browser test.
            browser_version (str): [optional] Browser version used for the browser test.
            device (SyntheticsDevice): [optional]
            duration (float): [optional] Global duration in second of the browser test.
            error (str): [optional] Error returned for the browser test.
            passed (bool): [optional] Whether or not the browser test was conducted.
            received_email_count (int): [optional] The amount of email received during the browser test.
            start_url (str): [optional] Starting URL for the browser test.
            step_details ([SyntheticsStepDetail]): [optional] Array containing the different browser test steps.
            thumbnails_bucket_key (bool): [optional] Whether or not a thumbnail is associated with the browser test.
            time_to_interactive (float): [optional] Time in second to wait before the browser test starts after reaching the start URL.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsBrowserTestResultData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
