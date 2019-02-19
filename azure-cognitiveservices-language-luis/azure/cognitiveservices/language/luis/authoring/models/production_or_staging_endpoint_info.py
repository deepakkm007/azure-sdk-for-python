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

from .endpoint_info import EndpointInfo


class ProductionOrStagingEndpointInfo(EndpointInfo):
    """ProductionOrStagingEndpointInfo.

    :param version_id: The version ID to publish.
    :type version_id: str
    :param is_staging: Indicates if the staging slot should be used, instead
     of the Production one.
    :type is_staging: bool
    :param endpoint_url: The Runtime endpoint URL for this model version.
    :type endpoint_url: str
    :param region: The target region that the application is published to.
    :type region: str
    :param assigned_endpoint_key: The endpoint key.
    :type assigned_endpoint_key: str
    :param endpoint_region: The endpoint's region.
    :type endpoint_region: str
    :param published_date_time: Timestamp when was last published.
    :type published_date_time: str
    """

    _attribute_map = {
        'version_id': {'key': 'versionId', 'type': 'str'},
        'is_staging': {'key': 'isStaging', 'type': 'bool'},
        'endpoint_url': {'key': 'endpointUrl', 'type': 'str'},
        'region': {'key': 'region', 'type': 'str'},
        'assigned_endpoint_key': {'key': 'assignedEndpointKey', 'type': 'str'},
        'endpoint_region': {'key': 'endpointRegion', 'type': 'str'},
        'published_date_time': {'key': 'publishedDateTime', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ProductionOrStagingEndpointInfo, self).__init__(**kwargs)
