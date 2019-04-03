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


class ElasticPoolPerDatabaseSettings(Model):
    """Per database settings of an elastic pool.

    :param min_capacity: The minimum capacity all databases are guaranteed.
    :type min_capacity: float
    :param max_capacity: The maximum capacity any one database can consume.
    :type max_capacity: float
    """

    _attribute_map = {
        'min_capacity': {'key': 'minCapacity', 'type': 'float'},
        'max_capacity': {'key': 'maxCapacity', 'type': 'float'},
    }

    def __init__(self, **kwargs):
        super(ElasticPoolPerDatabaseSettings, self).__init__(**kwargs)
        self.min_capacity = kwargs.get('min_capacity', None)
        self.max_capacity = kwargs.get('max_capacity', None)
