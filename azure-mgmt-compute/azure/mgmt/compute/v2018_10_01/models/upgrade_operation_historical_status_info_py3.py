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


class UpgradeOperationHistoricalStatusInfo(Model):
    """Virtual Machine Scale Set OS Upgrade History operation response.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar properties: Information about the properties of the upgrade
     operation.
    :vartype properties:
     ~azure.mgmt.compute.v2018_10_01.models.UpgradeOperationHistoricalStatusInfoProperties
    :ivar type: Resource type
    :vartype type: str
    :ivar location: Resource location
    :vartype location: str
    """

    _validation = {
        'properties': {'readonly': True},
        'type': {'readonly': True},
        'location': {'readonly': True},
    }

    _attribute_map = {
        'properties': {'key': 'properties', 'type': 'UpgradeOperationHistoricalStatusInfoProperties'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(UpgradeOperationHistoricalStatusInfo, self).__init__(**kwargs)
        self.properties = None
        self.type = None
        self.location = None
