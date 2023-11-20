# coding: utf-8

"""
    OmniCore Model and State Management API

    This is an OmniCore Model and State Management server.  # noqa: E501

    The version of the OpenAPI document: 1.8.2
    Contact: omnicoresupport@korewireless.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictBool, StrictStr

class Policy(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    connect: StrictBool = Field(..., alias="Connect")
    publish_state: StrictBool = Field(..., alias="PublishState")
    publish_events: StrictBool = Field(..., alias="PublishEvents")
    publish_events_regex: StrictStr = Field(..., alias="PublishEventsRegex")
    publish_loopback: StrictBool = Field(..., alias="PublishLoopback")
    subscribe_command: StrictBool = Field(..., alias="SubscribeCommand")
    subscribe_command_regex: StrictStr = Field(..., alias="SubscribeCommandRegex")
    subscribe_broadcast: StrictBool = Field(..., alias="SubscribeBroadcast")
    subscribe_broadcast_regex: StrictStr = Field(..., alias="SubscribeBroadcastRegex")
    subscribe_config: StrictBool = Field(..., alias="SubscribeConfig")
    __properties = ["Connect", "PublishState", "PublishEvents", "PublishEventsRegex", "PublishLoopback", "SubscribeCommand", "SubscribeCommandRegex", "SubscribeBroadcast", "SubscribeBroadcastRegex", "SubscribeConfig"]

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
    def from_json(cls, json_str: str) -> Policy:
        """Create an instance of Policy from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Policy:
        """Create an instance of Policy from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Policy.parse_obj(obj)

        _obj = Policy.parse_obj({
            "connect": obj.get("Connect"),
            "publish_state": obj.get("PublishState"),
            "publish_events": obj.get("PublishEvents"),
            "publish_events_regex": obj.get("PublishEventsRegex"),
            "publish_loopback": obj.get("PublishLoopback"),
            "subscribe_command": obj.get("SubscribeCommand"),
            "subscribe_command_regex": obj.get("SubscribeCommandRegex"),
            "subscribe_broadcast": obj.get("SubscribeBroadcast"),
            "subscribe_broadcast_regex": obj.get("SubscribeBroadcastRegex"),
            "subscribe_config": obj.get("SubscribeConfig")
        })
        return _obj

