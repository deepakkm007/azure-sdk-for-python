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


class MetricAlertAction(Model):
    """An alert action.

    :param action_group_id: the id of the action group to use.
    :type action_group_id: str
    :param webhook_properties: The properties of a webhook object.
    :type webhook_properties: dict[str, str]
    """

    _attribute_map = {
        'action_group_id': {'key': 'actionGroupId', 'type': 'str'},
        'webhook_properties': {'key': 'webhookProperties', 'type': '{str}'},
    }

    def __init__(self, *, action_group_id: str=None, webhook_properties=None, **kwargs) -> None:
        super(MetricAlertAction, self).__init__(**kwargs)
        self.action_group_id = action_group_id
        self.webhook_properties = webhook_properties
