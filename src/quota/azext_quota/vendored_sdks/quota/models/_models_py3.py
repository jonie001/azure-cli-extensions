# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._azure_quota_extension_api_enums import *


class commonresourceproperties(msrest.serialization.Model):
    """Resource properties.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type. Example: "Microsoft.Quota/quotas".
    :vartype type: str
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
    }

    def __init__(
        self,
        **kwargs
    ):
        super(commonresourceproperties, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class creategenericquotarequestparameters(msrest.serialization.Model):
    """Quota change requests information.

    :param value: Quota change requests.
    :type value: list[~azure_quota_extension_api.models.currentquotalimitbase]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[currentquotalimitbase]'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["currentquotalimitbase"]] = None,
        **kwargs
    ):
        super(creategenericquotarequestparameters, self).__init__(**kwargs)
        self.value = value


class currentquotalimitbase(msrest.serialization.Model):
    """Quota limit.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The resource ID.
    :vartype id: str
    :ivar type: The resource type.
    :vartype type: str
    :ivar name: The resource name.
    :vartype name: str
    :param properties: Quota properties for the specified resource, based on the API called, Quotas
     or Usages.
    :type properties: ~azure_quota_extension_api.models.quotaproperties
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'quotaproperties'},
    }

    def __init__(
        self,
        *,
        properties: Optional["quotaproperties"] = None,
        **kwargs
    ):
        super(currentquotalimitbase, self).__init__(**kwargs)
        self.id = None
        self.type = None
        self.name = None
        self.properties = properties


class currentusagesbase(msrest.serialization.Model):
    """Resource usage.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The resource ID.
    :vartype id: str
    :ivar type: The resource type.
    :vartype type: str
    :ivar name: The resource name.
    :vartype name: str
    :param properties: Usage properties for the specified resource.
    :type properties: ~azure_quota_extension_api.models.usagesproperties
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'usagesproperties'},
    }

    def __init__(
        self,
        *,
        properties: Optional["usagesproperties"] = None,
        **kwargs
    ):
        super(currentusagesbase, self).__init__(**kwargs)
        self.id = None
        self.type = None
        self.name = None
        self.properties = properties


class exceptionresponse(msrest.serialization.Model):
    """Error.

    :param error: API error details.
    :type error: ~azure_quota_extension_api.models.serviceerror
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'serviceerror'},
    }

    def __init__(
        self,
        *,
        error: Optional["serviceerror"] = None,
        **kwargs
    ):
        super(exceptionresponse, self).__init__(**kwargs)
        self.error = error


class limitjsonobject(msrest.serialization.Model):
    """LimitJson abstract class.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: limitobject.

    All required parameters must be populated in order to send to Azure.

    :param limit_object_type: Required. The limit object type.Constant filled by server.  Possible
     values include: "LimitValue".
    :type limit_object_type: str or ~azure_quota_extension_api.models.Limittype
    """

    _validation = {
        'limit_object_type': {'required': True},
    }

    _attribute_map = {
        'limit_object_type': {'key': 'limitObjectType', 'type': 'str'},
    }

    _subtype_map = {
        'limit_object_type': {'LimitValue': 'limitobject'}
    }

    def __init__(
        self,
        **kwargs
    ):
        super(limitjsonobject, self).__init__(**kwargs)
        self.limit_object_type = None  # type: Optional[str]


class limitobject(limitjsonobject):
    """The resource quota limit value.

    All required parameters must be populated in order to send to Azure.

    :param limit_object_type: Required. The limit object type.Constant filled by server.  Possible
     values include: "LimitValue".
    :type limit_object_type: str or ~azure_quota_extension_api.models.Limittype
    :param value: Required. The quota/limit value.
    :type value: int
    :param limit_type: The quota or usages limit types. Possible values include: "Independent",
     "Shared".
    :type limit_type: str or ~azure_quota_extension_api.models.Quotalimittypes
    """

    _validation = {
        'limit_object_type': {'required': True},
        'value': {'required': True},
    }

    _attribute_map = {
        'limit_object_type': {'key': 'limitObjectType', 'type': 'str'},
        'value': {'key': 'value', 'type': 'int'},
        'limit_type': {'key': 'limitType', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: int,
        limit_type: Optional[Union[str, "Quotalimittypes"]] = None,
        **kwargs
    ):
        super(limitobject, self).__init__(**kwargs)
        self.limit_object_type = 'LimitValue'  # type: str
        self.value = value
        self.limit_type = limit_type


class operationdisplay(msrest.serialization.Model):
    """operationdisplay.

    :param provider: Provider name.
    :type provider: str
    :param resource: Resource name.
    :type resource: str
    :param operation: Operation name.
    :type operation: str
    :param description: Operation description.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        provider: Optional[str] = None,
        resource: Optional[str] = None,
        operation: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs
    ):
        super(operationdisplay, self).__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description


class operationlist(msrest.serialization.Model):
    """operationlist.

    :param value:
    :type value: list[~azure_quota_extension_api.models.operationresponse]
    :param next_link: URL to get the next page of items.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[operationresponse]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["operationresponse"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(operationlist, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class operationresponse(msrest.serialization.Model):
    """operationresponse.

    :param name:
    :type name: str
    :param display:
    :type display: ~azure_quota_extension_api.models.operationdisplay
    :param origin:
    :type origin: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'operationdisplay'},
        'origin': {'key': 'origin', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        display: Optional["operationdisplay"] = None,
        origin: Optional[str] = None,
        **kwargs
    ):
        super(operationresponse, self).__init__(**kwargs)
        self.name = name
        self.display = display
        self.origin = origin


class quotalimits(msrest.serialization.Model):
    """Quota limits.

    :param value: List of quota limits.
    :type value: list[~azure_quota_extension_api.models.currentquotalimitbase]
    :param next_link: The URI used to fetch the next page of quota limits. When there are no more
     pages, this string is null.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[currentquotalimitbase]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["currentquotalimitbase"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(quotalimits, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class quotalimitsresponse(msrest.serialization.Model):
    """Quota limits request response.

    :param value: List of quota limits with the quota request status.
    :type value: list[~azure_quota_extension_api.models.currentquotalimitbase]
    :param next_link: The URI used to fetch the next page of quota limits. When there are no more
     pages, this is null.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[currentquotalimitbase]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["currentquotalimitbase"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(quotalimitsresponse, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class quotaproperties(msrest.serialization.Model):
    """Quota properties for the specified resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param limit: Resource quota limit properties.
    :type limit: ~azure_quota_extension_api.models.limitjsonobject
    :ivar unit: The quota units, such as Count and Bytes. When requesting quota, use the **unit**
     value returned in the GET response in the request body of your PUT operation.
    :vartype unit: str
    :param name: Resource name provided by the resource provider. Use this property name when
     requesting quota.
    :type name: ~azure_quota_extension_api.models.resourcename
    :param resource_type: Resource type name.
    :type resource_type: str
    :ivar quota_period: The time period over which the quota usage values are summarized. For
     example:
     *P1D (per one day)*\ PT1M (per one minute)
     *PT1S (per one second).
     This parameter is optional because, for some resources like compute, the period is irrelevant.
    :vartype quota_period: str
    :ivar is_quota_applicable: States if quota can be requested for this resource.
    :vartype is_quota_applicable: bool
    :param properties: Additional properties for the specific resource provider.
    :type properties: object
    """

    _validation = {
        'unit': {'readonly': True},
        'quota_period': {'readonly': True},
        'is_quota_applicable': {'readonly': True},
    }

    _attribute_map = {
        'limit': {'key': 'limit', 'type': 'limitjsonobject'},
        'unit': {'key': 'unit', 'type': 'str'},
        'name': {'key': 'name', 'type': 'resourcename'},
        'resource_type': {'key': 'resourceType', 'type': 'str'},
        'quota_period': {'key': 'quotaPeriod', 'type': 'str'},
        'is_quota_applicable': {'key': 'isQuotaApplicable', 'type': 'bool'},
        'properties': {'key': 'properties', 'type': 'object'},
    }

    def __init__(
        self,
        *,
        limit: Optional["limitjsonobject"] = None,
        name: Optional["resourcename"] = None,
        resource_type: Optional[str] = None,
        properties: Optional[object] = None,
        **kwargs
    ):
        super(quotaproperties, self).__init__(**kwargs)
        self.limit = limit
        self.unit = None
        self.name = name
        self.resource_type = resource_type
        self.quota_period = None
        self.is_quota_applicable = None
        self.properties = properties


class quotarequestdetails(msrest.serialization.Model):
    """List of quota requests with details.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Quota request ID.
    :vartype id: str
    :ivar name: Quota request name.
    :vartype name: str
    :ivar type: Resource type. "Microsoft.Quota/quotas".
    :vartype type: str
    :ivar provisioning_state: The quota request status. Possible values include: "Accepted",
     "Invalid", "Succeeded", "Failed", "InProgress".
    :vartype provisioning_state: str or ~azure_quota_extension_api.models.Quotarequeststate
    :ivar message: User-friendly status message.
    :vartype message: str
    :param error: Error details of the quota request.
    :type error: ~azure_quota_extension_api.models.serviceerrordetail
    :ivar request_submit_time: The quota request submission time. The date conforms to the
     following format specified by the ISO 8601 standard: yyyy-MM-ddTHH:mm:ssZ.
    :vartype request_submit_time: ~datetime.datetime
    :param value: Quota request details.
    :type value: list[~azure_quota_extension_api.models.subrequest]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'message': {'readonly': True},
        'request_submit_time': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'message': {'key': 'properties.message', 'type': 'str'},
        'error': {'key': 'properties.error', 'type': 'serviceerrordetail'},
        'request_submit_time': {'key': 'properties.requestSubmitTime', 'type': 'iso-8601'},
        'value': {'key': 'properties.value', 'type': '[subrequest]'},
    }

    def __init__(
        self,
        *,
        error: Optional["serviceerrordetail"] = None,
        value: Optional[List["subrequest"]] = None,
        **kwargs
    ):
        super(quotarequestdetails, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.provisioning_state = None
        self.message = None
        self.error = error
        self.request_submit_time = None
        self.value = value


class quotarequestdetailslist(msrest.serialization.Model):
    """Quota request information.

    :param value: Quota request details.
    :type value: list[~azure_quota_extension_api.models.quotarequestdetails]
    :param next_link: The URI for fetching the next page of quota limits. When there are no more
     pages, this string is null.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[quotarequestdetails]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["quotarequestdetails"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(quotarequestdetailslist, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class quotarequestoneresourcesubmitresponse(msrest.serialization.Model):
    """Quota request response.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Quota request ID.
    :vartype id: str
    :ivar name: The name of the quota request.
    :vartype name: str
    :ivar type: Resource type. "Microsoft.Quota/ServiceLimitRequests".
    :vartype type: str
    :ivar provisioning_state: Quota request status. Possible values include: "Accepted", "Invalid",
     "Succeeded", "Failed", "InProgress".
    :vartype provisioning_state: str or ~azure_quota_extension_api.models.Quotarequeststate
    :ivar message: User-friendly status message.
    :vartype message: str
    :ivar request_submit_time: Quota request submission time. The date conforms to the following
     ISO 8601 standard format: yyyy-MM-ddTHH:mm:ssZ.
    :vartype request_submit_time: ~datetime.datetime
    :param limit: Resource quota limit properties.
    :type limit: ~azure_quota_extension_api.models.limitobject
    :ivar current_value: Usage information for the current resource.
    :vartype current_value: int
    :param unit: The quota limit units, such as Count and Bytes. When requesting quota, use the
     **unit** value returned in the GET response in the request body of your PUT operation.
    :type unit: str
    :param name_properties_name: Resource name provided by the resource provider. Use this property
     name when requesting quota.
    :type name_properties_name: ~azure_quota_extension_api.models.resourcename
    :param resource_type: Resource type name.
    :type resource_type: str
    :ivar quota_period: The time period over which the quota usage values are summarized. For
     example:
     *P1D (per one day)*\ PT1M (per one minute)
     *PT1S (per one second).
     This parameter is optional because, for some resources like compute, the period is irrelevant.
    :vartype quota_period: str
    :ivar is_quota_applicable: States if quota can be requested for this resource.
    :vartype is_quota_applicable: bool
    :param error: Error details of the quota request.
    :type error: ~azure_quota_extension_api.models.serviceerrordetail
    :param properties: Additional properties for the specific resource provider.
    :type properties: object
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'message': {'readonly': True},
        'request_submit_time': {'readonly': True},
        'current_value': {'readonly': True},
        'quota_period': {'readonly': True},
        'is_quota_applicable': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'message': {'key': 'properties.message', 'type': 'str'},
        'request_submit_time': {'key': 'properties.requestSubmitTime', 'type': 'iso-8601'},
        'limit': {'key': 'properties.limit', 'type': 'limitobject'},
        'current_value': {'key': 'properties.currentValue', 'type': 'int'},
        'unit': {'key': 'properties.unit', 'type': 'str'},
        'name_properties_name': {'key': 'properties.name', 'type': 'resourcename'},
        'resource_type': {'key': 'properties.resourceType', 'type': 'str'},
        'quota_period': {'key': 'properties.quotaPeriod', 'type': 'str'},
        'is_quota_applicable': {'key': 'properties.isQuotaApplicable', 'type': 'bool'},
        'error': {'key': 'properties.error', 'type': 'serviceerrordetail'},
        'properties': {'key': 'properties.properties', 'type': 'object'},
    }

    def __init__(
        self,
        *,
        limit: Optional["limitobject"] = None,
        unit: Optional[str] = None,
        name_properties_name: Optional["resourcename"] = None,
        resource_type: Optional[str] = None,
        error: Optional["serviceerrordetail"] = None,
        properties: Optional[object] = None,
        **kwargs
    ):
        super(quotarequestoneresourcesubmitresponse, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.provisioning_state = None
        self.message = None
        self.request_submit_time = None
        self.limit = limit
        self.current_value = None
        self.unit = unit
        self.name_properties_name = name_properties_name
        self.resource_type = resource_type
        self.quota_period = None
        self.is_quota_applicable = None
        self.error = error
        self.properties = properties


class quotarequestproperties(msrest.serialization.Model):
    """Quota request properties.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar provisioning_state: The quota request status. Possible values include: "Accepted",
     "Invalid", "Succeeded", "Failed", "InProgress".
    :vartype provisioning_state: str or ~azure_quota_extension_api.models.Quotarequeststate
    :ivar message: User-friendly status message.
    :vartype message: str
    :param error: Error details of the quota request.
    :type error: ~azure_quota_extension_api.models.serviceerrordetail
    :ivar request_submit_time: The quota request submission time. The date conforms to the
     following format specified by the ISO 8601 standard: yyyy-MM-ddTHH:mm:ssZ.
    :vartype request_submit_time: ~datetime.datetime
    :param value: Quota request details.
    :type value: list[~azure_quota_extension_api.models.subrequest]
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'message': {'readonly': True},
        'request_submit_time': {'readonly': True},
    }

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'error': {'key': 'error', 'type': 'serviceerrordetail'},
        'request_submit_time': {'key': 'requestSubmitTime', 'type': 'iso-8601'},
        'value': {'key': 'value', 'type': '[subrequest]'},
    }

    def __init__(
        self,
        *,
        error: Optional["serviceerrordetail"] = None,
        value: Optional[List["subrequest"]] = None,
        **kwargs
    ):
        super(quotarequestproperties, self).__init__(**kwargs)
        self.provisioning_state = None
        self.message = None
        self.error = error
        self.request_submit_time = None
        self.value = value


class quotarequestsubmitresponse(msrest.serialization.Model):
    """Quota request response.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Quota request ID.
    :vartype id: str
    :ivar name: Quota request name.
    :vartype name: str
    :param properties: Quota request details.
    :type properties: ~azure_quota_extension_api.models.quotarequestproperties
    :ivar type: Resource type. "Microsoft.Quota/quotas".
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'quotarequestproperties'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        properties: Optional["quotarequestproperties"] = None,
        **kwargs
    ):
        super(quotarequestsubmitresponse, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.properties = properties
        self.type = None


class quotarequestsubmitresponse202(msrest.serialization.Model):
    """The quota request response with the quota request ID.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The quota request ID. To check the request status, use the **id** value in a `Quota
     Request Status <https://docs.microsoft.com/en-us/rest/api/reserved-vm-
     instances/quotarequeststatus/get>`_ GET operation.
    :vartype id: str
    :ivar name: Operation ID.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar provisioning_state: Quota request status. Possible values include: "Accepted", "Invalid",
     "Succeeded", "Failed", "InProgress".
    :vartype provisioning_state: str or ~azure_quota_extension_api.models.Quotarequeststate
    :ivar message: User-friendly message.
    :vartype message: str
    :param limit: Resource quota limit properties.
    :type limit: ~azure_quota_extension_api.models.limitobject
    :param unit: The quota limit units, such as Count and Bytes. When requesting quota, use the
     **unit** value returned in the GET response in the request body of your PUT operation.
    :type unit: str
    :param name_properties_name: Resource name provided by the resource provider. Use this property
     name when requesting quota.
    :type name_properties_name: ~azure_quota_extension_api.models.resourcename
    :param resource_type: Resource type name.
    :type resource_type: str
    :ivar quota_period: The time period over which the quota usage values are summarized. For
     example:
     *P1D (per one day)*\ PT1M (per one minute)
     *PT1S (per one second).
     This parameter is optional because, for some resources like compute, the period is irrelevant.
    :vartype quota_period: str
    :param properties: Additional properties for the specific resource provider.
    :type properties: object
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'message': {'readonly': True},
        'quota_period': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'message': {'key': 'properties.message', 'type': 'str'},
        'limit': {'key': 'properties.limit', 'type': 'limitobject'},
        'unit': {'key': 'properties.unit', 'type': 'str'},
        'name_properties_name': {'key': 'properties.name', 'type': 'resourcename'},
        'resource_type': {'key': 'properties.resourceType', 'type': 'str'},
        'quota_period': {'key': 'properties.quotaPeriod', 'type': 'str'},
        'properties': {'key': 'properties.properties', 'type': 'object'},
    }

    def __init__(
        self,
        *,
        limit: Optional["limitobject"] = None,
        unit: Optional[str] = None,
        name_properties_name: Optional["resourcename"] = None,
        resource_type: Optional[str] = None,
        properties: Optional[object] = None,
        **kwargs
    ):
        super(quotarequestsubmitresponse202, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.provisioning_state = None
        self.message = None
        self.limit = limit
        self.unit = unit
        self.name_properties_name = name_properties_name
        self.resource_type = resource_type
        self.quota_period = None
        self.properties = properties


class resourcename(msrest.serialization.Model):
    """Name of the resource provided by the resource Provider. When requesting quota, use this property name.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param value: Resource name.
    :type value: str
    :ivar localized_value: Resource display name.
    :vartype localized_value: str
    """

    _validation = {
        'localized_value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
        'localized_value': {'key': 'localizedValue', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[str] = None,
        **kwargs
    ):
        super(resourcename, self).__init__(**kwargs)
        self.value = value
        self.localized_value = None


class serviceerror(msrest.serialization.Model):
    """API error details.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param code: Error code.
    :type code: str
    :param message: Error message.
    :type message: str
    :ivar details: List of error details.
    :vartype details: list[~azure_quota_extension_api.models.serviceerrordetail]
    """

    _validation = {
        'details': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': '[serviceerrordetail]'},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        message: Optional[str] = None,
        **kwargs
    ):
        super(serviceerror, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.details = None


class serviceerrordetail(msrest.serialization.Model):
    """Error details.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: Error code.
    :vartype code: str
    :ivar message: Error message.
    :vartype message: str
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(serviceerrordetail, self).__init__(**kwargs)
        self.code = None
        self.message = None


class subrequest(msrest.serialization.Model):
    """Request property.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param name: Resource name.
    :type name: ~azure_quota_extension_api.models.resourcename
    :ivar resource_type: Resource type for which the quota properties were requested.
    :vartype resource_type: str
    :param unit: Quota limit units, such as Count and Bytes. When requesting quota, use the
     **unit** value returned in the GET response in the request body of your PUT operation.
    :type unit: str
    :ivar provisioning_state: The quota request status. Possible values include: "Accepted",
     "Invalid", "Succeeded", "Failed", "InProgress".
    :vartype provisioning_state: str or ~azure_quota_extension_api.models.Quotarequeststate
    :ivar message: User-friendly status message.
    :vartype message: str
    :ivar sub_request_id: Quota request ID.
    :vartype sub_request_id: str
    :param limit: Resource quota limit properties.
    :type limit: ~azure_quota_extension_api.models.limitjsonobject
    """

    _validation = {
        'resource_type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'message': {'readonly': True},
        'sub_request_id': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'resourcename'},
        'resource_type': {'key': 'resourceType', 'type': 'str'},
        'unit': {'key': 'unit', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'sub_request_id': {'key': 'subRequestId', 'type': 'str'},
        'limit': {'key': 'limit', 'type': 'limitjsonobject'},
    }

    def __init__(
        self,
        *,
        name: Optional["resourcename"] = None,
        unit: Optional[str] = None,
        limit: Optional["limitjsonobject"] = None,
        **kwargs
    ):
        super(subrequest, self).__init__(**kwargs)
        self.name = name
        self.resource_type = None
        self.unit = unit
        self.provisioning_state = None
        self.message = None
        self.sub_request_id = None
        self.limit = limit


class usageslimits(msrest.serialization.Model):
    """Quota limits.

    :param value: List of quota limits.
    :type value: list[~azure_quota_extension_api.models.currentusagesbase]
    :param next_link: The URI used to fetch the next page of quota limits. When there are no more
     pages, this is null.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[currentusagesbase]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["currentusagesbase"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(usageslimits, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class usagesobject(msrest.serialization.Model):
    """The resource usages value.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. The usages value.
    :type value: int
    :param usages_type: The quota or usages limit types. Possible values include: "Individual",
     "Combined".
    :type usages_type: str or ~azure_quota_extension_api.models.Usagestypes
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'int'},
        'usages_type': {'key': 'usagesType', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: int,
        usages_type: Optional[Union[str, "Usagestypes"]] = None,
        **kwargs
    ):
        super(usagesobject, self).__init__(**kwargs)
        self.value = value
        self.usages_type = usages_type


class usagesproperties(msrest.serialization.Model):
    """Usage properties for the specified resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param usages: The quota limit properties for this resource.
    :type usages: ~azure_quota_extension_api.models.usagesobject
    :ivar unit: The units for the quota usage, such as Count and Bytes. When requesting quota, use
     the **unit** value returned in the GET response in the request body of your PUT operation.
    :vartype unit: str
    :param name: Resource name provided by the resource provider. Use this property name when
     requesting quota.
    :type name: ~azure_quota_extension_api.models.resourcename
    :param resource_type: The name of the resource type.
    :type resource_type: str
    :ivar quota_period: The time period for the summary of the quota usage values. For example:
     *P1D (per one day)*\ PT1M (per one minute)
     *PT1S (per one second).
     This parameter is optional because it is not relevant for all resources such as compute.
    :vartype quota_period: str
    :ivar is_quota_applicable: States if quota can be requested for this resource.
    :vartype is_quota_applicable: bool
    :param properties: Additional properties for the specific resource provider.
    :type properties: object
    """

    _validation = {
        'unit': {'readonly': True},
        'quota_period': {'readonly': True},
        'is_quota_applicable': {'readonly': True},
    }

    _attribute_map = {
        'usages': {'key': 'usages', 'type': 'usagesobject'},
        'unit': {'key': 'unit', 'type': 'str'},
        'name': {'key': 'name', 'type': 'resourcename'},
        'resource_type': {'key': 'resourceType', 'type': 'str'},
        'quota_period': {'key': 'quotaPeriod', 'type': 'str'},
        'is_quota_applicable': {'key': 'isQuotaApplicable', 'type': 'bool'},
        'properties': {'key': 'properties', 'type': 'object'},
    }

    def __init__(
        self,
        *,
        usages: Optional["usagesobject"] = None,
        name: Optional["resourcename"] = None,
        resource_type: Optional[str] = None,
        properties: Optional[object] = None,
        **kwargs
    ):
        super(usagesproperties, self).__init__(**kwargs)
        self.usages = usages
        self.unit = None
        self.name = name
        self.resource_type = resource_type
        self.quota_period = None
        self.is_quota_applicable = None
        self.properties = properties
