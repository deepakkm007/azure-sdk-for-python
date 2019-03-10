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


class Alert(Resource):
    """Security alert.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :ivar state: State of the alert (Active, Dismissed etc.)
    :vartype state: str
    :ivar reported_time_utc: The time the incident was reported to
     Microsoft.Security in UTC
    :vartype reported_time_utc: datetime
    :ivar vendor_name: Name of the vendor that discovered the incident
    :vartype vendor_name: str
    :ivar alert_name: Name of the alert type
    :vartype alert_name: str
    :ivar alert_display_name: Display name of the alert type
    :vartype alert_display_name: str
    :ivar detected_time_utc: The time the incident was detected by the vendor
    :vartype detected_time_utc: datetime
    :ivar description: Description of the incident and what it means
    :vartype description: str
    :ivar remediation_steps: Recommended steps to reradiate the incident
    :vartype remediation_steps: str
    :ivar action_taken: The action that was taken as a response to the alert
     (Active, Blocked etc.)
    :vartype action_taken: str
    :ivar reported_severity: Estimated severity of this alert. Possible values
     include: 'Informational', 'Low', 'Medium', 'High'
    :vartype reported_severity: str or
     ~azure.mgmt.security.models.ReportedSeverity
    :ivar compromised_entity: The entity that the incident happened on
    :vartype compromised_entity: str
    :ivar associated_resource: Azure resource ID of the associated resource
    :vartype associated_resource: str
    :param extended_properties:
    :type extended_properties: dict[str, object]
    :ivar system_source: The type of the alerted resource (Azure, Non-Azure)
    :vartype system_source: str
    :ivar can_be_investigated: Whether this alert can be investigated with
     Azure Security Center
    :vartype can_be_investigated: bool
    :ivar is_incident: Whether this alert is for incident type or not
     (otherwise - single alert)
    :vartype is_incident: bool
    :param entities: objects that are related to this alerts
    :type entities: list[~azure.mgmt.security.models.AlertEntity]
    :ivar confidence_score: level of confidence we have on the alert
    :vartype confidence_score: float
    :param confidence_reasons: reasons the alert got the confidenceScore value
    :type confidence_reasons:
     list[~azure.mgmt.security.models.AlertConfidenceReason]
    :ivar subscription_id: Azure subscription ID of the resource that had the
     security alert or the subscription ID of the workspace that this resource
     reports to
    :vartype subscription_id: str
    :ivar instance_id: Instance ID of the alert.
    :vartype instance_id: str
    :ivar workspace_arm_id: Azure resource ID of the workspace that the alert
     was reported to.
    :vartype workspace_arm_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'state': {'readonly': True},
        'reported_time_utc': {'readonly': True},
        'vendor_name': {'readonly': True},
        'alert_name': {'readonly': True},
        'alert_display_name': {'readonly': True},
        'detected_time_utc': {'readonly': True},
        'description': {'readonly': True},
        'remediation_steps': {'readonly': True},
        'action_taken': {'readonly': True},
        'reported_severity': {'readonly': True},
        'compromised_entity': {'readonly': True},
        'associated_resource': {'readonly': True},
        'system_source': {'readonly': True},
        'can_be_investigated': {'readonly': True},
        'is_incident': {'readonly': True},
        'confidence_score': {'readonly': True, 'maximum': 1, 'minimum': 0},
        'subscription_id': {'readonly': True},
        'instance_id': {'readonly': True},
        'workspace_arm_id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'state': {'key': 'properties.state', 'type': 'str'},
        'reported_time_utc': {'key': 'properties.reportedTimeUtc', 'type': 'iso-8601'},
        'vendor_name': {'key': 'properties.vendorName', 'type': 'str'},
        'alert_name': {'key': 'properties.alertName', 'type': 'str'},
        'alert_display_name': {'key': 'properties.alertDisplayName', 'type': 'str'},
        'detected_time_utc': {'key': 'properties.detectedTimeUtc', 'type': 'iso-8601'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'remediation_steps': {'key': 'properties.remediationSteps', 'type': 'str'},
        'action_taken': {'key': 'properties.actionTaken', 'type': 'str'},
        'reported_severity': {'key': 'properties.reportedSeverity', 'type': 'str'},
        'compromised_entity': {'key': 'properties.compromisedEntity', 'type': 'str'},
        'associated_resource': {'key': 'properties.associatedResource', 'type': 'str'},
        'extended_properties': {'key': 'properties.extendedProperties', 'type': '{object}'},
        'system_source': {'key': 'properties.systemSource', 'type': 'str'},
        'can_be_investigated': {'key': 'properties.canBeInvestigated', 'type': 'bool'},
        'is_incident': {'key': 'properties.isIncident', 'type': 'bool'},
        'entities': {'key': 'properties.entities', 'type': '[AlertEntity]'},
        'confidence_score': {'key': 'properties.confidenceScore', 'type': 'float'},
        'confidence_reasons': {'key': 'properties.confidenceReasons', 'type': '[AlertConfidenceReason]'},
        'subscription_id': {'key': 'properties.subscriptionId', 'type': 'str'},
        'instance_id': {'key': 'properties.instanceId', 'type': 'str'},
        'workspace_arm_id': {'key': 'properties.workspaceArmId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Alert, self).__init__(**kwargs)
        self.state = None
        self.reported_time_utc = None
        self.vendor_name = None
        self.alert_name = None
        self.alert_display_name = None
        self.detected_time_utc = None
        self.description = None
        self.remediation_steps = None
        self.action_taken = None
        self.reported_severity = None
        self.compromised_entity = None
        self.associated_resource = None
        self.extended_properties = kwargs.get('extended_properties', None)
        self.system_source = None
        self.can_be_investigated = None
        self.is_incident = None
        self.entities = kwargs.get('entities', None)
        self.confidence_score = None
        self.confidence_reasons = kwargs.get('confidence_reasons', None)
        self.subscription_id = None
        self.instance_id = None
        self.workspace_arm_id = None
