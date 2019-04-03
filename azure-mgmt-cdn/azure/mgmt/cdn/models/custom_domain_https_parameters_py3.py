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


class CustomDomainHttpsParameters(Model):
    """The JSON object that contains the properties to secure a custom domain.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: CdnManagedHttpsParameters, UserManagedHttpsParameters

    All required parameters must be populated in order to send to Azure.

    :param protocol_type: Required. Defines the TLS extension protocol that is
     used for secure delivery. Possible values include: 'ServerNameIndication',
     'IPBased'
    :type protocol_type: str or ~azure.mgmt.cdn.models.ProtocolType
    :param certificate_source: Required. Constant filled by server.
    :type certificate_source: str
    """

    _validation = {
        'protocol_type': {'required': True},
        'certificate_source': {'required': True},
    }

    _attribute_map = {
        'protocol_type': {'key': 'protocolType', 'type': 'str'},
        'certificate_source': {'key': 'certificateSource', 'type': 'str'},
    }

    _subtype_map = {
        'certificate_source': {'Cdn': 'CdnManagedHttpsParameters', 'AzureKeyVault': 'UserManagedHttpsParameters'}
    }

    def __init__(self, *, protocol_type, **kwargs) -> None:
        super(CustomDomainHttpsParameters, self).__init__(**kwargs)
        self.protocol_type = protocol_type
        self.certificate_source = None
