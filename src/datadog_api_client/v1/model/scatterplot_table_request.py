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
    from datadog_api_client.v1.model.formula_and_function_query_definition import FormulaAndFunctionQueryDefinition
    from datadog_api_client.v1.model.formula_and_function_response_format import FormulaAndFunctionResponseFormat
    from datadog_api_client.v1.model.scatterplot_widget_formula import ScatterplotWidgetFormula

    globals()["FormulaAndFunctionQueryDefinition"] = FormulaAndFunctionQueryDefinition
    globals()["FormulaAndFunctionResponseFormat"] = FormulaAndFunctionResponseFormat
    globals()["ScatterplotWidgetFormula"] = ScatterplotWidgetFormula


class ScatterplotTableRequest(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "formulas": ([ScatterplotWidgetFormula],),
            "queries": ([FormulaAndFunctionQueryDefinition],),
            "response_format": (FormulaAndFunctionResponseFormat,),
        }

    attribute_map = {
        "formulas": "formulas",
        "queries": "queries",
        "response_format": "response_format",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """ScatterplotTableRequest - a model defined in OpenAPI

        Keyword Args:
            formulas ([ScatterplotWidgetFormula]): [optional] List of Scatterplot formulas that operate on queries. **This feature is currently in beta.**
            queries ([FormulaAndFunctionQueryDefinition]): [optional] List of queries that can be returned directly or used in formulas. **This feature is currently in beta.**
            response_format (FormulaAndFunctionResponseFormat): [optional]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(ScatterplotTableRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
