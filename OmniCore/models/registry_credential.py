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
from pydantic import BaseModel, Field, StrictStr
from OmniCore.models.public_key_certificate import PublicKeyCertificate

class RegistryCredential(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    public_key_certificate: Optional[PublicKeyCertificate] = Field(None, alias="publicKeyCertificate")
    id: Optional[StrictStr] = None
    __properties = ["publicKeyCertificate", "id"]

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
    def from_json(cls, json_str: str) -> RegistryCredential:
        """Create an instance of RegistryCredential from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of public_key_certificate
        if self.public_key_certificate:
            _dict['publicKeyCertificate'] = self.public_key_certificate.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RegistryCredential:
        """Create an instance of RegistryCredential from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return RegistryCredential.parse_obj(obj)

        _obj = RegistryCredential.parse_obj({
            "public_key_certificate": PublicKeyCertificate.from_dict(obj.get("publicKeyCertificate")) if obj.get("publicKeyCertificate") is not None else None,
            "id": obj.get("id")
        })
        return _obj

