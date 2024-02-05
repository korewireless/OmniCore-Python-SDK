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
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class Folder(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    no_of_files: Optional[StrictInt] = Field(None, alias="noOfFiles")
    file_size: Optional[StrictFloat] = Field(None, alias="fileSize")
    noofoperations: Optional[StrictInt] = None
    updatedon: Optional[StrictStr] = None
    registryid: Optional[StrictStr] = None
    __properties = ["noOfFiles", "fileSize", "noofoperations", "updatedon", "registryid"]

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
    def from_json(cls, json_str: str) -> Folder:
        """Create an instance of Folder from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Folder:
        """Create an instance of Folder from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Folder.parse_obj(obj)

        _obj = Folder.parse_obj({
            "no_of_files": obj.get("noOfFiles"),
            "file_size": obj.get("fileSize"),
            "noofoperations": obj.get("noofoperations"),
            "updatedon": obj.get("updatedon"),
            "registryid": obj.get("registryid")
        })
        return _obj

