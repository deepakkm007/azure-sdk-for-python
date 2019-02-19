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


class InboundNatPool(SubResource):
    """Inbound NAT pool of the load balancer.

    All required parameters must be populated in order to send to Azure.

    :param id: Resource ID.
    :type id: str
    :param frontend_ip_configuration: A reference to frontend IP addresses.
    :type frontend_ip_configuration:
     ~azure.mgmt.network.v2018_12_01.models.SubResource
    :param protocol: Required. Possible values include: 'Udp', 'Tcp', 'All'
    :type protocol: str or
     ~azure.mgmt.network.v2018_12_01.models.TransportProtocol
    :param frontend_port_range_start: Required. The first port number in the
     range of external ports that will be used to provide Inbound Nat to NICs
     associated with a load balancer. Acceptable values range between 1 and
     65534.
    :type frontend_port_range_start: int
    :param frontend_port_range_end: Required. The last port number in the
     range of external ports that will be used to provide Inbound Nat to NICs
     associated with a load balancer. Acceptable values range between 1 and
     65535.
    :type frontend_port_range_end: int
    :param backend_port: Required. The port used for internal connections on
     the endpoint. Acceptable values are between 1 and 65535.
    :type backend_port: int
    :param idle_timeout_in_minutes: The timeout for the TCP idle connection.
     The value can be set between 4 and 30 minutes. The default value is 4
     minutes. This element is only used when the protocol is set to TCP.
    :type idle_timeout_in_minutes: int
    :param enable_floating_ip: Configures a virtual machine's endpoint for the
     floating IP capability required to configure a SQL AlwaysOn Availability
     Group. This setting is required when using the SQL AlwaysOn Availability
     Groups in SQL server. This setting can't be changed after you create the
     endpoint.
    :type enable_floating_ip: bool
    :param enable_tcp_reset: Receive bidirectional TCP Reset on TCP flow idle
     timeout or unexpected connection termination. This element is only used
     when the protocol is set to TCP.
    :type enable_tcp_reset: bool
    :param provisioning_state: Gets the provisioning state of the PublicIP
     resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :type provisioning_state: str
    :param name: The name of the resource that is unique within a resource
     group. This name can be used to access the resource.
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _validation = {
        'protocol': {'required': True},
        'frontend_port_range_start': {'required': True},
        'frontend_port_range_end': {'required': True},
        'backend_port': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'frontend_ip_configuration': {'key': 'properties.frontendIPConfiguration', 'type': 'SubResource'},
        'protocol': {'key': 'properties.protocol', 'type': 'str'},
        'frontend_port_range_start': {'key': 'properties.frontendPortRangeStart', 'type': 'int'},
        'frontend_port_range_end': {'key': 'properties.frontendPortRangeEnd', 'type': 'int'},
        'backend_port': {'key': 'properties.backendPort', 'type': 'int'},
        'idle_timeout_in_minutes': {'key': 'properties.idleTimeoutInMinutes', 'type': 'int'},
        'enable_floating_ip': {'key': 'properties.enableFloatingIP', 'type': 'bool'},
        'enable_tcp_reset': {'key': 'properties.enableTcpReset', 'type': 'bool'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, *, protocol, frontend_port_range_start: int, frontend_port_range_end: int, backend_port: int, id: str=None, frontend_ip_configuration=None, idle_timeout_in_minutes: int=None, enable_floating_ip: bool=None, enable_tcp_reset: bool=None, provisioning_state: str=None, name: str=None, etag: str=None, **kwargs) -> None:
        super(InboundNatPool, self).__init__(id=id, **kwargs)
        self.frontend_ip_configuration = frontend_ip_configuration
        self.protocol = protocol
        self.frontend_port_range_start = frontend_port_range_start
        self.frontend_port_range_end = frontend_port_range_end
        self.backend_port = backend_port
        self.idle_timeout_in_minutes = idle_timeout_in_minutes
        self.enable_floating_ip = enable_floating_ip
        self.enable_tcp_reset = enable_tcp_reset
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = etag
