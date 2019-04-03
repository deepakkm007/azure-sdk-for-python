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


class MapsAccountCreateParameters(Model):
    """Parameters used to create a new Maps Account.

    All required parameters must be populated in order to send to Azure.

    :param location: Required. The location of the resource.
    :type location: str
    :param tags: Gets or sets a list of key value pairs that describe the
     resource. These tags can be used in viewing and grouping this resource
     (across resource groups). A maximum of 15 tags can be provided for a
     resource. Each tag must have a key no greater than 128 characters and
     value no greater than 256 characters.
    :type tags: dict[str, str]
    :param sku: Required. The SKU of this account.
    :type sku: ~azure.mgmt.maps.models.Sku
    """

    _validation = {
        'location': {'required': True},
        'sku': {'required': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'Sku'},
    }

    def __init__(self, *, location: str, sku, tags=None, **kwargs) -> None:
        super(MapsAccountCreateParameters, self).__init__(**kwargs)
        self.location = location
        self.tags = tags
        self.sku = sku
