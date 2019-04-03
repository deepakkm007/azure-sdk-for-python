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

from .resource import Resource


class AgreementTerms(Resource):
    """Terms properties for provided Publisher/Offer/Plan tuple.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param publisher: Publisher identifier string of image being deployed.
    :type publisher: str
    :param product: Offer identifier string of image being deployed.
    :type product: str
    :param plan: Plan identifier string of image being deployed.
    :type plan: str
    :param license_text_link: Link to HTML with Microsoft and Publisher terms.
    :type license_text_link: str
    :param privacy_policy_link: Link to the privacy policy of the publisher.
    :type privacy_policy_link: str
    :param retrieve_datetime: Date and time in UTC of when the terms were
     accepted. This is empty if Accepted is false.
    :type retrieve_datetime: str
    :param signature: Terms signature.
    :type signature: str
    :param accepted: If any version of the terms have been accepted, otherwise
     false.
    :type accepted: bool
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'publisher': {'key': 'properties.publisher', 'type': 'str'},
        'product': {'key': 'properties.product', 'type': 'str'},
        'plan': {'key': 'properties.plan', 'type': 'str'},
        'license_text_link': {'key': 'properties.licenseTextLink', 'type': 'str'},
        'privacy_policy_link': {'key': 'properties.privacyPolicyLink', 'type': 'str'},
        'retrieve_datetime': {'key': 'properties.retrieveDatetime', 'type': 'str'},
        'signature': {'key': 'properties.signature', 'type': 'str'},
        'accepted': {'key': 'properties.accepted', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(AgreementTerms, self).__init__(**kwargs)
        self.publisher = kwargs.get('publisher', None)
        self.product = kwargs.get('product', None)
        self.plan = kwargs.get('plan', None)
        self.license_text_link = kwargs.get('license_text_link', None)
        self.privacy_policy_link = kwargs.get('privacy_policy_link', None)
        self.retrieve_datetime = kwargs.get('retrieve_datetime', None)
        self.signature = kwargs.get('signature', None)
        self.accepted = kwargs.get('accepted', None)
