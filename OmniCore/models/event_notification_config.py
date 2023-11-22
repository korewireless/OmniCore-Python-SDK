# coding: utf-8

"""
    OmniCore Model and State Management API

    This is an OmniCore Model and State Management server.  # noqa: E501

    The version of the OpenAPI document: 1.8.6
    Contact: omnicoresupport@korewireless.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class EventNotificationConfig(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pubsub_topic_name: Optional[StrictStr] = Field(None, alias="pubsubTopicName", description="PubsubTopicName: A Topic name. For example, `projects/myProject/topics/deviceEvents`.")
    subfolder_matches: Optional[StrictStr] = Field(None, alias="subfolderMatches", description="SubfolderMatches: If the subfolder name matches this string exactly, this configuration will be used. The string must not include the leading '/' character. If empty, all strings are matched. This field is used only for telemetry events; subfolders are not supported for state changes.")
    __properties = ["pubsubTopicName", "subfolderMatches"]

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
    def from_json(cls, json_str: str) -> EventNotificationConfig:
        """Create an instance of EventNotificationConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EventNotificationConfig:
        """Create an instance of EventNotificationConfig from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return EventNotificationConfig.parse_obj(obj)

        _obj = EventNotificationConfig.parse_obj({
            "pubsub_topic_name": obj.get("pubsubTopicName"),
            "subfolder_matches": obj.get("subfolderMatches")
        })
        return _obj

