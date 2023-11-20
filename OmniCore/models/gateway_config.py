# coding: utf-8

"""
    OmniCore Model and State Management API

    This is an OmniCore Model and State Management server.  # noqa: E501

    The version of the OpenAPI document: 1.8.3
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

class GatewayConfig(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    gateway_auth_method: Optional[StrictStr] = Field(None, alias="gatewayAuthMethod")
    gateway_type: Optional[StrictStr] = Field(None, alias="gatewayType")
    __properties = ["gatewayAuthMethod", "gatewayType"]

    @validator('gateway_auth_method')
    def gateway_auth_method_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('GATEWAY_AUTH_METHOD_UNSPECIFIED', 'ASSOCIATION_ONLY', 'DEVICE_AUTH_TOKEN_ONLY', 'ASSOCIATION_AND_DEVICE_AUTH_TOKEN'):
            raise ValueError("must validate the enum values ('GATEWAY_AUTH_METHOD_UNSPECIFIED', 'ASSOCIATION_ONLY', 'DEVICE_AUTH_TOKEN_ONLY', 'ASSOCIATION_AND_DEVICE_AUTH_TOKEN')")
        return v

    @validator('gateway_type')
    def gateway_type_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('NON_GATEWAY', 'GATEWAY'):
            raise ValueError("must validate the enum values ('NON_GATEWAY', 'GATEWAY')")
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
    def from_json(cls, json_str: str) -> GatewayConfig:
        """Create an instance of GatewayConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GatewayConfig:
        """Create an instance of GatewayConfig from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return GatewayConfig.parse_obj(obj)

        _obj = GatewayConfig.parse_obj({
            "gateway_auth_method": obj.get("gatewayAuthMethod"),
            "gateway_type": obj.get("gatewayType")
        })
        return _obj

