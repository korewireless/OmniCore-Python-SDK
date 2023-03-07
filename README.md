# OmniCore
This is an OmniCore Model and State Management server.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonNextgenClientCodegen
For more information, please visit [http://www.korewireless.com](http://www.korewireless.com)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/korewireless/OmniCore-Python-SDK.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/korewireless/OmniCore-Python-SDK.git`)

Then import the package:
```python
import OmniCore
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import OmniCore
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import OmniCore
from OmniCore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demo-api.omnicore.cloud.korewireless.com/model-state-management
# See configuration.py for a list of all supported configuration parameters.
configuration = OmniCore.Configuration(
    host = "https://demo-api.omnicore.cloud.korewireless.com/model-state-management"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = OmniCore.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
with OmniCore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = OmniCore.DeviceApi(api_client)
    subscription_id = 'subscription_id_example' # str | Subscription ID
    registry_id = 'registry_id_example' # str | Registry ID
    device = OmniCore.BindRequest() # BindRequest | application/json

    try:
        api_response = api_instance.bind_device(subscription_id, registry_id, device)
        print("The response of DeviceApi->bind_device:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceApi->bind_device: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://demo-api.omnicore.cloud.korewireless.com/model-state-management*

| Class         | Method                                                                             | HTTP request                                                                                                  | Description |
| ------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ----------- |
| *DeviceApi*   | [**bind_device**](docs/DeviceApi.md#bind_device)                                   | **POST** /subscriptions/{subscriptionId}/registries/{registryId}/bindDeviceToGateway                          |
| *DeviceApi*   | [**bind_devices**](docs/DeviceApi.md#bind_devices)                                 | **POST** /subscriptions/{subscriptionId}/registries/{registryId}/bindDevicesToGateway                         |
| *DeviceApi*   | [**block_device_communcation**](docs/DeviceApi.md#block_device_communcation)       | **PUT** /subscriptions/{subscriptionid}/registries/{registryId}/devices/{deviceId}/communication              |
| *DeviceApi*   | [**create_device**](docs/DeviceApi.md#create_device)                               | **POST** /subscriptions/{subscriptionId}/registries/{registryId}/devices                                      |
| *DeviceApi*   | [**delete_device**](docs/DeviceApi.md#delete_device)                               | **DELETE** /subscriptions/{subscriptionId}/registries/{registryId}/devices/{deviceId}                         |
| *DeviceApi*   | [**get_config**](docs/DeviceApi.md#get_config)                                     | **GET** /subscriptions/{subscriptionid}/registries/{registryId}/devices/{deviceId}/configVersions             |
| *DeviceApi*   | [**get_device**](docs/DeviceApi.md#get_device)                                     | **GET** /subscriptions/{subscriptionId}/registries/{registryId}/devices/{deviceId}                            |
| *DeviceApi*   | [**get_devices**](docs/DeviceApi.md#get_devices)                                   | **GET** /subscriptions/{subscriptionId}/registries/{registryId}/devices                                       |
| *DeviceApi*   | [**get_states**](docs/DeviceApi.md#get_states)                                     | **GET** /subscriptions/{subscriptionid}/registries/{registryId}/devices/{deviceId}/states                     |
| *DeviceApi*   | [**send_command_to_device**](docs/DeviceApi.md#send_command_to_device)             | **POST** /subscriptions/{subscriptionid}/registries/{registryId}/devices/{deviceId}/sendCommandToDevice       |
| *DeviceApi*   | [**send_configuration_to_device**](docs/DeviceApi.md#send_configuration_to_device) | **POST** /subscriptions/{subscriptionid}/registries/{registryId}/devices/{deviceId}/sendConfigurationToDevice |
| *DeviceApi*   | [**un_bind_device**](docs/DeviceApi.md#un_bind_device)                             | **POST** /subscriptions/{subscriptionId}/registries/{registryId}/unbindDeviceFromGateway                      |
| *DeviceApi*   | [**un_bind_devices**](docs/DeviceApi.md#un_bind_devices)                           | **POST** /subscriptions/{subscriptionId}/registries/{registryId}/unbindDevicesFromGateway                     |
| *DeviceApi*   | [**update_device**](docs/DeviceApi.md#update_device)                               | **PATCH** /subscriptions/{subscriptionId}/registries/{registryId}/devices/{deviceId}                          |
| *RegistryApi* | [**create_registry**](docs/RegistryApi.md#create_registry)                         | **POST** /subscriptions/{subscriptionId}/registries                                                           |
| *RegistryApi* | [**delete_registry**](docs/RegistryApi.md#delete_registry)                         | **DELETE** /subscriptions/{subscriptionId}/registries/{registryId}                                            |
| *RegistryApi* | [**get_registries**](docs/RegistryApi.md#get_registries)                           | **GET** /subscriptions/{subscriptionId}/registries                                                            |
| *RegistryApi* | [**get_registry**](docs/RegistryApi.md#get_registry)                               | **GET** /subscriptions/{subscriptionId}/registries/{registryId}                                               |
| *RegistryApi* | [**update_registry**](docs/RegistryApi.md#update_registry)                         | **PATCH** /subscriptions/{subscriptionId}/registries/{registryId}                                             |


## Documentation For Models

 - [BindRequest](docs/BindRequest.md)
 - [BindRequestIdsGateway](docs/BindRequestIdsGateway.md)
 - [BlockCommunicationBody](docs/BlockCommunicationBody.md)
 - [Device](docs/Device.md)
 - [DeviceCertificate](docs/DeviceCertificate.md)
 - [DeviceCommand](docs/DeviceCommand.md)
 - [DeviceConfig](docs/DeviceConfig.md)
 - [DeviceConfiguration](docs/DeviceConfiguration.md)
 - [DeviceCredential](docs/DeviceCredential.md)
 - [DeviceRegistry](docs/DeviceRegistry.md)
 - [DeviceState](docs/DeviceState.md)
 - [ErrorFrame](docs/ErrorFrame.md)
 - [ErrorStatus](docs/ErrorStatus.md)
 - [EventNotificationConfig](docs/EventNotificationConfig.md)
 - [GatewayConfig](docs/GatewayConfig.md)
 - [GenericErrorResponse](docs/GenericErrorResponse.md)
 - [HttpConfig](docs/HttpConfig.md)
 - [Info](docs/Info.md)
 - [ListDeviceConfigVersionsResponse](docs/ListDeviceConfigVersionsResponse.md)
 - [ListDeviceRegistriesResponse](docs/ListDeviceRegistriesResponse.md)
 - [ListDeviceStatesResponse](docs/ListDeviceStatesResponse.md)
 - [ListDevicesResponse](docs/ListDevicesResponse.md)
 - [LogLevel](docs/LogLevel.md)
 - [MqttConfig](docs/MqttConfig.md)
 - [NewDevice](docs/NewDevice.md)
 - [NewRegistry](docs/NewRegistry.md)
 - [NotificationConfig](docs/NotificationConfig.md)
 - [PublicKeyCertificate](docs/PublicKeyCertificate.md)
 - [PublicKeyCredential](docs/PublicKeyCredential.md)
 - [RegistryCertificate](docs/RegistryCertificate.md)
 - [RegistryCredential](docs/RegistryCredential.md)
 - [UpdateDevice](docs/UpdateDevice.md)
 - [UpdateRegistry](docs/UpdateRegistry.md)
 - [X509CertificateDetails](docs/X509CertificateDetails.md)


## Documentation For Authorization


## bearerAuth

- **Type**: Bearer authentication (JWT)


## Author

support@korewireless.com


