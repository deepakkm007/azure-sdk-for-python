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

from .tracked_resource_py3 import TrackedResource


class Endpoint(TrackedResource):
    """CDN endpoint is the entity within a CDN profile containing configuration
    information such as origin, protocol, content caching and delivery
    behavior. The CDN endpoint uses the URL format
    <endpointname>.azureedge.net.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Required. Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param origin_host_header: The host header value sent to the origin with
     each request. If you leave this blank, the request hostname determines
     this value. Azure CDN origins, such as Web Apps, Blob Storage, and Cloud
     Services require this host header value to match the origin hostname by
     default.
    :type origin_host_header: str
    :param origin_path: A directory path on the origin that CDN can use to
     retrieve content from, e.g. contoso.cloudapp.net/originpath.
    :type origin_path: str
    :param content_types_to_compress: List of content types on which
     compression applies. The value should be a valid MIME type.
    :type content_types_to_compress: list[str]
    :param is_compression_enabled: Indicates whether content compression is
     enabled on CDN. Default value is false. If compression is enabled, content
     will be served as compressed if user requests for a compressed version.
     Content won't be compressed on CDN when requested content is smaller than
     1 byte or larger than 1 MB.
    :type is_compression_enabled: bool
    :param is_http_allowed: Indicates whether HTTP traffic is allowed on the
     endpoint. Default value is true. At least one protocol (HTTP or HTTPS)
     must be allowed.
    :type is_http_allowed: bool
    :param is_https_allowed: Indicates whether HTTPS traffic is allowed on the
     endpoint. Default value is true. At least one protocol (HTTP or HTTPS)
     must be allowed.
    :type is_https_allowed: bool
    :param query_string_caching_behavior: Defines how CDN caches requests that
     include query strings. You can ignore any query strings when caching,
     bypass caching to prevent requests that contain query strings from being
     cached, or cache every request with a unique URL. Possible values include:
     'IgnoreQueryString', 'BypassCaching', 'UseQueryString', 'NotSet'
    :type query_string_caching_behavior: str or
     ~azure.mgmt.cdn.models.QueryStringCachingBehavior
    :param optimization_type: Specifies what scenario the customer wants this
     CDN endpoint to optimize for, e.g. Download, Media services. With this
     information, CDN can apply scenario driven optimization. Possible values
     include: 'GeneralWebDelivery', 'GeneralMediaStreaming',
     'VideoOnDemandMediaStreaming', 'LargeFileDownload',
     'DynamicSiteAcceleration'
    :type optimization_type: str or ~azure.mgmt.cdn.models.OptimizationType
    :param probe_path: Path to a file hosted on the origin which helps
     accelerate delivery of the dynamic content and calculate the most optimal
     routes for the CDN. This is relative to the origin path.
    :type probe_path: str
    :param geo_filters: List of rules defining the user's geo access within a
     CDN endpoint. Each geo filter defines an access rule to a specified path
     or content, e.g. block APAC for path /pictures/
    :type geo_filters: list[~azure.mgmt.cdn.models.GeoFilter]
    :param delivery_policy: A policy that specifies the delivery rules to be
     used for an endpoint.
    :type delivery_policy:
     ~azure.mgmt.cdn.models.EndpointPropertiesUpdateParametersDeliveryPolicy
    :ivar host_name: The host name of the endpoint structured as
     {endpointName}.{DNSZone}, e.g. contoso.azureedge.net
    :vartype host_name: str
    :param origins: Required. The source of the content being delivered via
     CDN.
    :type origins: list[~azure.mgmt.cdn.models.DeepCreatedOrigin]
    :ivar resource_state: Resource status of the endpoint. Possible values
     include: 'Creating', 'Deleting', 'Running', 'Starting', 'Stopped',
     'Stopping'
    :vartype resource_state: str or
     ~azure.mgmt.cdn.models.EndpointResourceState
    :ivar provisioning_state: Provisioning status of the endpoint.
    :vartype provisioning_state: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'host_name': {'readonly': True},
        'origins': {'required': True},
        'resource_state': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'origin_host_header': {'key': 'properties.originHostHeader', 'type': 'str'},
        'origin_path': {'key': 'properties.originPath', 'type': 'str'},
        'content_types_to_compress': {'key': 'properties.contentTypesToCompress', 'type': '[str]'},
        'is_compression_enabled': {'key': 'properties.isCompressionEnabled', 'type': 'bool'},
        'is_http_allowed': {'key': 'properties.isHttpAllowed', 'type': 'bool'},
        'is_https_allowed': {'key': 'properties.isHttpsAllowed', 'type': 'bool'},
        'query_string_caching_behavior': {'key': 'properties.queryStringCachingBehavior', 'type': 'QueryStringCachingBehavior'},
        'optimization_type': {'key': 'properties.optimizationType', 'type': 'str'},
        'probe_path': {'key': 'properties.probePath', 'type': 'str'},
        'geo_filters': {'key': 'properties.geoFilters', 'type': '[GeoFilter]'},
        'delivery_policy': {'key': 'properties.deliveryPolicy', 'type': 'EndpointPropertiesUpdateParametersDeliveryPolicy'},
        'host_name': {'key': 'properties.hostName', 'type': 'str'},
        'origins': {'key': 'properties.origins', 'type': '[DeepCreatedOrigin]'},
        'resource_state': {'key': 'properties.resourceState', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, *, location: str, origins, tags=None, origin_host_header: str=None, origin_path: str=None, content_types_to_compress=None, is_compression_enabled: bool=None, is_http_allowed: bool=None, is_https_allowed: bool=None, query_string_caching_behavior=None, optimization_type=None, probe_path: str=None, geo_filters=None, delivery_policy=None, **kwargs) -> None:
        super(Endpoint, self).__init__(location=location, tags=tags, **kwargs)
        self.origin_host_header = origin_host_header
        self.origin_path = origin_path
        self.content_types_to_compress = content_types_to_compress
        self.is_compression_enabled = is_compression_enabled
        self.is_http_allowed = is_http_allowed
        self.is_https_allowed = is_https_allowed
        self.query_string_caching_behavior = query_string_caching_behavior
        self.optimization_type = optimization_type
        self.probe_path = probe_path
        self.geo_filters = geo_filters
        self.delivery_policy = delivery_policy
        self.host_name = None
        self.origins = origins
        self.resource_state = None
        self.provisioning_state = None
