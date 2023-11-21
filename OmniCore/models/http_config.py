# coding: utf-8

"""
    OmniCore Model and State Management API

    This is an OmniCore Model and State Management server.  # noqa: E501

    The version of the OpenAPI document: 1.8.4
    Contact: omnicoresupport@korewireless.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator

class HttpConfig(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    http_enabled_state: Optional[StrictStr] = Field(None, alias="httpEnabledState", description="HttpEnabledState: If enabled, allows devices to use DeviceService via the HTTP protocol. Otherwise, any requests to DeviceService will fail for this registry.  Possible values:   \"HTTP_STATE_UNSPECIFIED\" - No HTTP state specified. If not specified, DeviceService will be enabled by default.   \"HTTP_ENABLED\" - Enables DeviceService (HTTP) service for the registry.   \"HTTP_DISABLED\" - Disables DeviceService (HTTP) service for the registry.")
    __properties = ["httpEnabledState"]

    @validator('http_enabled_state')
    def http_enabled_state_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('HTTP_ENABLED', 'HTTP_DISABLED', 'HTTP_STATE_UNSPECIFIED'):
            raise ValueError("must validate the enum values ('HTTP_ENABLED', 'HTTP_DISABLED', 'HTTP_STATE_UNSPECIFIED')")
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
    def from_json(cls, json_str: str) -> HttpConfig:
        """Create an instance of HttpConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HttpConfig:
        """Create an instance of HttpConfig from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return HttpConfig.parse_obj(obj)

        _obj = HttpConfig.parse_obj({
            "http_enabled_state": obj.get("httpEnabledState")
        })
        return _obj

