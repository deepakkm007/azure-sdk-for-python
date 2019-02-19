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

from .sub_resource import SubResource


class ExpressRouteCircuitPeering(SubResource):
    """Peering in an ExpressRouteCircuit resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :param peering_type: The peering type. Possible values include:
     'AzurePublicPeering', 'AzurePrivatePeering', 'MicrosoftPeering'
    :type peering_type: str or
     ~azure.mgmt.network.v2018_12_01.models.ExpressRoutePeeringType
    :param state: The peering state. Possible values include: 'Disabled',
     'Enabled'
    :type state: str or
     ~azure.mgmt.network.v2018_12_01.models.ExpressRoutePeeringState
    :param azure_asn: The Azure ASN.
    :type azure_asn: int
    :param peer_asn: The peer ASN.
    :type peer_asn: long
    :param primary_peer_address_prefix: The primary address prefix.
    :type primary_peer_address_prefix: str
    :param secondary_peer_address_prefix: The secondary address prefix.
    :type secondary_peer_address_prefix: str
    :param primary_azure_port: The primary port.
    :type primary_azure_port: str
    :param secondary_azure_port: The secondary port.
    :type secondary_azure_port: str
    :param shared_key: The shared key.
    :type shared_key: str
    :param vlan_id: The VLAN ID.
    :type vlan_id: int
    :param microsoft_peering_config: The Microsoft peering configuration.
    :type microsoft_peering_config:
     ~azure.mgmt.network.v2018_12_01.models.ExpressRouteCircuitPeeringConfig
    :param stats: Gets peering stats.
    :type stats:
     ~azure.mgmt.network.v2018_12_01.models.ExpressRouteCircuitStats
    :param provisioning_state: Gets the provisioning state of the public IP
     resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :type provisioning_state: str
    :param gateway_manager_etag: The GatewayManager Etag.
    :type gateway_manager_etag: str
    :param last_modified_by: Gets whether the provider or the customer last
     modified the peering.
    :type last_modified_by: str
    :param route_filter: The reference of the RouteFilter resource.
    :type route_filter: ~azure.mgmt.network.v2018_12_01.models.RouteFilter
    :param ipv6_peering_config: The IPv6 peering configuration.
    :type ipv6_peering_config:
     ~azure.mgmt.network.v2018_12_01.models.Ipv6ExpressRouteCircuitPeeringConfig
    :param express_route_connection: The ExpressRoute connection.
    :type express_route_connection:
     ~azure.mgmt.network.v2018_12_01.models.ExpressRouteConnectionId
    :param connections: The list of circuit connections associated with Azure
     Private Peering for this circuit.
    :type connections:
     list[~azure.mgmt.network.v2018_12_01.models.ExpressRouteCircuitConnection]
    :param name: Gets name of the resource that is unique within a resource
     group. This name can be used to access the resource.
    :type name: str
    :ivar etag: A unique read-only string that changes whenever the resource
     is updated.
    :vartype etag: str
    """

    _validation = {
        'peer_asn': {'maximum': 4294967295, 'minimum': 1},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'peering_type': {'key': 'properties.peeringType', 'type': 'str'},
        'state': {'key': 'properties.state', 'type': 'str'},
        'azure_asn': {'key': 'properties.azureASN', 'type': 'int'},
        'peer_asn': {'key': 'properties.peerASN', 'type': 'long'},
        'primary_peer_address_prefix': {'key': 'properties.primaryPeerAddressPrefix', 'type': 'str'},
        'secondary_peer_address_prefix': {'key': 'properties.secondaryPeerAddressPrefix', 'type': 'str'},
        'primary_azure_port': {'key': 'properties.primaryAzurePort', 'type': 'str'},
        'secondary_azure_port': {'key': 'properties.secondaryAzurePort', 'type': 'str'},
        'shared_key': {'key': 'properties.sharedKey', 'type': 'str'},
        'vlan_id': {'key': 'properties.vlanId', 'type': 'int'},
        'microsoft_peering_config': {'key': 'properties.microsoftPeeringConfig', 'type': 'ExpressRouteCircuitPeeringConfig'},
        'stats': {'key': 'properties.stats', 'type': 'ExpressRouteCircuitStats'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'gateway_manager_etag': {'key': 'properties.gatewayManagerEtag', 'type': 'str'},
        'last_modified_by': {'key': 'properties.lastModifiedBy', 'type': 'str'},
        'route_filter': {'key': 'properties.routeFilter', 'type': 'RouteFilter'},
        'ipv6_peering_config': {'key': 'properties.ipv6PeeringConfig', 'type': 'Ipv6ExpressRouteCircuitPeeringConfig'},
        'express_route_connection': {'key': 'properties.expressRouteConnection', 'type': 'ExpressRouteConnectionId'},
        'connections': {'key': 'properties.connections', 'type': '[ExpressRouteCircuitConnection]'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ExpressRouteCircuitPeering, self).__init__(**kwargs)
        self.peering_type = kwargs.get('peering_type', None)
        self.state = kwargs.get('state', None)
        self.azure_asn = kwargs.get('azure_asn', None)
        self.peer_asn = kwargs.get('peer_asn', None)
        self.primary_peer_address_prefix = kwargs.get('primary_peer_address_prefix', None)
        self.secondary_peer_address_prefix = kwargs.get('secondary_peer_address_prefix', None)
        self.primary_azure_port = kwargs.get('primary_azure_port', None)
        self.secondary_azure_port = kwargs.get('secondary_azure_port', None)
        self.shared_key = kwargs.get('shared_key', None)
        self.vlan_id = kwargs.get('vlan_id', None)
        self.microsoft_peering_config = kwargs.get('microsoft_peering_config', None)
        self.stats = kwargs.get('stats', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.gateway_manager_etag = kwargs.get('gateway_manager_etag', None)
        self.last_modified_by = kwargs.get('last_modified_by', None)
        self.route_filter = kwargs.get('route_filter', None)
        self.ipv6_peering_config = kwargs.get('ipv6_peering_config', None)
        self.express_route_connection = kwargs.get('express_route_connection', None)
        self.connections = kwargs.get('connections', None)
        self.name = kwargs.get('name', None)
        self.etag = None
