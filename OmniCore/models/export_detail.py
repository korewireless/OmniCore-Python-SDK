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
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr

class ExportDetail(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    subscription: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    source: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    destination: Optional[StrictStr] = None
    created_on: Optional[StrictStr] = Field(None, alias="createdOn")
    nooffiles: Optional[StrictInt] = None
    file_size: Optional[StrictFloat] = Field(None, alias="fileSize")
    done: Optional[StrictBool] = None
    __properties = ["subscription", "name", "source", "status", "destination", "createdOn", "nooffiles", "fileSize", "done"]

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
    def from_json(cls, json_str: str) -> ExportDetail:
        """Create an instance of ExportDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExportDetail:
        """Create an instance of ExportDetail from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ExportDetail.parse_obj(obj)

        _obj = ExportDetail.parse_obj({
            "subscription": obj.get("subscription"),
            "name": obj.get("name"),
            "source": obj.get("source"),
            "status": obj.get("status"),
            "destination": obj.get("destination"),
            "created_on": obj.get("createdOn"),
            "nooffiles": obj.get("nooffiles"),
            "file_size": obj.get("fileSize"),
            "done": obj.get("done")
        })
        return _obj

