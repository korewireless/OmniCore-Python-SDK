# coding: utf-8

"""
    OmniCore Model and State Management API

    This is an OmniCore Model and State Management server.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@korewireless.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "OmniCore"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3",
    "python-dateutil",
    "pydantic",
    "aenum"
]

setup(
    name=NAME,
    version=VERSION,
    description="OmniCore Model and State Management API",
    author="API Support",
    author_email="support@korewireless.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "OmniCore Model and State Management API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    This is an OmniCore Model and State Management server.  # noqa: E501
    """
)
