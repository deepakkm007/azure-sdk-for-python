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

from .service_properties_base_py3 import ServicePropertiesBase


class ServiceProperties(ServicePropertiesBase):
    """The service resource properties.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: StatelessServiceProperties, StatefulServiceProperties

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param placement_constraints: The placement constraints as a string.
     Placement constraints are boolean expressions on node properties and allow
     for restricting a service to particular nodes based on the service
     requirements. For example, to place a service on nodes where NodeType is
     blue specify the following: "NodeColor == blue)".
    :type placement_constraints: str
    :param correlation_scheme:
    :type correlation_scheme:
     list[~azure.mgmt.servicefabric.models.ServiceCorrelationDescription]
    :param service_load_metrics:
    :type service_load_metrics:
     list[~azure.mgmt.servicefabric.models.ServiceLoadMetricDescription]
    :param service_placement_policies:
    :type service_placement_policies:
     list[~azure.mgmt.servicefabric.models.ServicePlacementPolicyDescription]
    :param default_move_cost: Possible values include: 'Zero', 'Low',
     'Medium', 'High'
    :type default_move_cost: str or ~azure.mgmt.servicefabric.models.enum
    :ivar provisioning_state: The current deployment or provisioning state,
     which only appears in the response
    :vartype provisioning_state: str
    :param service_type_name: The name of the service type
    :type service_type_name: str
    :param partition_description:
    :type partition_description:
     ~azure.mgmt.servicefabric.models.PartitionSchemeDescription
    :param service_kind: Required. Constant filled by server.
    :type service_kind: str
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'service_kind': {'required': True},
    }

    _attribute_map = {
        'placement_constraints': {'key': 'placementConstraints', 'type': 'str'},
        'correlation_scheme': {'key': 'correlationScheme', 'type': '[ServiceCorrelationDescription]'},
        'service_load_metrics': {'key': 'serviceLoadMetrics', 'type': '[ServiceLoadMetricDescription]'},
        'service_placement_policies': {'key': 'servicePlacementPolicies', 'type': '[ServicePlacementPolicyDescription]'},
        'default_move_cost': {'key': 'defaultMoveCost', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'service_type_name': {'key': 'serviceTypeName', 'type': 'str'},
        'partition_description': {'key': 'partitionDescription', 'type': 'PartitionSchemeDescription'},
        'service_kind': {'key': 'serviceKind', 'type': 'str'},
    }

    _subtype_map = {
        'service_kind': {'Stateless': 'StatelessServiceProperties', 'Stateful': 'StatefulServiceProperties'}
    }

    def __init__(self, *, placement_constraints: str=None, correlation_scheme=None, service_load_metrics=None, service_placement_policies=None, default_move_cost=None, service_type_name: str=None, partition_description=None, **kwargs) -> None:
        super(ServiceProperties, self).__init__(placement_constraints=placement_constraints, correlation_scheme=correlation_scheme, service_load_metrics=service_load_metrics, service_placement_policies=service_placement_policies, default_move_cost=default_move_cost, **kwargs)
        self.provisioning_state = None
        self.service_type_name = service_type_name
        self.partition_description = partition_description
        self.service_kind = None
        self.service_kind = 'ServiceProperties'
