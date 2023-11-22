# coding: utf-8

"""
    OmniCore Model and State Management API

    This is an OmniCore Model and State Management server.  # noqa: E501

    The version of the OpenAPI document: 1.8.5
    Contact: omnicoresupport@korewireless.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt
from OmniCore.models.device import Device

class ListDevicesResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    devices: List[Device] = ...
    page_number: Optional[StrictInt] = Field(None, alias="pageNumber")
    page_size: Optional[StrictInt] = Field(None, alias="pageSize")
    total_count: Optional[StrictInt] = Field(None, alias="totalCount")
    __properties = ["devices", "pageNumber", "pageSize", "totalCount"]

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
    def from_json(cls, json_str: str) -> ListDevicesResponse:
        """Create an instance of ListDevicesResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in devices (list)
        _items = []
        if self.devices:
            for _item in self.devices:
                if _item:
                    _items.append(_item.to_dict())
            _dict['devices'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListDevicesResponse:
        """Create an instance of ListDevicesResponse from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ListDevicesResponse.parse_obj(obj)

        _obj = ListDevicesResponse.parse_obj({
            "devices": [Device.from_dict(_item) for _item in obj.get("devices")] if obj.get("devices") is not None else None,
            "page_number": obj.get("pageNumber"),
            "page_size": obj.get("pageSize"),
            "total_count": obj.get("totalCount")
        })
        return _obj

