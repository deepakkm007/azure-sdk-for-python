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


class CertificateImportParameters(Model):
    """The certificate import parameters.

    :param base64_encoded_certificate: Base64 encoded representation of the
     certificate object to import. This certificate needs to contain the
     private key.
    :type base64_encoded_certificate: str
    :param password: If the private key in base64EncodedCertificate is
     encrypted, the password used for encryption
    :type password: str
    :param certificate_policy: The management policy for the certificate
    :type certificate_policy: :class:`CertificatePolicy
     <azure.keyvault.generated.models.CertificatePolicy>`
    :param certificate_attributes: The attributes of the certificate
     (optional)
    :type certificate_attributes: :class:`CertificateAttributes
     <azure.keyvault.generated.models.CertificateAttributes>`
    :param tags: Application-specific metadata in the form of key-value pairs
    :type tags: dict
    """ 

    _validation = {
        'base64_encoded_certificate': {'required': True},
    }

    _attribute_map = {
        'base64_encoded_certificate': {'key': 'value', 'type': 'str'},
        'password': {'key': 'pwd', 'type': 'str'},
        'certificate_policy': {'key': 'policy', 'type': 'CertificatePolicy'},
        'certificate_attributes': {'key': 'attributes', 'type': 'CertificateAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, base64_encoded_certificate, password=None, certificate_policy=None, certificate_attributes=None, tags=None):
        self.base64_encoded_certificate = base64_encoded_certificate
        self.password = password
        self.certificate_policy = certificate_policy
        self.certificate_attributes = certificate_attributes
        self.tags = tags
