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

from .proxy_only_resource import ProxyOnlyResource


class MigrateMySqlRequest(ProxyOnlyResource):
    """MySQL migration request.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :param connection_string: Required. Connection string to the remote MySQL
     database.
    :type connection_string: str
    :param migration_type: Required. The type of migration operation to be
     done. Possible values include: 'LocalToRemote', 'RemoteToLocal'
    :type migration_type: str or ~azure.mgmt.web.models.MySqlMigrationType
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'connection_string': {'required': True},
        'migration_type': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'connection_string': {'key': 'properties.connectionString', 'type': 'str'},
        'migration_type': {'key': 'properties.migrationType', 'type': 'MySqlMigrationType'},
    }

    def __init__(self, **kwargs):
        super(MigrateMySqlRequest, self).__init__(**kwargs)
        self.connection_string = kwargs.get('connection_string', None)
        self.migration_type = kwargs.get('migration_type', None)
