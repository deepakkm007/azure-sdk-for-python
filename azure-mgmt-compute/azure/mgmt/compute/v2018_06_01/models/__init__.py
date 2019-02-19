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
    from .compute_operation_value_py3 import ComputeOperationValue
    from .instance_view_status_py3 import InstanceViewStatus
    from .sub_resource_py3 import SubResource
    from .sku_py3 import Sku
    from .availability_set_py3 import AvailabilitySet
    from .availability_set_update_py3 import AvailabilitySetUpdate
    from .virtual_machine_size_py3 import VirtualMachineSize
    from .virtual_machine_extension_image_py3 import VirtualMachineExtensionImage
    from .virtual_machine_image_resource_py3 import VirtualMachineImageResource
    from .virtual_machine_extension_instance_view_py3 import VirtualMachineExtensionInstanceView
    from .virtual_machine_extension_py3 import VirtualMachineExtension
    from .virtual_machine_extension_update_py3 import VirtualMachineExtensionUpdate
    from .virtual_machine_extensions_list_result_py3 import VirtualMachineExtensionsListResult
    from .purchase_plan_py3 import PurchasePlan
    from .os_disk_image_py3 import OSDiskImage
    from .data_disk_image_py3 import DataDiskImage
    from .virtual_machine_image_py3 import VirtualMachineImage
    from .usage_name_py3 import UsageName
    from .usage_py3 import Usage
    from .virtual_machine_reimage_parameters_py3 import VirtualMachineReimageParameters
    from .virtual_machine_capture_parameters_py3 import VirtualMachineCaptureParameters
    from .virtual_machine_capture_result_py3 import VirtualMachineCaptureResult
    from .plan_py3 import Plan
    from .hardware_profile_py3 import HardwareProfile
    from .image_reference_py3 import ImageReference
    from .key_vault_secret_reference_py3 import KeyVaultSecretReference
    from .key_vault_key_reference_py3 import KeyVaultKeyReference
    from .disk_encryption_settings_py3 import DiskEncryptionSettings
    from .virtual_hard_disk_py3 import VirtualHardDisk
    from .diff_disk_settings_py3 import DiffDiskSettings
    from .managed_disk_parameters_py3 import ManagedDiskParameters
    from .os_disk_py3 import OSDisk
    from .data_disk_py3 import DataDisk
    from .storage_profile_py3 import StorageProfile
    from .additional_capabilities_py3 import AdditionalCapabilities
    from .additional_unattend_content_py3 import AdditionalUnattendContent
    from .win_rm_listener_py3 import WinRMListener
    from .win_rm_configuration_py3 import WinRMConfiguration
    from .windows_configuration_py3 import WindowsConfiguration
    from .ssh_public_key_py3 import SshPublicKey
    from .ssh_configuration_py3 import SshConfiguration
    from .linux_configuration_py3 import LinuxConfiguration
    from .vault_certificate_py3 import VaultCertificate
    from .vault_secret_group_py3 import VaultSecretGroup
    from .os_profile_py3 import OSProfile
    from .network_interface_reference_py3 import NetworkInterfaceReference
    from .network_profile_py3 import NetworkProfile
    from .boot_diagnostics_py3 import BootDiagnostics
    from .diagnostics_profile_py3 import DiagnosticsProfile
    from .virtual_machine_extension_handler_instance_view_py3 import VirtualMachineExtensionHandlerInstanceView
    from .virtual_machine_agent_instance_view_py3 import VirtualMachineAgentInstanceView
    from .disk_instance_view_py3 import DiskInstanceView
    from .boot_diagnostics_instance_view_py3 import BootDiagnosticsInstanceView
    from .virtual_machine_identity_user_assigned_identities_value_py3 import VirtualMachineIdentityUserAssignedIdentitiesValue
    from .virtual_machine_identity_py3 import VirtualMachineIdentity
    from .maintenance_redeploy_status_py3 import MaintenanceRedeployStatus
    from .virtual_machine_instance_view_py3 import VirtualMachineInstanceView
    from .virtual_machine_py3 import VirtualMachine
    from .virtual_machine_update_py3 import VirtualMachineUpdate
    from .auto_os_upgrade_policy_py3 import AutoOSUpgradePolicy
    from .rolling_upgrade_policy_py3 import RollingUpgradePolicy
    from .upgrade_policy_py3 import UpgradePolicy
    from .image_os_disk_py3 import ImageOSDisk
    from .image_data_disk_py3 import ImageDataDisk
    from .image_storage_profile_py3 import ImageStorageProfile
    from .image_py3 import Image
    from .image_update_py3 import ImageUpdate
    from .virtual_machine_scale_set_identity_user_assigned_identities_value_py3 import VirtualMachineScaleSetIdentityUserAssignedIdentitiesValue
    from .virtual_machine_scale_set_identity_py3 import VirtualMachineScaleSetIdentity
    from .virtual_machine_scale_set_os_profile_py3 import VirtualMachineScaleSetOSProfile
    from .virtual_machine_scale_set_update_os_profile_py3 import VirtualMachineScaleSetUpdateOSProfile
    from .virtual_machine_scale_set_managed_disk_parameters_py3 import VirtualMachineScaleSetManagedDiskParameters
    from .virtual_machine_scale_set_os_disk_py3 import VirtualMachineScaleSetOSDisk
    from .virtual_machine_scale_set_update_os_disk_py3 import VirtualMachineScaleSetUpdateOSDisk
    from .virtual_machine_scale_set_data_disk_py3 import VirtualMachineScaleSetDataDisk
    from .virtual_machine_scale_set_storage_profile_py3 import VirtualMachineScaleSetStorageProfile
    from .virtual_machine_scale_set_update_storage_profile_py3 import VirtualMachineScaleSetUpdateStorageProfile
    from .api_entity_reference_py3 import ApiEntityReference
    from .virtual_machine_scale_set_public_ip_address_configuration_dns_settings_py3 import VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettings
    from .virtual_machine_scale_set_ip_tag_py3 import VirtualMachineScaleSetIpTag
    from .virtual_machine_scale_set_public_ip_address_configuration_py3 import VirtualMachineScaleSetPublicIPAddressConfiguration
    from .virtual_machine_scale_set_update_public_ip_address_configuration_py3 import VirtualMachineScaleSetUpdatePublicIPAddressConfiguration
    from .virtual_machine_scale_set_ip_configuration_py3 import VirtualMachineScaleSetIPConfiguration
    from .virtual_machine_scale_set_update_ip_configuration_py3 import VirtualMachineScaleSetUpdateIPConfiguration
    from .virtual_machine_scale_set_network_configuration_dns_settings_py3 import VirtualMachineScaleSetNetworkConfigurationDnsSettings
    from .virtual_machine_scale_set_network_configuration_py3 import VirtualMachineScaleSetNetworkConfiguration
    from .virtual_machine_scale_set_update_network_configuration_py3 import VirtualMachineScaleSetUpdateNetworkConfiguration
    from .virtual_machine_scale_set_network_profile_py3 import VirtualMachineScaleSetNetworkProfile
    from .virtual_machine_scale_set_update_network_profile_py3 import VirtualMachineScaleSetUpdateNetworkProfile
    from .virtual_machine_scale_set_extension_py3 import VirtualMachineScaleSetExtension
    from .virtual_machine_scale_set_extension_profile_py3 import VirtualMachineScaleSetExtensionProfile
    from .virtual_machine_scale_set_vm_profile_py3 import VirtualMachineScaleSetVMProfile
    from .virtual_machine_scale_set_update_vm_profile_py3 import VirtualMachineScaleSetUpdateVMProfile
    from .virtual_machine_scale_set_py3 import VirtualMachineScaleSet
    from .virtual_machine_scale_set_vm_reimage_parameters_py3 import VirtualMachineScaleSetVMReimageParameters
    from .virtual_machine_scale_set_reimage_parameters_py3 import VirtualMachineScaleSetReimageParameters
    from .virtual_machine_scale_set_update_py3 import VirtualMachineScaleSetUpdate
    from .virtual_machine_scale_set_vm_instance_ids_py3 import VirtualMachineScaleSetVMInstanceIDs
    from .virtual_machine_scale_set_vm_instance_required_ids_py3 import VirtualMachineScaleSetVMInstanceRequiredIDs
    from .virtual_machine_status_code_count_py3 import VirtualMachineStatusCodeCount
    from .virtual_machine_scale_set_instance_view_statuses_summary_py3 import VirtualMachineScaleSetInstanceViewStatusesSummary
    from .virtual_machine_scale_set_vm_extensions_summary_py3 import VirtualMachineScaleSetVMExtensionsSummary
    from .virtual_machine_scale_set_instance_view_py3 import VirtualMachineScaleSetInstanceView
    from .virtual_machine_scale_set_sku_capacity_py3 import VirtualMachineScaleSetSkuCapacity
    from .virtual_machine_scale_set_sku_py3 import VirtualMachineScaleSetSku
    from .api_error_base_py3 import ApiErrorBase
    from .inner_error_py3 import InnerError
    from .api_error_py3 import ApiError
    from .rollback_status_info_py3 import RollbackStatusInfo
    from .upgrade_operation_history_status_py3 import UpgradeOperationHistoryStatus
    from .rolling_upgrade_progress_info_py3 import RollingUpgradeProgressInfo
    from .upgrade_operation_historical_status_info_properties_py3 import UpgradeOperationHistoricalStatusInfoProperties
    from .upgrade_operation_historical_status_info_py3 import UpgradeOperationHistoricalStatusInfo
    from .virtual_machine_health_status_py3 import VirtualMachineHealthStatus
    from .virtual_machine_scale_set_vm_instance_view_py3 import VirtualMachineScaleSetVMInstanceView
    from .virtual_machine_scale_set_vm_py3 import VirtualMachineScaleSetVM
    from .rolling_upgrade_running_status_py3 import RollingUpgradeRunningStatus
    from .rolling_upgrade_status_info_py3 import RollingUpgradeStatusInfo
    from .resource_py3 import Resource
    from .update_resource_py3 import UpdateResource
    from .sub_resource_read_only_py3 import SubResourceReadOnly
    from .recovery_walk_response_py3 import RecoveryWalkResponse
    from .request_rate_by_interval_input_py3 import RequestRateByIntervalInput
    from .throttled_requests_input_py3 import ThrottledRequestsInput
    from .log_analytics_input_base_py3 import LogAnalyticsInputBase
    from .log_analytics_output_py3 import LogAnalyticsOutput
    from .log_analytics_operation_result_py3 import LogAnalyticsOperationResult
    from .run_command_input_parameter_py3 import RunCommandInputParameter
    from .run_command_input_py3 import RunCommandInput
    from .run_command_parameter_definition_py3 import RunCommandParameterDefinition
    from .run_command_document_base_py3 import RunCommandDocumentBase
    from .run_command_document_py3 import RunCommandDocument
    from .run_command_result_py3 import RunCommandResult
    from .gallery_identifier_py3 import GalleryIdentifier
    from .gallery_py3 import Gallery
    from .gallery_image_identifier_py3 import GalleryImageIdentifier
    from .resource_range_py3 import ResourceRange
    from .recommended_machine_configuration_py3 import RecommendedMachineConfiguration
    from .disallowed_py3 import Disallowed
    from .image_purchase_plan_py3 import ImagePurchasePlan
    from .gallery_image_py3 import GalleryImage
    from .gallery_image_version_publishing_profile_py3 import GalleryImageVersionPublishingProfile
    from .gallery_os_disk_image_py3 import GalleryOSDiskImage
    from .gallery_data_disk_image_py3 import GalleryDataDiskImage
    from .gallery_image_version_storage_profile_py3 import GalleryImageVersionStorageProfile
    from .regional_replication_status_py3 import RegionalReplicationStatus
    from .replication_status_py3 import ReplicationStatus
    from .gallery_image_version_py3 import GalleryImageVersion
    from .target_region_py3 import TargetRegion
    from .managed_artifact_py3 import ManagedArtifact
    from .gallery_artifact_source_py3 import GalleryArtifactSource
    from .gallery_artifact_publishing_profile_base_py3 import GalleryArtifactPublishingProfileBase
    from .gallery_disk_image_py3 import GalleryDiskImage
    from .disk_sku_py3 import DiskSku
    from .image_disk_reference_py3 import ImageDiskReference
    from .creation_data_py3 import CreationData
    from .source_vault_py3 import SourceVault
    from .key_vault_and_secret_reference_py3 import KeyVaultAndSecretReference
    from .key_vault_and_key_reference_py3 import KeyVaultAndKeyReference
    from .encryption_settings_py3 import EncryptionSettings
    from .disk_py3 import Disk
    from .disk_update_py3 import DiskUpdate
    from .snapshot_sku_py3 import SnapshotSku
    from .grant_access_data_py3 import GrantAccessData
    from .access_uri_py3 import AccessUri
    from .snapshot_py3 import Snapshot
    from .snapshot_update_py3 import SnapshotUpdate
except (SyntaxError, ImportError):
    from .compute_operation_value import ComputeOperationValue
    from .instance_view_status import InstanceViewStatus
    from .sub_resource import SubResource
    from .sku import Sku
    from .availability_set import AvailabilitySet
    from .availability_set_update import AvailabilitySetUpdate
    from .virtual_machine_size import VirtualMachineSize
    from .virtual_machine_extension_image import VirtualMachineExtensionImage
    from .virtual_machine_image_resource import VirtualMachineImageResource
    from .virtual_machine_extension_instance_view import VirtualMachineExtensionInstanceView
    from .virtual_machine_extension import VirtualMachineExtension
    from .virtual_machine_extension_update import VirtualMachineExtensionUpdate
    from .virtual_machine_extensions_list_result import VirtualMachineExtensionsListResult
    from .purchase_plan import PurchasePlan
    from .os_disk_image import OSDiskImage
    from .data_disk_image import DataDiskImage
    from .virtual_machine_image import VirtualMachineImage
    from .usage_name import UsageName
    from .usage import Usage
    from .virtual_machine_reimage_parameters import VirtualMachineReimageParameters
    from .virtual_machine_capture_parameters import VirtualMachineCaptureParameters
    from .virtual_machine_capture_result import VirtualMachineCaptureResult
    from .plan import Plan
    from .hardware_profile import HardwareProfile
    from .image_reference import ImageReference
    from .key_vault_secret_reference import KeyVaultSecretReference
    from .key_vault_key_reference import KeyVaultKeyReference
    from .disk_encryption_settings import DiskEncryptionSettings
    from .virtual_hard_disk import VirtualHardDisk
    from .diff_disk_settings import DiffDiskSettings
    from .managed_disk_parameters import ManagedDiskParameters
    from .os_disk import OSDisk
    from .data_disk import DataDisk
    from .storage_profile import StorageProfile
    from .additional_capabilities import AdditionalCapabilities
    from .additional_unattend_content import AdditionalUnattendContent
    from .win_rm_listener import WinRMListener
    from .win_rm_configuration import WinRMConfiguration
    from .windows_configuration import WindowsConfiguration
    from .ssh_public_key import SshPublicKey
    from .ssh_configuration import SshConfiguration
    from .linux_configuration import LinuxConfiguration
    from .vault_certificate import VaultCertificate
    from .vault_secret_group import VaultSecretGroup
    from .os_profile import OSProfile
    from .network_interface_reference import NetworkInterfaceReference
    from .network_profile import NetworkProfile
    from .boot_diagnostics import BootDiagnostics
    from .diagnostics_profile import DiagnosticsProfile
    from .virtual_machine_extension_handler_instance_view import VirtualMachineExtensionHandlerInstanceView
    from .virtual_machine_agent_instance_view import VirtualMachineAgentInstanceView
    from .disk_instance_view import DiskInstanceView
    from .boot_diagnostics_instance_view import BootDiagnosticsInstanceView
    from .virtual_machine_identity_user_assigned_identities_value import VirtualMachineIdentityUserAssignedIdentitiesValue
    from .virtual_machine_identity import VirtualMachineIdentity
    from .maintenance_redeploy_status import MaintenanceRedeployStatus
    from .virtual_machine_instance_view import VirtualMachineInstanceView
    from .virtual_machine import VirtualMachine
    from .virtual_machine_update import VirtualMachineUpdate
    from .auto_os_upgrade_policy import AutoOSUpgradePolicy
    from .rolling_upgrade_policy import RollingUpgradePolicy
    from .upgrade_policy import UpgradePolicy
    from .image_os_disk import ImageOSDisk
    from .image_data_disk import ImageDataDisk
    from .image_storage_profile import ImageStorageProfile
    from .image import Image
    from .image_update import ImageUpdate
    from .virtual_machine_scale_set_identity_user_assigned_identities_value import VirtualMachineScaleSetIdentityUserAssignedIdentitiesValue
    from .virtual_machine_scale_set_identity import VirtualMachineScaleSetIdentity
    from .virtual_machine_scale_set_os_profile import VirtualMachineScaleSetOSProfile
    from .virtual_machine_scale_set_update_os_profile import VirtualMachineScaleSetUpdateOSProfile
    from .virtual_machine_scale_set_managed_disk_parameters import VirtualMachineScaleSetManagedDiskParameters
    from .virtual_machine_scale_set_os_disk import VirtualMachineScaleSetOSDisk
    from .virtual_machine_scale_set_update_os_disk import VirtualMachineScaleSetUpdateOSDisk
    from .virtual_machine_scale_set_data_disk import VirtualMachineScaleSetDataDisk
    from .virtual_machine_scale_set_storage_profile import VirtualMachineScaleSetStorageProfile
    from .virtual_machine_scale_set_update_storage_profile import VirtualMachineScaleSetUpdateStorageProfile
    from .api_entity_reference import ApiEntityReference
    from .virtual_machine_scale_set_public_ip_address_configuration_dns_settings import VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettings
    from .virtual_machine_scale_set_ip_tag import VirtualMachineScaleSetIpTag
    from .virtual_machine_scale_set_public_ip_address_configuration import VirtualMachineScaleSetPublicIPAddressConfiguration
    from .virtual_machine_scale_set_update_public_ip_address_configuration import VirtualMachineScaleSetUpdatePublicIPAddressConfiguration
    from .virtual_machine_scale_set_ip_configuration import VirtualMachineScaleSetIPConfiguration
    from .virtual_machine_scale_set_update_ip_configuration import VirtualMachineScaleSetUpdateIPConfiguration
    from .virtual_machine_scale_set_network_configuration_dns_settings import VirtualMachineScaleSetNetworkConfigurationDnsSettings
    from .virtual_machine_scale_set_network_configuration import VirtualMachineScaleSetNetworkConfiguration
    from .virtual_machine_scale_set_update_network_configuration import VirtualMachineScaleSetUpdateNetworkConfiguration
    from .virtual_machine_scale_set_network_profile import VirtualMachineScaleSetNetworkProfile
    from .virtual_machine_scale_set_update_network_profile import VirtualMachineScaleSetUpdateNetworkProfile
    from .virtual_machine_scale_set_extension import VirtualMachineScaleSetExtension
    from .virtual_machine_scale_set_extension_profile import VirtualMachineScaleSetExtensionProfile
    from .virtual_machine_scale_set_vm_profile import VirtualMachineScaleSetVMProfile
    from .virtual_machine_scale_set_update_vm_profile import VirtualMachineScaleSetUpdateVMProfile
    from .virtual_machine_scale_set import VirtualMachineScaleSet
    from .virtual_machine_scale_set_vm_reimage_parameters import VirtualMachineScaleSetVMReimageParameters
    from .virtual_machine_scale_set_reimage_parameters import VirtualMachineScaleSetReimageParameters
    from .virtual_machine_scale_set_update import VirtualMachineScaleSetUpdate
    from .virtual_machine_scale_set_vm_instance_ids import VirtualMachineScaleSetVMInstanceIDs
    from .virtual_machine_scale_set_vm_instance_required_ids import VirtualMachineScaleSetVMInstanceRequiredIDs
    from .virtual_machine_status_code_count import VirtualMachineStatusCodeCount
    from .virtual_machine_scale_set_instance_view_statuses_summary import VirtualMachineScaleSetInstanceViewStatusesSummary
    from .virtual_machine_scale_set_vm_extensions_summary import VirtualMachineScaleSetVMExtensionsSummary
    from .virtual_machine_scale_set_instance_view import VirtualMachineScaleSetInstanceView
    from .virtual_machine_scale_set_sku_capacity import VirtualMachineScaleSetSkuCapacity
    from .virtual_machine_scale_set_sku import VirtualMachineScaleSetSku
    from .api_error_base import ApiErrorBase
    from .inner_error import InnerError
    from .api_error import ApiError
    from .rollback_status_info import RollbackStatusInfo
    from .upgrade_operation_history_status import UpgradeOperationHistoryStatus
    from .rolling_upgrade_progress_info import RollingUpgradeProgressInfo
    from .upgrade_operation_historical_status_info_properties import UpgradeOperationHistoricalStatusInfoProperties
    from .upgrade_operation_historical_status_info import UpgradeOperationHistoricalStatusInfo
    from .virtual_machine_health_status import VirtualMachineHealthStatus
    from .virtual_machine_scale_set_vm_instance_view import VirtualMachineScaleSetVMInstanceView
    from .virtual_machine_scale_set_vm import VirtualMachineScaleSetVM
    from .rolling_upgrade_running_status import RollingUpgradeRunningStatus
    from .rolling_upgrade_status_info import RollingUpgradeStatusInfo
    from .resource import Resource
    from .update_resource import UpdateResource
    from .sub_resource_read_only import SubResourceReadOnly
    from .recovery_walk_response import RecoveryWalkResponse
    from .request_rate_by_interval_input import RequestRateByIntervalInput
    from .throttled_requests_input import ThrottledRequestsInput
    from .log_analytics_input_base import LogAnalyticsInputBase
    from .log_analytics_output import LogAnalyticsOutput
    from .log_analytics_operation_result import LogAnalyticsOperationResult
    from .run_command_input_parameter import RunCommandInputParameter
    from .run_command_input import RunCommandInput
    from .run_command_parameter_definition import RunCommandParameterDefinition
    from .run_command_document_base import RunCommandDocumentBase
    from .run_command_document import RunCommandDocument
    from .run_command_result import RunCommandResult
    from .gallery_identifier import GalleryIdentifier
    from .gallery import Gallery
    from .gallery_image_identifier import GalleryImageIdentifier
    from .resource_range import ResourceRange
    from .recommended_machine_configuration import RecommendedMachineConfiguration
    from .disallowed import Disallowed
    from .image_purchase_plan import ImagePurchasePlan
    from .gallery_image import GalleryImage
    from .gallery_image_version_publishing_profile import GalleryImageVersionPublishingProfile
    from .gallery_os_disk_image import GalleryOSDiskImage
    from .gallery_data_disk_image import GalleryDataDiskImage
    from .gallery_image_version_storage_profile import GalleryImageVersionStorageProfile
    from .regional_replication_status import RegionalReplicationStatus
    from .replication_status import ReplicationStatus
    from .gallery_image_version import GalleryImageVersion
    from .target_region import TargetRegion
    from .managed_artifact import ManagedArtifact
    from .gallery_artifact_source import GalleryArtifactSource
    from .gallery_artifact_publishing_profile_base import GalleryArtifactPublishingProfileBase
    from .gallery_disk_image import GalleryDiskImage
    from .disk_sku import DiskSku
    from .image_disk_reference import ImageDiskReference
    from .creation_data import CreationData
    from .source_vault import SourceVault
    from .key_vault_and_secret_reference import KeyVaultAndSecretReference
    from .key_vault_and_key_reference import KeyVaultAndKeyReference
    from .encryption_settings import EncryptionSettings
    from .disk import Disk
    from .disk_update import DiskUpdate
    from .snapshot_sku import SnapshotSku
    from .grant_access_data import GrantAccessData
    from .access_uri import AccessUri
    from .snapshot import Snapshot
    from .snapshot_update import SnapshotUpdate
from .compute_operation_value_paged import ComputeOperationValuePaged
from .availability_set_paged import AvailabilitySetPaged
from .virtual_machine_size_paged import VirtualMachineSizePaged
from .usage_paged import UsagePaged
from .virtual_machine_paged import VirtualMachinePaged
from .image_paged import ImagePaged
from .virtual_machine_scale_set_paged import VirtualMachineScaleSetPaged
from .virtual_machine_scale_set_sku_paged import VirtualMachineScaleSetSkuPaged
from .upgrade_operation_historical_status_info_paged import UpgradeOperationHistoricalStatusInfoPaged
from .virtual_machine_scale_set_extension_paged import VirtualMachineScaleSetExtensionPaged
from .virtual_machine_scale_set_vm_paged import VirtualMachineScaleSetVMPaged
from .run_command_document_base_paged import RunCommandDocumentBasePaged
from .gallery_paged import GalleryPaged
from .gallery_image_paged import GalleryImagePaged
from .gallery_image_version_paged import GalleryImageVersionPaged
from .disk_paged import DiskPaged
from .snapshot_paged import SnapshotPaged
from .compute_management_client_enums import (
    StatusLevelTypes,
    AvailabilitySetSkuTypes,
    OperatingSystemTypes,
    VirtualMachineSizeTypes,
    CachingTypes,
    DiskCreateOptionTypes,
    StorageAccountTypes,
    DiffDiskOptions,
    PassNames,
    ComponentNames,
    SettingNames,
    ProtocolTypes,
    ResourceIdentityType,
    MaintenanceOperationResultCodeTypes,
    UpgradeMode,
    OperatingSystemStateTypes,
    IPVersion,
    VirtualMachinePriorityTypes,
    VirtualMachineEvictionPolicyTypes,
    VirtualMachineScaleSetSkuScaleType,
    UpgradeState,
    UpgradeOperationInvoker,
    RollingUpgradeStatusCode,
    RollingUpgradeActionType,
    IntervalInMins,
    AggregatedReplicationState,
    ReplicationState,
    HostCaching,
    DiskStorageAccountTypes,
    DiskCreateOption,
    SnapshotStorageAccountTypes,
    AccessLevel,
    InstanceViewTypes,
    ReplicationStatusTypes,
)

__all__ = [
    'ComputeOperationValue',
    'InstanceViewStatus',
    'SubResource',
    'Sku',
    'AvailabilitySet',
    'AvailabilitySetUpdate',
    'VirtualMachineSize',
    'VirtualMachineExtensionImage',
    'VirtualMachineImageResource',
    'VirtualMachineExtensionInstanceView',
    'VirtualMachineExtension',
    'VirtualMachineExtensionUpdate',
    'VirtualMachineExtensionsListResult',
    'PurchasePlan',
    'OSDiskImage',
    'DataDiskImage',
    'VirtualMachineImage',
    'UsageName',
    'Usage',
    'VirtualMachineReimageParameters',
    'VirtualMachineCaptureParameters',
    'VirtualMachineCaptureResult',
    'Plan',
    'HardwareProfile',
    'ImageReference',
    'KeyVaultSecretReference',
    'KeyVaultKeyReference',
    'DiskEncryptionSettings',
    'VirtualHardDisk',
    'DiffDiskSettings',
    'ManagedDiskParameters',
    'OSDisk',
    'DataDisk',
    'StorageProfile',
    'AdditionalCapabilities',
    'AdditionalUnattendContent',
    'WinRMListener',
    'WinRMConfiguration',
    'WindowsConfiguration',
    'SshPublicKey',
    'SshConfiguration',
    'LinuxConfiguration',
    'VaultCertificate',
    'VaultSecretGroup',
    'OSProfile',
    'NetworkInterfaceReference',
    'NetworkProfile',
    'BootDiagnostics',
    'DiagnosticsProfile',
    'VirtualMachineExtensionHandlerInstanceView',
    'VirtualMachineAgentInstanceView',
    'DiskInstanceView',
    'BootDiagnosticsInstanceView',
    'VirtualMachineIdentityUserAssignedIdentitiesValue',
    'VirtualMachineIdentity',
    'MaintenanceRedeployStatus',
    'VirtualMachineInstanceView',
    'VirtualMachine',
    'VirtualMachineUpdate',
    'AutoOSUpgradePolicy',
    'RollingUpgradePolicy',
    'UpgradePolicy',
    'ImageOSDisk',
    'ImageDataDisk',
    'ImageStorageProfile',
    'Image',
    'ImageUpdate',
    'VirtualMachineScaleSetIdentityUserAssignedIdentitiesValue',
    'VirtualMachineScaleSetIdentity',
    'VirtualMachineScaleSetOSProfile',
    'VirtualMachineScaleSetUpdateOSProfile',
    'VirtualMachineScaleSetManagedDiskParameters',
    'VirtualMachineScaleSetOSDisk',
    'VirtualMachineScaleSetUpdateOSDisk',
    'VirtualMachineScaleSetDataDisk',
    'VirtualMachineScaleSetStorageProfile',
    'VirtualMachineScaleSetUpdateStorageProfile',
    'ApiEntityReference',
    'VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettings',
    'VirtualMachineScaleSetIpTag',
    'VirtualMachineScaleSetPublicIPAddressConfiguration',
    'VirtualMachineScaleSetUpdatePublicIPAddressConfiguration',
    'VirtualMachineScaleSetIPConfiguration',
    'VirtualMachineScaleSetUpdateIPConfiguration',
    'VirtualMachineScaleSetNetworkConfigurationDnsSettings',
    'VirtualMachineScaleSetNetworkConfiguration',
    'VirtualMachineScaleSetUpdateNetworkConfiguration',
    'VirtualMachineScaleSetNetworkProfile',
    'VirtualMachineScaleSetUpdateNetworkProfile',
    'VirtualMachineScaleSetExtension',
    'VirtualMachineScaleSetExtensionProfile',
    'VirtualMachineScaleSetVMProfile',
    'VirtualMachineScaleSetUpdateVMProfile',
    'VirtualMachineScaleSet',
    'VirtualMachineScaleSetVMReimageParameters',
    'VirtualMachineScaleSetReimageParameters',
    'VirtualMachineScaleSetUpdate',
    'VirtualMachineScaleSetVMInstanceIDs',
    'VirtualMachineScaleSetVMInstanceRequiredIDs',
    'VirtualMachineStatusCodeCount',
    'VirtualMachineScaleSetInstanceViewStatusesSummary',
    'VirtualMachineScaleSetVMExtensionsSummary',
    'VirtualMachineScaleSetInstanceView',
    'VirtualMachineScaleSetSkuCapacity',
    'VirtualMachineScaleSetSku',
    'ApiErrorBase',
    'InnerError',
    'ApiError',
    'RollbackStatusInfo',
    'UpgradeOperationHistoryStatus',
    'RollingUpgradeProgressInfo',
    'UpgradeOperationHistoricalStatusInfoProperties',
    'UpgradeOperationHistoricalStatusInfo',
    'VirtualMachineHealthStatus',
    'VirtualMachineScaleSetVMInstanceView',
    'VirtualMachineScaleSetVM',
    'RollingUpgradeRunningStatus',
    'RollingUpgradeStatusInfo',
    'Resource',
    'UpdateResource',
    'SubResourceReadOnly',
    'RecoveryWalkResponse',
    'RequestRateByIntervalInput',
    'ThrottledRequestsInput',
    'LogAnalyticsInputBase',
    'LogAnalyticsOutput',
    'LogAnalyticsOperationResult',
    'RunCommandInputParameter',
    'RunCommandInput',
    'RunCommandParameterDefinition',
    'RunCommandDocumentBase',
    'RunCommandDocument',
    'RunCommandResult',
    'GalleryIdentifier',
    'Gallery',
    'GalleryImageIdentifier',
    'ResourceRange',
    'RecommendedMachineConfiguration',
    'Disallowed',
    'ImagePurchasePlan',
    'GalleryImage',
    'GalleryImageVersionPublishingProfile',
    'GalleryOSDiskImage',
    'GalleryDataDiskImage',
    'GalleryImageVersionStorageProfile',
    'RegionalReplicationStatus',
    'ReplicationStatus',
    'GalleryImageVersion',
    'TargetRegion',
    'ManagedArtifact',
    'GalleryArtifactSource',
    'GalleryArtifactPublishingProfileBase',
    'GalleryDiskImage',
    'DiskSku',
    'ImageDiskReference',
    'CreationData',
    'SourceVault',
    'KeyVaultAndSecretReference',
    'KeyVaultAndKeyReference',
    'EncryptionSettings',
    'Disk',
    'DiskUpdate',
    'SnapshotSku',
    'GrantAccessData',
    'AccessUri',
    'Snapshot',
    'SnapshotUpdate',
    'ComputeOperationValuePaged',
    'AvailabilitySetPaged',
    'VirtualMachineSizePaged',
    'UsagePaged',
    'VirtualMachinePaged',
    'ImagePaged',
    'VirtualMachineScaleSetPaged',
    'VirtualMachineScaleSetSkuPaged',
    'UpgradeOperationHistoricalStatusInfoPaged',
    'VirtualMachineScaleSetExtensionPaged',
    'VirtualMachineScaleSetVMPaged',
    'RunCommandDocumentBasePaged',
    'GalleryPaged',
    'GalleryImagePaged',
    'GalleryImageVersionPaged',
    'DiskPaged',
    'SnapshotPaged',
    'StatusLevelTypes',
    'AvailabilitySetSkuTypes',
    'OperatingSystemTypes',
    'VirtualMachineSizeTypes',
    'CachingTypes',
    'DiskCreateOptionTypes',
    'StorageAccountTypes',
    'DiffDiskOptions',
    'PassNames',
    'ComponentNames',
    'SettingNames',
    'ProtocolTypes',
    'ResourceIdentityType',
    'MaintenanceOperationResultCodeTypes',
    'UpgradeMode',
    'OperatingSystemStateTypes',
    'IPVersion',
    'VirtualMachinePriorityTypes',
    'VirtualMachineEvictionPolicyTypes',
    'VirtualMachineScaleSetSkuScaleType',
    'UpgradeState',
    'UpgradeOperationInvoker',
    'RollingUpgradeStatusCode',
    'RollingUpgradeActionType',
    'IntervalInMins',
    'AggregatedReplicationState',
    'ReplicationState',
    'HostCaching',
    'DiskStorageAccountTypes',
    'DiskCreateOption',
    'SnapshotStorageAccountTypes',
    'AccessLevel',
    'InstanceViewTypes',
    'ReplicationStatusTypes',
]
