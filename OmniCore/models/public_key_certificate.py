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
from OmniCore.models.x509_certificate_details import X509CertificateDetails

class PublicKeyCertificate(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    certificate: Optional[StrictStr] = Field(None, description="Certificate: The certificate data.")
    format: Optional[StrictStr] = Field(None, description="Format: The certificate format.  Possible values:   \"UNSPECIFIED_PUBLIC_KEY_CERTIFICATE_FORMAT\" - The format has not been specified. This is an invalid default value and must not be used.   \"X509_CERTIFICATE_PEM\" - An X.509v3 certificate ([RFC5280](https://www.ietf.org/rfc/rfc5280.txt)), encoded in base64, and wrapped by `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----`.")
    x509_details: Optional[X509CertificateDetails] = Field(None, alias="x509Details")
    __properties = ["certificate", "format", "x509Details"]

    @validator('format')
    def format_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('X509_CERTIFICATE_PEM'):
            raise ValueError("must validate the enum values ('X509_CERTIFICATE_PEM')")
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
    def from_json(cls, json_str: str) -> PublicKeyCertificate:
        """Create an instance of PublicKeyCertificate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of x509_details
        if self.x509_details:
            _dict['x509Details'] = self.x509_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PublicKeyCertificate:
        """Create an instance of PublicKeyCertificate from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return PublicKeyCertificate.parse_obj(obj)

        _obj = PublicKeyCertificate.parse_obj({
            "certificate": obj.get("certificate"),
            "format": obj.get("format"),
            "x509_details": X509CertificateDetails.from_dict(obj.get("x509Details")) if obj.get("x509Details") is not None else None
        })
        return _obj

