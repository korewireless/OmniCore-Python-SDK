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

class X509CertificateDetails(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    expiry_time: Optional[StrictStr] = Field(None, alias="expiryTime", description="ExpiryTime: The time the certificate becomes invalid.")
    issuer: Optional[StrictStr] = Field(None, description="Issuer: The entity that signed the certificate.")
    public_key_type: Optional[StrictStr] = Field(None, alias="publicKeyType", description="PublicKeyType: The type of public key in the certificate.")
    signature_algorithm: Optional[StrictStr] = Field(None, alias="signatureAlgorithm", description="SignatureAlgorithm: The algorithm used to sign the certificate.")
    start_time: Optional[StrictStr] = Field(None, alias="startTime", description="StartTime: The time the certificate becomes valid.")
    subject: Optional[StrictStr] = Field(None, description="Subject: The entity the certificate and public key belong to.")
    __properties = ["expiryTime", "issuer", "publicKeyType", "signatureAlgorithm", "startTime", "subject"]

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
    def from_json(cls, json_str: str) -> X509CertificateDetails:
        """Create an instance of X509CertificateDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> X509CertificateDetails:
        """Create an instance of X509CertificateDetails from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return X509CertificateDetails.parse_obj(obj)

        _obj = X509CertificateDetails.parse_obj({
            "expiry_time": obj.get("expiryTime"),
            "issuer": obj.get("issuer"),
            "public_key_type": obj.get("publicKeyType"),
            "signature_algorithm": obj.get("signatureAlgorithm"),
            "start_time": obj.get("startTime"),
            "subject": obj.get("subject")
        })
        return _obj

