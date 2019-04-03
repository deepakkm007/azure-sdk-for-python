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

from .proxy_resource_py3 import ProxyResource


class ImportExportResponse(ProxyResource):
    """Response for Import/Export Get operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar request_type: The request type of the operation.
    :vartype request_type: str
    :ivar request_id: The request type of the operation.
    :vartype request_id: str
    :ivar server_name: The name of the server.
    :vartype server_name: str
    :ivar database_name: The name of the database.
    :vartype database_name: str
    :ivar status: The status message returned from the server.
    :vartype status: str
    :ivar last_modified_time: The operation status last modified time.
    :vartype last_modified_time: str
    :ivar queued_time: The operation queued time.
    :vartype queued_time: str
    :ivar blob_uri: The blob uri.
    :vartype blob_uri: str
    :ivar error_message: The error message returned from the server.
    :vartype error_message: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'request_type': {'readonly': True},
        'request_id': {'readonly': True},
        'server_name': {'readonly': True},
        'database_name': {'readonly': True},
        'status': {'readonly': True},
        'last_modified_time': {'readonly': True},
        'queued_time': {'readonly': True},
        'blob_uri': {'readonly': True},
        'error_message': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'request_type': {'key': 'properties.requestType', 'type': 'str'},
        'request_id': {'key': 'properties.requestId', 'type': 'str'},
        'server_name': {'key': 'properties.serverName', 'type': 'str'},
        'database_name': {'key': 'properties.databaseName', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'last_modified_time': {'key': 'properties.lastModifiedTime', 'type': 'str'},
        'queued_time': {'key': 'properties.queuedTime', 'type': 'str'},
        'blob_uri': {'key': 'properties.blobUri', 'type': 'str'},
        'error_message': {'key': 'properties.errorMessage', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(ImportExportResponse, self).__init__(**kwargs)
        self.request_type = None
        self.request_id = None
        self.server_name = None
        self.database_name = None
        self.status = None
        self.last_modified_time = None
        self.queued_time = None
        self.blob_uri = None
        self.error_message = None
