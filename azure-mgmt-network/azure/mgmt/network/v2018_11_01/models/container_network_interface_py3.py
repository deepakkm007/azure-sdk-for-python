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

from .sub_resource_py3 import SubResource


class ContainerNetworkInterface(SubResource):
    """Container network interface child resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :param container_network_interface_configuration: Container network
     interface configuration from which this container network interface is
     created.
    :type container_network_interface_configuration:
     ~azure.mgmt.network.v2018_11_01.models.ContainerNetworkInterfaceConfiguration
    :param container: Reference to the container to which this container
     network interface is attached.
    :type container: ~azure.mgmt.network.v2018_11_01.models.Container
    :param ip_configurations: Reference to the ip configuration on this
     container nic.
    :type ip_configurations:
     list[~azure.mgmt.network.v2018_11_01.models.ContainerNetworkInterfaceIpConfiguration]
    :ivar provisioning_state: The provisioning state of the resource.
    :vartype provisioning_state: str
    :param name: The name of the resource. This name can be used to access the
     resource.
    :type name: str
    :ivar type: Sub Resource type.
    :vartype type: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'container_network_interface_configuration': {'key': 'properties.containerNetworkInterfaceConfiguration', 'type': 'ContainerNetworkInterfaceConfiguration'},
        'container': {'key': 'properties.container', 'type': 'Container'},
        'ip_configurations': {'key': 'properties.ipConfigurations', 'type': '[ContainerNetworkInterfaceIpConfiguration]'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, container_network_interface_configuration=None, container=None, ip_configurations=None, name: str=None, etag: str=None, **kwargs) -> None:
        super(ContainerNetworkInterface, self).__init__(id=id, **kwargs)
        self.container_network_interface_configuration = container_network_interface_configuration
        self.container = container
        self.ip_configurations = ip_configurations
        self.provisioning_state = None
        self.name = name
        self.type = None
        self.etag = etag
