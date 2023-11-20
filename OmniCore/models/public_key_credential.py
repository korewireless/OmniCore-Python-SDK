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

class PublicKeyCredential(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    format: StrictStr = Field(..., description="Format: The format of the key.  Possible values:   \"UNSPECIFIED_PUBLIC_KEY_FORMAT\" - The format has not been specified. This is an invalid default value and must not be used.   \"RSA_PEM\" - An RSA public key encoded in base64, and wrapped by `-----BEGIN PUBLIC KEY-----` and `-----END PUBLIC KEY-----`. This can be used to verify `RS256` signatures in JWT tokens ([RFC7518]( https://www.ietf.org/rfc/rfc7518.txt)).   \"RSA_X509_PEM\" - As RSA_PEM, but wrapped in an X.509v3 certificate ([RFC5280]( https://www.ietf.org/rfc/rfc5280.txt)), encoded in base64, and wrapped by `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----`.   \"ES256_PEM\" - Public key for the ECDSA algorithm using P-256 and SHA-256, encoded in base64, and wrapped by `-----BEGIN PUBLIC KEY-----` and `-----END PUBLIC KEY-----`. This can be used to verify JWT tokens with the `ES256` algorithm ([RFC7518](https://www.ietf.org/rfc/rfc7518.txt)). This curve is defined in [OpenSSL](https://www.openssl.org/) as the `prime256v1` curve.   \"ES256_X509_PEM\" - As ES256_PEM, but wrapped in an X.509v3 certificate ([RFC5280]( https://www.ietf.org/rfc/rfc5280.txt)), encoded in base64, and wrapped by `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----`.")
    key: Optional[StrictStr] = Field(None, description="Key: The key data.")
    __properties = ["format", "key"]

    @validator('format')
    def format_validate_enum(cls, v):
        if v not in ('RSA_PEM', 'ES256_PEM', 'RSA_X509_PEM', 'ES256_X509_PEM'):
            raise ValueError("must validate the enum values ('RSA_PEM', 'ES256_PEM', 'RSA_X509_PEM', 'ES256_X509_PEM')")
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
    def from_json(cls, json_str: str) -> PublicKeyCredential:
        """Create an instance of PublicKeyCredential from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PublicKeyCredential:
        """Create an instance of PublicKeyCredential from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return PublicKeyCredential.parse_obj(obj)

        _obj = PublicKeyCredential.parse_obj({
            "format": obj.get("format"),
            "key": obj.get("key")
        })
        return _obj

