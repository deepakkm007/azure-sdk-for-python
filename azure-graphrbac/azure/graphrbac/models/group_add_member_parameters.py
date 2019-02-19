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


class GroupAddMemberParameters(Model):
    """Request parameters for adding a member to a group.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param url: Required. A member object URL, such as
     "https://graph.windows.net/0b1f9851-1bf0-433f-aec3-cb9272f093dc/directoryObjects/f260bbc4-c254-447b-94cf-293b5ec434dd",
     where "0b1f9851-1bf0-433f-aec3-cb9272f093dc" is the tenantId and
     "f260bbc4-c254-447b-94cf-293b5ec434dd" is the objectId of the member
     (user, application, servicePrincipal, group) to be added.
    :type url: str
    """

    _validation = {
        'url': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'url': {'key': 'url', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(GroupAddMemberParameters, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.url = kwargs.get('url', None)
