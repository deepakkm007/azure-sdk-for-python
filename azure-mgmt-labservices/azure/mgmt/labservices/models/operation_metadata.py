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

from msrest.serialization import Model


class OperationMetadata(Model):
    """The REST API operation supported by ManagedLab ResourceProvider.

    :param name: Operation name: {provider}/{resource}/{operation}
    :type name: str
    :param display: The object that describes the operations
    :type display: ~azure.mgmt.labservices.models.OperationMetadataDisplay
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationMetadataDisplay'},
    }

    def __init__(self, **kwargs):
        super(OperationMetadata, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display = kwargs.get('display', None)
