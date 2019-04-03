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


class GetSsisObjectMetadataRequest(Model):
    """The request payload of get SSIS object metadata.

    :param metadata_path: Metadata path.
    :type metadata_path: str
    """

    _attribute_map = {
        'metadata_path': {'key': 'metadataPath', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(GetSsisObjectMetadataRequest, self).__init__(**kwargs)
        self.metadata_path = kwargs.get('metadata_path', None)
