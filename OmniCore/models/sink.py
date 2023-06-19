# coding: utf-8

"""
    OmniCore Model and State Management API

    This is an OmniCore Model and State Management server.  # noqa: E501

    The version of the OpenAPI document: 1.8.1
    Contact: omnicoresupport@korewireless.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictBool, StrictStr, validator
from OmniCore.models.config import Config

class Sink(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[StrictStr] = None
    subscription: Optional[StrictStr] = None
    sink: Optional[StrictStr] = None
    config: Optional[Config] = None
    status: Optional[StrictBool] = None
    createdon: Optional[StrictStr] = None
    updatedon: Optional[StrictStr] = None
    __properties = ["id", "subscription", "sink", "config", "status", "createdon", "updatedon"]

    @validator('sink')
    def sink_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('pubsub'):
            raise ValueError("must validate the enum values ('pubsub')")
        return v

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
    def from_json(cls, json_str: str) -> Sink:
        """Create an instance of Sink from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                            "subscription",
                            "status",
                            "createdon",
                            "updatedon",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of config
        if self.config:
            _dict['config'] = self.config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Sink:
        """Create an instance of Sink from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Sink.parse_obj(obj)

        _obj = Sink.parse_obj({
            "id": obj.get("id"),
            "subscription": obj.get("subscription"),
            "sink": obj.get("sink"),
            "config": Config.from_dict(obj.get("config")) if obj.get("config") is not None else None,
            "status": obj.get("status"),
            "createdon": obj.get("createdon"),
            "updatedon": obj.get("updatedon")
        })
        return _obj

