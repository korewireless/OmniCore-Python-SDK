# coding: utf-8

"""
    OmniCore Model and State Management API

    This is an OmniCore Model and State Management server.  # noqa: E501

    The version of the OpenAPI document: 1.0
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
from OmniCore.models.public_key_credential import PublicKeyCredential

class DeviceCredential(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    expiration_time: Optional[StrictStr] = Field(None, alias="expirationTime", description="ExpirationTime: [Optional] The time at which this credential becomes invalid. This credential will be ignored for new client authentication requests after this timestamp; however, it will not be automatically deleted.")
    id: Optional[StrictStr] = None
    public_key: Optional[PublicKeyCredential] = Field(None, alias="publicKey")
    __properties = ["expirationTime", "id", "publicKey"]

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
    def from_json(cls, json_str: str) -> DeviceCredential:
        """Create an instance of DeviceCredential from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of public_key
        if self.public_key:
            _dict['publicKey'] = self.public_key.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DeviceCredential:
        """Create an instance of DeviceCredential from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return DeviceCredential.parse_obj(obj)

        _obj = DeviceCredential.parse_obj({
            "expiration_time": obj.get("expirationTime"),
            "id": obj.get("id"),
            "public_key": PublicKeyCredential.from_dict(obj.get("publicKey")) if obj.get("publicKey") is not None else None
        })
        return _obj

