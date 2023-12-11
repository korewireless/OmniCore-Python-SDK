# OmniCore
This is an OmniCore Model and State Management server.


- API version: 1.8.7
- Package version: 1.8.7
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

# Defining the host is optional and defaults to https://api.korewireless.com
# See configuration.py for a list of all supported configuration parameters.
configuration = OmniCore.Configuration(
    host = "https://api.korewireless.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

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
    bind = OmniCore.BindRequest() # BindRequest | application/json

    try:
        api_response = api_instance.bind_device(subscription_id, registry_id, bind)
        print("The response of DeviceApi->bind_device:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceApi->bind_device: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.korewireless.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DeviceApi* | [**bind_device**](docs/DeviceApi.md#bind_device) | **POST** /omnicore/subscriptions/{subscriptionId}/registries/{registryId}/bindDeviceToGateway | 
*DeviceApi* | [**bind_devices**](docs/DeviceApi.md#bind_devices) | **POST** /omnicore/subscriptions/{subscriptionId}/registries/{registryId}/bindDevicesToGateway | 
*DeviceApi* | [**block_device_communcation**](docs/DeviceApi.md#block_device_communcation) | **PUT** /omnicore/subscriptions/{subscriptionid}/registries/{registryId}/devices/{deviceId}/communication | 
*DeviceApi* | [**create_device**](docs/DeviceApi.md#create_device) | **POST** /omnicore/subscriptions/{subscriptionId}/registries/{registryId}/devices | 
*DeviceApi* | [**delete_device**](docs/DeviceApi.md#delete_device) | **DELETE** /omnicore/subscriptions/{subscriptionId}/registries/{registryId}/devices/{deviceId} | 
*DeviceApi* | [**get_config**](docs/DeviceApi.md#get_config) | **GET** /omnicore/subscriptions/{subscriptionid}/registries/{registryId}/devices/{deviceId}/configVersions | 
*DeviceApi* | [**get_device**](docs/DeviceApi.md#get_device) | **GET** /omnicore/subscriptions/{subscriptionId}/registries/{registryId}/devices/{deviceId} | 
*DeviceApi* | [**get_devices**](docs/DeviceApi.md#get_devices) | **GET** /omnicore/subscriptions/{subscriptionId}/registries/{registryId}/devices | 
*DeviceApi* | [**get_states**](docs/DeviceApi.md#get_states) | **GET** /omnicore/subscriptions/{subscriptionid}/registries/{registryId}/devices/{deviceId}/states | 
*DeviceApi* | [**send_command_to_device**](docs/DeviceApi.md#send_command_to_device) | **POST** /omnicore/subscriptions/{subscriptionid}/registries/{registryId}/devices/{deviceId}/sendCommandToDevice | 
*DeviceApi* | [**un_bind_device**](docs/DeviceApi.md#un_bind_device) | **POST** /omnicore/subscriptions/{subscriptionId}/registries/{registryId}/unbindDeviceFromGateway | 
*DeviceApi* | [**un_bind_devices**](docs/DeviceApi.md#un_bind_devices) | **POST** /omnicore/subscriptions/{subscriptionId}/registries/{registryId}/unbindDevicesFromGateway | 
*DeviceApi* | [**update_configuration_to_device**](docs/DeviceApi.md#update_configuration_to_device) | **POST** /omnicore/subscriptions/{subscriptionid}/registries/{registryId}/devices/{deviceId}/updateConfigurationToDevice | 
*DeviceApi* | [**update_custom_onboard_request**](docs/DeviceApi.md#update_custom_onboard_request) | **POST** /omnicore/subscriptions/{subscriptionid}/registries/{registryId}/devices/{deviceId}/updateCustomOnboardRequest | 
*DeviceApi* | [**update_device**](docs/DeviceApi.md#update_device) | **PATCH** /omnicore/subscriptions/{subscriptionId}/registries/{registryId}/devices/{deviceId} | 
*MetricsApi* | [**get_metrics**](docs/MetricsApi.md#get_metrics) | **GET** /omnicore/subscriptions/{subscriptionId}/metrics | 
*RegistryApi* | [**create_registry**](docs/RegistryApi.md#create_registry) | **POST** /omnicore/subscriptions/{subscriptionId}/registries | 
*RegistryApi* | [**delete_registry**](docs/RegistryApi.md#delete_registry) | **DELETE** /omnicore/subscriptions/{subscriptionId}/registries/{registryId} | 
*RegistryApi* | [**get_registries**](docs/RegistryApi.md#get_registries) | **GET** /omnicore/subscriptions/{subscriptionId}/registries | 
*RegistryApi* | [**get_registry**](docs/RegistryApi.md#get_registry) | **GET** /omnicore/subscriptions/{subscriptionId}/registries/{registryId} | 
*RegistryApi* | [**send_broadcast_to_devices**](docs/RegistryApi.md#send_broadcast_to_devices) | **POST** /omnicore/subscriptions/{subscriptionid}/registries/{registryId}/sendBroadcastToDevice | 
*RegistryApi* | [**update_registry**](docs/RegistryApi.md#update_registry) | **PATCH** /omnicore/subscriptions/{subscriptionId}/registries/{registryId} | 
*SinkApi* | [**create_sink**](docs/SinkApi.md#create_sink) | **POST** /omnicore/subscriptions/{subscriptionId}/sinks | 
*SinkApi* | [**delete_sink**](docs/SinkApi.md#delete_sink) | **DELETE** /omnicore/subscriptions/{subscriptionId}/sinks/{sinkId} | 
*SinkApi* | [**get_a_sink**](docs/SinkApi.md#get_a_sink) | **GET** /omnicore/subscriptions/{subscriptionId}/sinks/{sinkId} | 
*SinkApi* | [**get_sinks**](docs/SinkApi.md#get_sinks) | **GET** /omnicore/subscriptions/{subscriptionId}/sinks | Get All Sinks
*VaultApi* | [**create_vault_configuration**](docs/VaultApi.md#create_vault_configuration) | **POST** /vault/subscriptions/{subscriptionid}/configurations | 
*VaultApi* | [**create_vault_key**](docs/VaultApi.md#create_vault_key) | **POST** /vault/subscriptions/{subscriptionid}/encryptionkeys | 
*VaultApi* | [**delete_configuration**](docs/VaultApi.md#delete_configuration) | **DELETE** /vault/subscriptions/{subscriptionid}/configurations/{configid} | 
*VaultApi* | [**delete_vault_key**](docs/VaultApi.md#delete_vault_key) | **DELETE** /vault/subscriptions/{subscriptionid}/encryptionkeys/{keyid} | 
*VaultApi* | [**enable_encryption**](docs/VaultApi.md#enable_encryption) | **POST** /vault/subscriptions/{subscriptionid}/encryption | 
*VaultApi* | [**get_exports**](docs/VaultApi.md#get_exports) | **GET** /vault/subscriptions/{subscriptionid}/exports | 
*VaultApi* | [**get_registry_data**](docs/VaultApi.md#get_registry_data) | **GET** /vault/subscriptions/{subscriptionid}/folders | 
*VaultApi* | [**get_replays**](docs/VaultApi.md#get_replays) | **GET** /vault/subscriptions/{subscriptionid}/replays | 
*VaultApi* | [**get_vault_audit**](docs/VaultApi.md#get_vault_audit) | **GET** /vault/subscriptions/{subscriptionid}/audit | 
*VaultApi* | [**get_vault_configurations**](docs/VaultApi.md#get_vault_configurations) | **GET** /vault/subscriptions/{subscriptionid}/configurations | 
*VaultApi* | [**get_vault_files**](docs/VaultApi.md#get_vault_files) | **GET** /vault/subscriptions/{subscriptionid}/registry/{registryid}/files | 
*VaultApi* | [**get_vault_keys**](docs/VaultApi.md#get_vault_keys) | **GET** /vault/subscriptions/{subscriptionid}/encryptionkeys | 
*VaultApi* | [**get_vault_metrics**](docs/VaultApi.md#get_vault_metrics) | **GET** /vault/subscriptions/{subscriptionid}/metrics | 
*VaultApi* | [**get_vault_status**](docs/VaultApi.md#get_vault_status) | **GET** /vault/subscriptions/{subscriptionid}/status | 
*VaultApi* | [**set_retention**](docs/VaultApi.md#set_retention) | **POST** /vault/subscriptions/{subscriptionid}/retention | 
*VaultApi* | [**start_export**](docs/VaultApi.md#start_export) | **POST** /vault/subscriptions/{subscriptionid}/exports | 
*VaultApi* | [**start_replay**](docs/VaultApi.md#start_replay) | **POST** /vault/subscriptions/{subscriptionid}/replays | 


## Documentation For Models

 - [Audit](docs/Audit.md)
 - [AuditResult](docs/AuditResult.md)
 - [BindRequest](docs/BindRequest.md)
 - [BindRequestIdsGateway](docs/BindRequestIdsGateway.md)
 - [BlockCommunicationBody](docs/BlockCommunicationBody.md)
 - [Config](docs/Config.md)
 - [Configurations](docs/Configurations.md)
 - [CreateConfiguration](docs/CreateConfiguration.md)
 - [CreateVaultKeyBody](docs/CreateVaultKeyBody.md)
 - [CustomOnboard](docs/CustomOnboard.md)
 - [Device](docs/Device.md)
 - [DeviceCommand](docs/DeviceCommand.md)
 - [DeviceConfig](docs/DeviceConfig.md)
 - [DeviceConfiguration](docs/DeviceConfiguration.md)
 - [DeviceCredential](docs/DeviceCredential.md)
 - [DeviceRegistry](docs/DeviceRegistry.md)
 - [DeviceState](docs/DeviceState.md)
 - [EnableEncryptionBody](docs/EnableEncryptionBody.md)
 - [ErrorFrame](docs/ErrorFrame.md)
 - [ErrorStatus](docs/ErrorStatus.md)
 - [EventNotificationConfig](docs/EventNotificationConfig.md)
 - [ExportDetail](docs/ExportDetail.md)
 - [FileDetail](docs/FileDetail.md)
 - [FileDetails](docs/FileDetails.md)
 - [Folder](docs/Folder.md)
 - [FolderData](docs/FolderData.md)
 - [Frame](docs/Frame.md)
 - [GatewayConfig](docs/GatewayConfig.md)
 - [GenericErrorResponse](docs/GenericErrorResponse.md)
 - [GetExportsResponse](docs/GetExportsResponse.md)
 - [GetKeysResponse](docs/GetKeysResponse.md)
 - [GetReplaysResponse](docs/GetReplaysResponse.md)
 - [HttpConfig](docs/HttpConfig.md)
 - [Info](docs/Info.md)
 - [ListDeviceConfigVersionsResponse](docs/ListDeviceConfigVersionsResponse.md)
 - [ListDeviceRegistries](docs/ListDeviceRegistries.md)
 - [ListDeviceStatesResponse](docs/ListDeviceStatesResponse.md)
 - [ListDevicesResponse](docs/ListDevicesResponse.md)
 - [ListSinks](docs/ListSinks.md)
 - [LogLevel](docs/LogLevel.md)
 - [Metrics](docs/Metrics.md)
 - [MetricsData](docs/MetricsData.md)
 - [MetricsDetails](docs/MetricsDetails.md)
 - [MetricsLogs](docs/MetricsLogs.md)
 - [MetricsResponse](docs/MetricsResponse.md)
 - [MetricsResponseDetails](docs/MetricsResponseDetails.md)
 - [MqttConfig](docs/MqttConfig.md)
 - [NotificationConfig](docs/NotificationConfig.md)
 - [OperationMetrics](docs/OperationMetrics.md)
 - [Policy](docs/Policy.md)
 - [PublicKeyCertificate](docs/PublicKeyCertificate.md)
 - [PublicKeyCredential](docs/PublicKeyCredential.md)
 - [RegistryCredential](docs/RegistryCredential.md)
 - [Replay](docs/Replay.md)
 - [ReplayBody](docs/ReplayBody.md)
 - [SetRetentionBody](docs/SetRetentionBody.md)
 - [Sink](docs/Sink.md)
 - [StartExportBody](docs/StartExportBody.md)
 - [VaultConfiguration](docs/VaultConfiguration.md)
 - [VaultEncryptionKey](docs/VaultEncryptionKey.md)
 - [VaultStatus](docs/VaultStatus.md)
 - [VaultStatusDetails](docs/VaultStatusDetails.md)
 - [X509CertificateDetails](docs/X509CertificateDetails.md)


## Documentation For Authorization


## bearerAuth

- **Type**: Bearer authentication (JWT)


## apiKey

- **Type**: API key
- **API key parameter name**: x-api-key
- **Location**: HTTP header


## Author

omnicoresupport@korewireless.com


