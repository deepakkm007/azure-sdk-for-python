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


class SmartGroupModificationItem(Model):
    """smartGroup modification item.

    :param modification_event: Reason for the modification. Possible values
     include: 'SmartGroupCreated', 'StateChange', 'AlertAdded', 'AlertRemoved'
    :type modification_event: str or
     ~azure.mgmt.alertsmanagement.models.SmartGroupModificationEvent
    :param old_value: Old value
    :type old_value: str
    :param new_value: New value
    :type new_value: str
    :param modified_at: Modified date and time
    :type modified_at: str
    :param modified_by: Modified user details (Principal client name)
    :type modified_by: str
    :param comments: Modification comments
    :type comments: str
    :param description: Description of the modification
    :type description: str
    """

    _attribute_map = {
        'modification_event': {'key': 'modificationEvent', 'type': 'SmartGroupModificationEvent'},
        'old_value': {'key': 'oldValue', 'type': 'str'},
        'new_value': {'key': 'newValue', 'type': 'str'},
        'modified_at': {'key': 'modifiedAt', 'type': 'str'},
        'modified_by': {'key': 'modifiedBy', 'type': 'str'},
        'comments': {'key': 'comments', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, *, modification_event=None, old_value: str=None, new_value: str=None, modified_at: str=None, modified_by: str=None, comments: str=None, description: str=None, **kwargs) -> None:
        super(SmartGroupModificationItem, self).__init__(**kwargs)
        self.modification_event = modification_event
        self.old_value = old_value
        self.new_value = new_value
        self.modified_at = modified_at
        self.modified_by = modified_by
        self.comments = comments
        self.description = description
