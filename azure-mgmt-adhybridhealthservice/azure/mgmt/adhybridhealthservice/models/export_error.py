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


class ExportError(Model):
    """The export error details.

    :param id: The error Id.
    :type id: str
    :param run_step_result_id: The run step result Id.
    :type run_step_result_id: str
    :param connector_id: The connector Id.
    :type connector_id: str
    :param type: The type of error.
    :type type: str
    :param error_code: The error code.
    :type error_code: str
    :param message: The export error message.
    :type message: str
    :param server_error_detail: The server error detail.
    :type server_error_detail: str
    :param time_first_occured: The date and time when the export error first
     occurred.
    :type time_first_occured: datetime
    :param retry_count: The retry count.
    :type retry_count: int
    :param cs_object_id: The cloud object Id.
    :type cs_object_id: str
    :param dn: The distinguished name.
    :type dn: str
    :param min_limit: The minimum limit.
    :type min_limit: str
    :param max_limit: The maximum limit.
    :type max_limit: str
    :param cloud_anchor: The name of the cloud anchor.
    :type cloud_anchor: str
    :param attribute_name: The attribute name.
    :type attribute_name: str
    :param attribute_value: The attribute value.
    :type attribute_value: str
    :param attribute_multi_value: Indicates if the attribute is multi valued
     or not.
    :type attribute_multi_value: bool
    :param object_id_conflict: The object Id with which there was an attribute
     conflict.
    :type object_id_conflict: str
    :param sam_account_name: The SAM account name.
    :type sam_account_name: str
    :param ad_object_type: The AD object type
    :type ad_object_type: str
    :param ad_object_guid: The AD object guid.
    :type ad_object_guid: str
    :param ad_display_name: The display name for the AD object.
    :type ad_display_name: str
    :param ad_source_of_authority: The source of authority for the AD object.
    :type ad_source_of_authority: str
    :param ad_source_anchor: The AD source anchor.
    :type ad_source_anchor: str
    :param ad_user_principal_name: The user principal name for the AD object.
    :type ad_user_principal_name: str
    :param ad_distinguished_name: The distinguished name for the AD object.
    :type ad_distinguished_name: str
    :param ad_mail: The email for the AD object.
    :type ad_mail: str
    :param time_occured: The date and time of occurrence.
    :type time_occured: datetime
    :param aad_object_type: The AAD side object type.
    :type aad_object_type: str
    :param aad_object_guid: The AAD side object guid.
    :type aad_object_guid: str
    :param aad_display_name: The AAD side display name
    :type aad_display_name: str
    :param aad_source_of_authority: The AAD side source of authority for the
     object.
    :type aad_source_of_authority: str
    :param aad_user_principal_name: The AAD side user principal name.
    :type aad_user_principal_name: str
    :param aad_distinguished_name: The AAD side distinguished name for the
     object.
    :type aad_distinguished_name: str
    :param aad_mail: The AAD side email for the object.
    :type aad_mail: str
    :param last_dir_sync_time: The date and time of last sync run.
    :type last_dir_sync_time: datetime
    :param modified_attribute_value: The modified attribute value.
    :type modified_attribute_value: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'run_step_result_id': {'key': 'runStepResultId', 'type': 'str'},
        'connector_id': {'key': 'connectorId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'error_code': {'key': 'errorCode', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'server_error_detail': {'key': 'serverErrorDetail', 'type': 'str'},
        'time_first_occured': {'key': 'timeFirstOccured', 'type': 'iso-8601'},
        'retry_count': {'key': 'retryCount', 'type': 'int'},
        'cs_object_id': {'key': 'csObjectId', 'type': 'str'},
        'dn': {'key': 'dn', 'type': 'str'},
        'min_limit': {'key': 'minLimit', 'type': 'str'},
        'max_limit': {'key': 'maxLimit', 'type': 'str'},
        'cloud_anchor': {'key': 'cloudAnchor', 'type': 'str'},
        'attribute_name': {'key': 'attributeName', 'type': 'str'},
        'attribute_value': {'key': 'attributeValue', 'type': 'str'},
        'attribute_multi_value': {'key': 'attributeMultiValue', 'type': 'bool'},
        'object_id_conflict': {'key': 'objectIdConflict', 'type': 'str'},
        'sam_account_name': {'key': 'samAccountName', 'type': 'str'},
        'ad_object_type': {'key': 'adObjectType', 'type': 'str'},
        'ad_object_guid': {'key': 'adObjectGuid', 'type': 'str'},
        'ad_display_name': {'key': 'adDisplayName', 'type': 'str'},
        'ad_source_of_authority': {'key': 'adSourceOfAuthority', 'type': 'str'},
        'ad_source_anchor': {'key': 'adSourceAnchor', 'type': 'str'},
        'ad_user_principal_name': {'key': 'adUserPrincipalName', 'type': 'str'},
        'ad_distinguished_name': {'key': 'adDistinguishedName', 'type': 'str'},
        'ad_mail': {'key': 'adMail', 'type': 'str'},
        'time_occured': {'key': 'timeOccured', 'type': 'iso-8601'},
        'aad_object_type': {'key': 'aadObjectType', 'type': 'str'},
        'aad_object_guid': {'key': 'aadObjectGuid', 'type': 'str'},
        'aad_display_name': {'key': 'aadDisplayName', 'type': 'str'},
        'aad_source_of_authority': {'key': 'aadSourceOfAuthority', 'type': 'str'},
        'aad_user_principal_name': {'key': 'aadUserPrincipalName', 'type': 'str'},
        'aad_distinguished_name': {'key': 'aadDistinguishedName', 'type': 'str'},
        'aad_mail': {'key': 'aadMail', 'type': 'str'},
        'last_dir_sync_time': {'key': 'lastDirSyncTime', 'type': 'iso-8601'},
        'modified_attribute_value': {'key': 'modifiedAttributeValue', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ExportError, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.run_step_result_id = kwargs.get('run_step_result_id', None)
        self.connector_id = kwargs.get('connector_id', None)
        self.type = kwargs.get('type', None)
        self.error_code = kwargs.get('error_code', None)
        self.message = kwargs.get('message', None)
        self.server_error_detail = kwargs.get('server_error_detail', None)
        self.time_first_occured = kwargs.get('time_first_occured', None)
        self.retry_count = kwargs.get('retry_count', None)
        self.cs_object_id = kwargs.get('cs_object_id', None)
        self.dn = kwargs.get('dn', None)
        self.min_limit = kwargs.get('min_limit', None)
        self.max_limit = kwargs.get('max_limit', None)
        self.cloud_anchor = kwargs.get('cloud_anchor', None)
        self.attribute_name = kwargs.get('attribute_name', None)
        self.attribute_value = kwargs.get('attribute_value', None)
        self.attribute_multi_value = kwargs.get('attribute_multi_value', None)
        self.object_id_conflict = kwargs.get('object_id_conflict', None)
        self.sam_account_name = kwargs.get('sam_account_name', None)
        self.ad_object_type = kwargs.get('ad_object_type', None)
        self.ad_object_guid = kwargs.get('ad_object_guid', None)
        self.ad_display_name = kwargs.get('ad_display_name', None)
        self.ad_source_of_authority = kwargs.get('ad_source_of_authority', None)
        self.ad_source_anchor = kwargs.get('ad_source_anchor', None)
        self.ad_user_principal_name = kwargs.get('ad_user_principal_name', None)
        self.ad_distinguished_name = kwargs.get('ad_distinguished_name', None)
        self.ad_mail = kwargs.get('ad_mail', None)
        self.time_occured = kwargs.get('time_occured', None)
        self.aad_object_type = kwargs.get('aad_object_type', None)
        self.aad_object_guid = kwargs.get('aad_object_guid', None)
        self.aad_display_name = kwargs.get('aad_display_name', None)
        self.aad_source_of_authority = kwargs.get('aad_source_of_authority', None)
        self.aad_user_principal_name = kwargs.get('aad_user_principal_name', None)
        self.aad_distinguished_name = kwargs.get('aad_distinguished_name', None)
        self.aad_mail = kwargs.get('aad_mail', None)
        self.last_dir_sync_time = kwargs.get('last_dir_sync_time', None)
        self.modified_attribute_value = kwargs.get('modified_attribute_value', None)
