# coding: utf-8

"""
    OmniCore Model and State Management API

    This is an OmniCore Model and State Management server.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@korewireless.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, constr
from OmniCore.models.device_config import DeviceConfig
from OmniCore.models.device_credential import DeviceCredential
from OmniCore.models.device_state import DeviceState
from OmniCore.models.error_status import ErrorStatus
from OmniCore.models.gateway_config import GatewayConfig
from OmniCore.models.log_level import LogLevel

class Device(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: constr(strict=True, max_length=256, min_length=3) = ...
    name: Optional[StrictStr] = None
    num_id: Optional[StrictStr] = Field(None, alias="numId")
    parent: StrictStr = ...
    registry: StrictStr = ...
    blocked: Optional[StrictBool] = None
    capresent: Optional[StrictBool] = None
    subscription: StrictStr = ...
    created_on: Optional[StrictStr] = Field(None, alias="createdOn")
    updated_on: Optional[StrictStr] = Field(None, alias="updatedOn")
    credentials: Optional[List[DeviceCredential]] = None
    gateway: Optional[List[StrictStr]] = None
    gateway_config: Optional[GatewayConfig] = Field(None, alias="gatewayConfig")
    is_gateway: Optional[StrictBool] = Field(None, alias="isGateway")
    device_errors: Optional[StrictStr] = Field(None, alias="deviceErrors")
    client_online: Optional[StrictBool] = Field(None, alias="clientOnline")
    last_config_ack_time: Optional[StrictStr] = Field(None, alias="lastConfigAckTime")
    last_config_send_time: Optional[StrictStr] = Field(None, alias="lastConfigSendTime")
    last_error_status: Optional[ErrorStatus] = Field(None, alias="lastErrorStatus")
    last_error_time: Optional[StrictStr] = Field(None, alias="lastErrorTime")
    last_event_time: Optional[StrictStr] = Field(None, alias="lastEventTime")
    last_heartbeat_time: Optional[StrictStr] = Field(None, alias="lastHeartbeatTime")
    last_state_time: Optional[StrictStr] = Field(None, alias="lastStateTime")
    log_level: Optional[LogLevel] = Field(None, alias="logLevel")
    metadata: Optional[Dict[str, StrictStr]] = None
    config: Optional[DeviceConfig] = None
    state: Optional[DeviceState] = None
    subscriptions: Optional[List[StrictStr]] = None
    __properties = ["id", "name", "numId", "parent", "registry", "blocked", "capresent", "subscription", "createdOn", "updatedOn", "credentials", "gateway", "gatewayConfig", "isGateway", "deviceErrors", "clientOnline", "lastConfigAckTime", "lastConfigSendTime", "lastErrorStatus", "lastErrorTime", "lastEventTime", "lastHeartbeatTime", "lastStateTime", "logLevel", "metadata", "config", "state", "subscriptions"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Device:
        """Create an instance of Device from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in credentials (list)
        _items = []
        if self.credentials:
            for _item in self.credentials:
                if _item:
                    _items.append(_item.to_dict())
            _dict['credentials'] = _items
        # override the default output from pydantic by calling `to_dict()` of gateway_config
        if self.gateway_config:
            _dict['gatewayConfig'] = self.gateway_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_error_status
        if self.last_error_status:
            _dict['lastErrorStatus'] = self.last_error_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of config
        if self.config:
            _dict['config'] = self.config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of state
        if self.state:
            _dict['state'] = self.state.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Device:
        """Create an instance of Device from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Device.parse_obj(obj)

        _obj = Device.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "num_id": obj.get("numId"),
            "parent": obj.get("parent"),
            "registry": obj.get("registry"),
            "blocked": obj.get("blocked"),
            "capresent": obj.get("capresent"),
            "subscription": obj.get("subscription"),
            "created_on": obj.get("createdOn"),
            "updated_on": obj.get("updatedOn"),
            "credentials": [DeviceCredential.from_dict(_item) for _item in obj.get("credentials")] if obj.get("credentials") is not None else None,
            "gateway": obj.get("gateway"),
            "gateway_config": GatewayConfig.from_dict(obj.get("gatewayConfig")) if obj.get("gatewayConfig") is not None else None,
            "is_gateway": obj.get("isGateway"),
            "device_errors": obj.get("deviceErrors"),
            "client_online": obj.get("clientOnline"),
            "last_config_ack_time": obj.get("lastConfigAckTime"),
            "last_config_send_time": obj.get("lastConfigSendTime"),
            "last_error_status": ErrorStatus.from_dict(obj.get("lastErrorStatus")) if obj.get("lastErrorStatus") is not None else None,
            "last_error_time": obj.get("lastErrorTime"),
            "last_event_time": obj.get("lastEventTime"),
            "last_heartbeat_time": obj.get("lastHeartbeatTime"),
            "last_state_time": obj.get("lastStateTime"),
            "log_level": obj.get("logLevel"),
            "metadata": obj.get("metadata"),
            "config": DeviceConfig.from_dict(obj.get("config")) if obj.get("config") is not None else None,
            "state": DeviceState.from_dict(obj.get("state")) if obj.get("state") is not None else None,
            "subscriptions": obj.get("subscriptions")
        })
        return _obj

