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


class CallbackUrl(Model):
    """The callback url.

    :param value: The URL value.
    :type value: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CallbackUrl, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
