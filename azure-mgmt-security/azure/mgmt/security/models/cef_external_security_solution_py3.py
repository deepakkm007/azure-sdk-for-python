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

from .external_security_solution_py3 import ExternalSecuritySolution


class CefExternalSecuritySolution(ExternalSecuritySolution):
    """Represents a security solution which sends CEF logs to an OMS workspace.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :ivar location: Location where the resource is stored
    :vartype location: str
    :param kind: Required. Constant filled by server.
    :type kind: str
    :param properties:
    :type properties: ~azure.mgmt.security.models.CefSolutionProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'readonly': True},
        'kind': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'CefSolutionProperties'},
    }

    def __init__(self, *, properties=None, **kwargs) -> None:
        super(CefExternalSecuritySolution, self).__init__(**kwargs)
        self.properties = properties
        self.kind = 'CEF'
