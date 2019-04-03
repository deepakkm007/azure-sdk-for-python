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


class ResourceGroupExportResult(Model):
    """Resource group export result.

    :param template: The template content.
    :type template: object
    :param error: The error.
    :type error:
     ~azure.mgmt.resource.resources.v2017_05_10.models.ResourceManagementErrorWithDetails
    """

    _attribute_map = {
        'template': {'key': 'template', 'type': 'object'},
        'error': {'key': 'error', 'type': 'ResourceManagementErrorWithDetails'},
    }

    def __init__(self, *, template=None, error=None, **kwargs) -> None:
        super(ResourceGroupExportResult, self).__init__(**kwargs)
        self.template = template
        self.error = error
