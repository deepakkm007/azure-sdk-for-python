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


class VirtualWanSecurityProvider(Model):
    """Collection of SecurityProviders.

    :param name: Name of the security provider.
    :type name: str
    :param url: Url of the security provider.
    :type url: str
    :param type: Name of the security provider. Possible values include:
     'External', 'Native'
    :type type: str or
     ~azure.mgmt.network.v2018_11_01.models.VirtualWanSecurityProviderType
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, url: str=None, type=None, **kwargs) -> None:
        super(VirtualWanSecurityProvider, self).__init__(**kwargs)
        self.name = name
        self.url = url
        self.type = type
