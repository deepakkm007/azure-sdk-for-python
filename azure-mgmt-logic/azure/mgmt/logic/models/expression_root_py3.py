# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .expression_py3 import Expression


class ExpressionRoot(Expression):
    """ExpressionRoot.

    :param text:
    :type text: str
    :param value:
    :type value: object
    :param subexpressions:
    :type subexpressions: list[~azure.mgmt.logic.models.Expression]
    :param error:
    :type error: ~azure.mgmt.logic.models.AzureResourceErrorInfo
    :param path: The path.
    :type path: str
    """

    _attribute_map = {
        'text': {'key': 'text', 'type': 'str'},
        'value': {'key': 'value', 'type': 'object'},
        'subexpressions': {'key': 'subexpressions', 'type': '[Expression]'},
        'error': {'key': 'error', 'type': 'AzureResourceErrorInfo'},
        'path': {'key': 'path', 'type': 'str'},
    }

    def __init__(self, *, text: str=None, value=None, subexpressions=None, error=None, path: str=None, **kwargs) -> None:
        super(ExpressionRoot, self).__init__(text=text, value=value, subexpressions=subexpressions, error=error, **kwargs)
        self.path = path
