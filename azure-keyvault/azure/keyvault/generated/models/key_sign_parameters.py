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


class KeySignParameters(Model):
    """The key operations parameters.

    :param algorithm: The signing/verification algorithm identifier. For more
     information on possible algorithm types, see
     JsonWebKeySignatureAlgorithm. Possible values include: 'RS256', 'RS384',
     'RS512', 'RSNULL'
    :type algorithm: str or :class:`JsonWebKeySignatureAlgorithm
     <azure.keyvault.generated.models.JsonWebKeySignatureAlgorithm>`
    :param value:
    :type value: bytes
    """ 

    _validation = {
        'algorithm': {'required': True, 'min_length': 1},
        'value': {'required': True},
    }

    _attribute_map = {
        'algorithm': {'key': 'alg', 'type': 'str'},
        'value': {'key': 'value', 'type': 'base64'},
    }

    def __init__(self, algorithm, value):
        self.algorithm = algorithm
        self.value = value
