# coding: utf-8

"""
    OmniCore Model and State Management API

    This is an OmniCore Model and State Management server.  # noqa: E501

    The version of the OpenAPI document: 1.8.7
    Contact: omnicoresupport@korewireless.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, constr
from OmniCore.models.event_notification_config import EventNotificationConfig
from OmniCore.models.http_config import HttpConfig
from OmniCore.models.log_level import LogLevel
from OmniCore.models.mqtt_config import MqttConfig
from OmniCore.models.notification_config import NotificationConfig
from OmniCore.models.registry_credential import RegistryCredential

class DeviceRegistry(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: constr(strict=True, max_length=256, min_length=3) = ...
    name: Optional[StrictStr] = None
    parent: Optional[StrictStr] = None
    created_on: Optional[StrictStr] = Field(None, alias="createdOn")
    updated_on: Optional[StrictStr] = Field(None, alias="updatedOn")
    credentials: Optional[List[RegistryCredential]] = None
    http_config: Optional[HttpConfig] = Field(None, alias="httpConfig")
    mqtt_config: Optional[MqttConfig] = Field(None, alias="mqttConfig")
    log_level: Optional[LogLevel] = Field(None, alias="logLevel")
    is_nats_route: Optional[StrictBool] = Field(None, alias="isNatsRoute")
    event_notification_configs: Optional[List[EventNotificationConfig]] = Field(None, alias="eventNotificationConfigs")
    log_notification_config: Optional[NotificationConfig] = Field(None, alias="logNotificationConfig")
    state_notification_config: Optional[NotificationConfig] = Field(None, alias="stateNotificationConfig")
    custom_onboard_notification_config: Optional[NotificationConfig] = Field(None, alias="customOnboardNotificationConfig")
    custom_onboard_enabled: Optional[StrictBool] = Field(None, alias="customOnboardEnabled")
    number_of_devices: Optional[StrictInt] = Field(None, alias="numberOfDevices")
    number_of_gateways: Optional[StrictInt] = Field(None, alias="numberOfGateways")
    __properties = ["id", "name", "parent", "createdOn", "updatedOn", "credentials", "httpConfig", "mqttConfig", "logLevel", "isNatsRoute", "eventNotificationConfigs", "logNotificationConfig", "stateNotificationConfig", "customOnboardNotificationConfig", "customOnboardEnabled", "numberOfDevices", "numberOfGateways"]

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
    def from_json(cls, json_str: str) -> DeviceRegistry:
        """Create an instance of DeviceRegistry from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "name",
                            "parent",
                            "created_on",
                            "updated_on",
                            "number_of_devices",
                            "number_of_gateways",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in credentials (list)
        _items = []
        if self.credentials:
            for _item in self.credentials:
                if _item:
                    _items.append(_item.to_dict())
            _dict['credentials'] = _items
        # override the default output from pydantic by calling `to_dict()` of http_config
        if self.http_config:
            _dict['httpConfig'] = self.http_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mqtt_config
        if self.mqtt_config:
            _dict['mqttConfig'] = self.mqtt_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in event_notification_configs (list)
        _items = []
        if self.event_notification_configs:
            for _item in self.event_notification_configs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['eventNotificationConfigs'] = _items
        # override the default output from pydantic by calling `to_dict()` of log_notification_config
        if self.log_notification_config:
            _dict['logNotificationConfig'] = self.log_notification_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of state_notification_config
        if self.state_notification_config:
            _dict['stateNotificationConfig'] = self.state_notification_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_onboard_notification_config
        if self.custom_onboard_notification_config:
            _dict['customOnboardNotificationConfig'] = self.custom_onboard_notification_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DeviceRegistry:
        """Create an instance of DeviceRegistry from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return DeviceRegistry.parse_obj(obj)

        _obj = DeviceRegistry.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "parent": obj.get("parent"),
            "created_on": obj.get("createdOn"),
            "updated_on": obj.get("updatedOn"),
            "credentials": [RegistryCredential.from_dict(_item) for _item in obj.get("credentials")] if obj.get("credentials") is not None else None,
            "http_config": HttpConfig.from_dict(obj.get("httpConfig")) if obj.get("httpConfig") is not None else None,
            "mqtt_config": MqttConfig.from_dict(obj.get("mqttConfig")) if obj.get("mqttConfig") is not None else None,
            "log_level": obj.get("logLevel"),
            "is_nats_route": obj.get("isNatsRoute"),
            "event_notification_configs": [EventNotificationConfig.from_dict(_item) for _item in obj.get("eventNotificationConfigs")] if obj.get("eventNotificationConfigs") is not None else None,
            "log_notification_config": NotificationConfig.from_dict(obj.get("logNotificationConfig")) if obj.get("logNotificationConfig") is not None else None,
            "state_notification_config": NotificationConfig.from_dict(obj.get("stateNotificationConfig")) if obj.get("stateNotificationConfig") is not None else None,
            "custom_onboard_notification_config": NotificationConfig.from_dict(obj.get("customOnboardNotificationConfig")) if obj.get("customOnboardNotificationConfig") is not None else None,
            "custom_onboard_enabled": obj.get("customOnboardEnabled"),
            "number_of_devices": obj.get("numberOfDevices"),
            "number_of_gateways": obj.get("numberOfGateways")
        })
        return _obj

