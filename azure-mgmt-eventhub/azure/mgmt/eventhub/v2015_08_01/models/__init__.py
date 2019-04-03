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

try:
    from .operation_display_py3 import OperationDisplay
    from .operation_py3 import Operation
    from .tracked_resource_py3 import TrackedResource
    from .resource_py3 import Resource
    from .sku_py3 import Sku
    from .namespace_create_or_update_parameters_py3 import NamespaceCreateOrUpdateParameters
    from .namespace_resource_py3 import NamespaceResource
    from .shared_access_authorization_rule_create_or_update_parameters_py3 import SharedAccessAuthorizationRuleCreateOrUpdateParameters
    from .shared_access_authorization_rule_resource_py3 import SharedAccessAuthorizationRuleResource
    from .resource_list_keys_py3 import ResourceListKeys
    from .regenerate_keys_parameters_py3 import RegenerateKeysParameters
    from .event_hub_create_or_update_parameters_py3 import EventHubCreateOrUpdateParameters
    from .event_hub_resource_py3 import EventHubResource
    from .consumer_group_create_or_update_parameters_py3 import ConsumerGroupCreateOrUpdateParameters
    from .consumer_group_resource_py3 import ConsumerGroupResource
    from .check_name_availability_parameter_py3 import CheckNameAvailabilityParameter
    from .check_name_availability_result_py3 import CheckNameAvailabilityResult
    from .namespace_update_parameter_py3 import NamespaceUpdateParameter
except (SyntaxError, ImportError):
    from .operation_display import OperationDisplay
    from .operation import Operation
    from .tracked_resource import TrackedResource
    from .resource import Resource
    from .sku import Sku
    from .namespace_create_or_update_parameters import NamespaceCreateOrUpdateParameters
    from .namespace_resource import NamespaceResource
    from .shared_access_authorization_rule_create_or_update_parameters import SharedAccessAuthorizationRuleCreateOrUpdateParameters
    from .shared_access_authorization_rule_resource import SharedAccessAuthorizationRuleResource
    from .resource_list_keys import ResourceListKeys
    from .regenerate_keys_parameters import RegenerateKeysParameters
    from .event_hub_create_or_update_parameters import EventHubCreateOrUpdateParameters
    from .event_hub_resource import EventHubResource
    from .consumer_group_create_or_update_parameters import ConsumerGroupCreateOrUpdateParameters
    from .consumer_group_resource import ConsumerGroupResource
    from .check_name_availability_parameter import CheckNameAvailabilityParameter
    from .check_name_availability_result import CheckNameAvailabilityResult
    from .namespace_update_parameter import NamespaceUpdateParameter
from .operation_paged import OperationPaged
from .namespace_resource_paged import NamespaceResourcePaged
from .shared_access_authorization_rule_resource_paged import SharedAccessAuthorizationRuleResourcePaged
from .event_hub_resource_paged import EventHubResourcePaged
from .consumer_group_resource_paged import ConsumerGroupResourcePaged
from .event_hub_management_client_enums import (
    SkuName,
    SkuTier,
    NamespaceState,
    AccessRights,
    Policykey,
    EntityStatus,
    UnavailableReason,
)

__all__ = [
    'OperationDisplay',
    'Operation',
    'TrackedResource',
    'Resource',
    'Sku',
    'NamespaceCreateOrUpdateParameters',
    'NamespaceResource',
    'SharedAccessAuthorizationRuleCreateOrUpdateParameters',
    'SharedAccessAuthorizationRuleResource',
    'ResourceListKeys',
    'RegenerateKeysParameters',
    'EventHubCreateOrUpdateParameters',
    'EventHubResource',
    'ConsumerGroupCreateOrUpdateParameters',
    'ConsumerGroupResource',
    'CheckNameAvailabilityParameter',
    'CheckNameAvailabilityResult',
    'NamespaceUpdateParameter',
    'OperationPaged',
    'NamespaceResourcePaged',
    'SharedAccessAuthorizationRuleResourcePaged',
    'EventHubResourcePaged',
    'ConsumerGroupResourcePaged',
    'SkuName',
    'SkuTier',
    'NamespaceState',
    'AccessRights',
    'Policykey',
    'EntityStatus',
    'UnavailableReason',
]
