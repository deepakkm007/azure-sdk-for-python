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


class CsmPublishingProfileOptions(Model):
    """Publishing options for requested profile.

    :param format: Name of the format. Valid values are:
     FileZilla3
     WebDeploy -- default
     Ftp. Possible values include: 'FileZilla3', 'WebDeploy', 'Ftp'
    :type format: str or ~azure.mgmt.web.models.PublishingProfileFormat
    :param include_disaster_recovery_endpoints: Include the DisasterRecover
     endpoint if true
    :type include_disaster_recovery_endpoints: bool
    """

    _attribute_map = {
        'format': {'key': 'format', 'type': 'str'},
        'include_disaster_recovery_endpoints': {'key': 'includeDisasterRecoveryEndpoints', 'type': 'bool'},
    }

    def __init__(self, *, format=None, include_disaster_recovery_endpoints: bool=None, **kwargs) -> None:
        super(CsmPublishingProfileOptions, self).__init__(**kwargs)
        self.format = format
        self.include_disaster_recovery_endpoints = include_disaster_recovery_endpoints
