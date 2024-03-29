# coding: utf-8

"""
    OmniCore Model and State Management API

    This is an OmniCore Model and State Management server.  # noqa: E501

    The version of the OpenAPI document: 1.8.11
    Contact: omnicoresupport@korewireless.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr

class ReplayBody(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    registry: Optional[StrictStr] = None
    start_time: Optional[StrictInt] = Field(None, alias="startTime")
    end_time: Optional[StrictInt] = Field(None, alias="endTime")
    destination: Optional[StrictStr] = None
    source: Optional[StrictStr] = None
    __properties = ["registry", "startTime", "endTime", "destination", "source"]

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
    def from_json(cls, json_str: str) -> ReplayBody:
        """Create an instance of ReplayBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReplayBody:
        """Create an instance of ReplayBody from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ReplayBody.parse_obj(obj)

        _obj = ReplayBody.parse_obj({
            "registry": obj.get("registry"),
            "start_time": obj.get("startTime"),
            "end_time": obj.get("endTime"),
            "destination": obj.get("destination"),
            "source": obj.get("source")
        })
        return _obj

