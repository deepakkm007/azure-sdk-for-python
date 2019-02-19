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

try:
    from .feature_properties_py3 import FeatureProperties
    from .feature_result_py3 import FeatureResult
    from .operation_display_py3 import OperationDisplay
    from .operation_py3 import Operation
except (SyntaxError, ImportError):
    from .feature_properties import FeatureProperties
    from .feature_result import FeatureResult
    from .operation_display import OperationDisplay
    from .operation import Operation
from .operation_paged import OperationPaged
from .feature_result_paged import FeatureResultPaged

__all__ = [
    'FeatureProperties',
    'FeatureResult',
    'OperationDisplay',
    'Operation',
    'OperationPaged',
    'FeatureResultPaged',
]
