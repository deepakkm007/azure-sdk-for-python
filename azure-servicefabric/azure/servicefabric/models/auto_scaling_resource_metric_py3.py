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

from .auto_scaling_metric_py3 import AutoScalingMetric


class AutoScalingResourceMetric(AutoScalingMetric):
    """Describes the resource that is used for triggering auto scaling.

    All required parameters must be populated in order to send to Azure.

    :param kind: Required. Constant filled by server.
    :type kind: str
    :param name: Required. Name of the resource. Possible values include:
     'cpu', 'memoryInGB'
    :type name: str or
     ~azure.servicefabric.models.AutoScalingResourceMetricName
    """

    _validation = {
        'kind': {'required': True},
        'name': {'required': True},
    }

    _attribute_map = {
        'kind': {'key': 'kind', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, *, name, **kwargs) -> None:
        super(AutoScalingResourceMetric, self).__init__(**kwargs)
        self.name = name
        self.kind = 'Resource'
