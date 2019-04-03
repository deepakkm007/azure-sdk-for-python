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
from msrest.exceptions import HttpOperationError


class ErrorDetails(Model):
    """Error details.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar http_status_code: The HTTP status code.
    :vartype http_status_code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar details: The error details.
    :vartype details: str
    """

    _validation = {
        'code': {'readonly': True},
        'http_status_code': {'readonly': True},
        'message': {'readonly': True},
        'details': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'http_status_code': {'key': 'httpStatusCode', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(ErrorDetails, self).__init__(**kwargs)
        self.code = None
        self.http_status_code = None
        self.message = None
        self.details = None


class ErrorDetailsException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorDetails'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorDetailsException, self).__init__(deserialize, response, 'ErrorDetails', *args)
