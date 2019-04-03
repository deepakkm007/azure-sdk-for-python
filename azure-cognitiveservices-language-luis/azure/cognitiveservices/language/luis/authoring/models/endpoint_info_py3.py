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


class EndpointInfo(Model):
    """The base class "ProductionOrStagingEndpointInfo" inherits from.

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

    def __init__(self, *, version_id: str=None, is_staging: bool=None, endpoint_url: str=None, region: str=None, assigned_endpoint_key: str=None, endpoint_region: str=None, published_date_time: str=None, **kwargs) -> None:
        super(EndpointInfo, self).__init__(**kwargs)
        self.version_id = version_id
        self.is_staging = is_staging
        self.endpoint_url = endpoint_url
        self.region = region
        self.assigned_endpoint_key = assigned_endpoint_key
        self.endpoint_region = endpoint_region
        self.published_date_time = published_date_time
