# OmniCore.VaultApi

All URIs are relative to *https://api.korewireless.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_vault_configuration**](VaultApi.md#create_vault_configuration) | **POST** /vault/subscriptions/{subscriptionid}/configurations | 
[**create_vault_key**](VaultApi.md#create_vault_key) | **POST** /vault/subscriptions/{subscriptionid}/encryptionkeys | 
[**delete_configuration**](VaultApi.md#delete_configuration) | **DELETE** /vault/subscriptions/{subscriptionid}/configurations/{configid} | 
[**delete_vault_key**](VaultApi.md#delete_vault_key) | **DELETE** /vault/subscriptions/{subscriptionid}/encryptionkeys/{keyid} | 
[**get_exports**](VaultApi.md#get_exports) | **GET** /vault/subscriptions/{subscriptionid}/exports | 
[**get_registry_data**](VaultApi.md#get_registry_data) | **GET** /vault/subscriptions/{subscriptionid}/folders | 
[**get_replays**](VaultApi.md#get_replays) | **GET** /vault/subscriptions/{subscriptionid}/replays | 
[**get_vault_audit**](VaultApi.md#get_vault_audit) | **GET** /vault/subscriptions/{subscriptionid}/audit | 
[**get_vault_configurations**](VaultApi.md#get_vault_configurations) | **GET** /vault/subscriptions/{subscriptionid}/configurations | 
[**get_vault_files**](VaultApi.md#get_vault_files) | **GET** /vault/subscriptions/{subscriptionid}/registry/{registryid}/files | 
[**get_vault_keys**](VaultApi.md#get_vault_keys) | **GET** /vault/subscriptions/{subscriptionid}/encryptionkeys | 
[**get_vault_metrics**](VaultApi.md#get_vault_metrics) | **GET** /vault/subscriptions/{subscriptionid}/metrics | 
[**get_vault_status**](VaultApi.md#get_vault_status) | **GET** /vault/subscriptions/{subscriptionid}/status | 
[**start_export**](VaultApi.md#start_export) | **POST** /vault/subscriptions/{subscriptionid}/exports | 
[**start_replay**](VaultApi.md#start_replay) | **POST** /vault/subscriptions/{subscriptionid}/replays | 


# **create_vault_configuration**
> Frame create_vault_configuration(subscriptionid, create_configuration=create_configuration)



create vault configuration

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
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
    api_instance = OmniCore.VaultApi(api_client)
    subscriptionid = 'subscriptionid_example' # str | Subscription ID
    create_configuration = OmniCore.CreateConfiguration() # CreateConfiguration | application/json (optional)

    try:
        api_response = api_instance.create_vault_configuration(subscriptionid, create_configuration=create_configuration)
        print("The response of VaultApi->create_vault_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultApi->create_vault_configuration: %s\n" % e)
```

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
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
    api_instance = OmniCore.VaultApi(api_client)
    subscriptionid = 'subscriptionid_example' # str | Subscription ID
    create_configuration = OmniCore.CreateConfiguration() # CreateConfiguration | application/json (optional)

    try:
        api_response = api_instance.create_vault_configuration(subscriptionid, create_configuration=create_configuration)
        print("The response of VaultApi->create_vault_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultApi->create_vault_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionid** | **str**| Subscription ID | 
 **create_configuration** | [**CreateConfiguration**](CreateConfiguration.md)| application/json | [optional] 

### Return type

[**Frame**](Frame.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_vault_key**
> Frame create_vault_key(subscriptionid, create_vault_key_body=create_vault_key_body)



Create Vault Key

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
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
    api_instance = OmniCore.VaultApi(api_client)
    subscriptionid = 'subscriptionid_example' # str | Subscription ID
    create_vault_key_body = OmniCore.CreateVaultKeyBody() # CreateVaultKeyBody | application/json (optional)

    try:
        api_response = api_instance.create_vault_key(subscriptionid, create_vault_key_body=create_vault_key_body)
        print("The response of VaultApi->create_vault_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultApi->create_vault_key: %s\n" % e)
```

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
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
    api_instance = OmniCore.VaultApi(api_client)
    subscriptionid = 'subscriptionid_example' # str | Subscription ID
    create_vault_key_body = OmniCore.CreateVaultKeyBody() # CreateVaultKeyBody | application/json (optional)

    try:
        api_response = api_instance.create_vault_key(subscriptionid, create_vault_key_body=create_vault_key_body)
        print("The response of VaultApi->create_vault_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultApi->create_vault_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionid** | **str**| Subscription ID | 
 **create_vault_key_body** | [**CreateVaultKeyBody**](CreateVaultKeyBody.md)| application/json | [optional] 

### Return type

[**Frame**](Frame.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_configuration**
> Frame delete_configuration(subscriptionid, configid)



Delete Configuration

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
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
    api_instance = OmniCore.VaultApi(api_client)
    subscriptionid = 'subscriptionid_example' # str | Subscription ID
    configid = 'configid_example' # str | config id

    try:
        api_response = api_instance.delete_configuration(subscriptionid, configid)
        print("The response of VaultApi->delete_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultApi->delete_configuration: %s\n" % e)
```

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
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
    api_instance = OmniCore.VaultApi(api_client)
    subscriptionid = 'subscriptionid_example' # str | Subscription ID
    configid = 'configid_example' # str | config id

    try:
        api_response = api_instance.delete_configuration(subscriptionid, configid)
        print("The response of VaultApi->delete_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultApi->delete_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionid** | **str**| Subscription ID | 
 **configid** | **str**| config id | 

### Return type

[**Frame**](Frame.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vault_key**
> Frame delete_vault_key(subscriptionid, keyid)



Delete Vault Key

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
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
    api_instance = OmniCore.VaultApi(api_client)
    subscriptionid = 'subscriptionid_example' # str | Subscription ID
    keyid = 'keyid_example' # str | key id

    try:
        api_response = api_instance.delete_vault_key(subscriptionid, keyid)
        print("The response of VaultApi->delete_vault_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultApi->delete_vault_key: %s\n" % e)
```

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
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
    api_instance = OmniCore.VaultApi(api_client)
    subscriptionid = 'subscriptionid_example' # str | Subscription ID
    keyid = 'keyid_example' # str | key id

    try:
        api_response = api_instance.delete_vault_key(subscriptionid, keyid)
        print("The response of VaultApi->delete_vault_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultApi->delete_vault_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionid** | **str**| Subscription ID | 
 **keyid** | **str**| key id | 

### Return type

[**Frame**](Frame.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_exports**
> GetExportsResponse get_exports(subscriptionid)



Get Exports

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
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
    api_instance = OmniCore.VaultApi(api_client)
    subscriptionid = 'subscriptionid_example' # str | Subscription ID

    try:
        api_response = api_instance.get_exports(subscriptionid)
        print("The response of VaultApi->get_exports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultApi->get_exports: %s\n" % e)
```

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
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
    api_instance = OmniCore.VaultApi(api_client)
    subscriptionid = 'subscriptionid_example' # str | Subscription ID

    try:
        api_response = api_instance.get_exports(subscriptionid)
        print("The response of VaultApi->get_exports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultApi->get_exports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionid** | **str**| Subscription ID | 

### Return type

[**GetExportsResponse**](GetExportsResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registry_data**
> FolderData get_registry_data(subscriptionid)



Get vault folder data

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
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
    api_instance = OmniCore.VaultApi(api_client)
    subscriptionid = 'subscriptionid_example' # str | Subscription ID

    try:
        api_response = api_instance.get_registry_data(subscriptionid)
        print("The response of VaultApi->get_registry_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultApi->get_registry_data: %s\n" % e)
```

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
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
    api_instance = OmniCore.VaultApi(api_client)
    subscriptionid = 'subscriptionid_example' # str | Subscription ID

    try:
        api_response = api_instance.get_registry_data(subscriptionid)
        print("The response of VaultApi->get_registry_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultApi->get_registry_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionid** | **str**| Subscription ID | 

### Return type

[**FolderData**](FolderData.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_replays**
> GetReplaysResponse get_replays(subscriptionid)



Get Replays

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
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
    api_instance = OmniCore.VaultApi(api_client)
    subscriptionid = 'subscriptionid_example' # str | Subscription ID

    try:
        api_response = api_instance.get_replays(subscriptionid)
        print("The response of VaultApi->get_replays:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultApi->get_replays: %s\n" % e)
```

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
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
    api_instance = OmniCore.VaultApi(api_client)
    subscriptionid = 'subscriptionid_example' # str | Subscription ID

    try:
        api_response = api_instance.get_replays(subscriptionid)
        print("The response of VaultApi->get_replays:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultApi->get_replays: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionid** | **str**| Subscription ID | 

### Return type

[**GetReplaysResponse**](GetReplaysResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vault_audit**
> AuditResult get_vault_audit(subscriptionid, page_number=page_number, page_size=page_size)



Get vault Audit

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
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
    api_instance = OmniCore.VaultApi(api_client)
    subscriptionid = 'subscriptionid_example' # str | Subscription ID
    page_number = 56 # int | Page Number (optional)
    page_size = 56 # int | Page Size (optional)

    try:
        api_response = api_instance.get_vault_audit(subscriptionid, page_number=page_number, page_size=page_size)
        print("The response of VaultApi->get_vault_audit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultApi->get_vault_audit: %s\n" % e)
```

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
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
    api_instance = OmniCore.VaultApi(api_client)
    subscriptionid = 'subscriptionid_example' # str | Subscription ID
    page_number = 56 # int | Page Number (optional)
    page_size = 56 # int | Page Size (optional)

    try:
        api_response = api_instance.get_vault_audit(subscriptionid, page_number=page_number, page_size=page_size)
        print("The response of VaultApi->get_vault_audit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultApi->get_vault_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionid** | **str**| Subscription ID | 
 **page_number** | **int**| Page Number | [optional] 
 **page_size** | **int**| Page Size | [optional] 

### Return type

[**AuditResult**](AuditResult.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vault_configurations**
> Configurations get_vault_configurations(subscriptionid)



Get vault configurations

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
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
    api_instance = OmniCore.VaultApi(api_client)
    subscriptionid = 'subscriptionid_example' # str | Subscription ID

    try:
        api_response = api_instance.get_vault_configurations(subscriptionid)
        print("The response of VaultApi->get_vault_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultApi->get_vault_configurations: %s\n" % e)
```

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
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
    api_instance = OmniCore.VaultApi(api_client)
    subscriptionid = 'subscriptionid_example' # str | Subscription ID

    try:
        api_response = api_instance.get_vault_configurations(subscriptionid)
        print("The response of VaultApi->get_vault_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultApi->get_vault_configurations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionid** | **str**| Subscription ID | 

### Return type

[**Configurations**](Configurations.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vault_files**
> FileDetails get_vault_files(subscriptionid, registryid, file_type=file_type)



Get vault files

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
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
    api_instance = OmniCore.VaultApi(api_client)
    subscriptionid = 'subscriptionid_example' # str | Subscription ID
    registryid = 'registryid_example' # str | registry ID
    file_type = 'file_type_example' # str | file type (optional)

    try:
        api_response = api_instance.get_vault_files(subscriptionid, registryid, file_type=file_type)
        print("The response of VaultApi->get_vault_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultApi->get_vault_files: %s\n" % e)
```

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
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
    api_instance = OmniCore.VaultApi(api_client)
    subscriptionid = 'subscriptionid_example' # str | Subscription ID
    registryid = 'registryid_example' # str | registry ID
    file_type = 'file_type_example' # str | file type (optional)

    try:
        api_response = api_instance.get_vault_files(subscriptionid, registryid, file_type=file_type)
        print("The response of VaultApi->get_vault_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultApi->get_vault_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionid** | **str**| Subscription ID | 
 **registryid** | **str**| registry ID | 
 **file_type** | **str**| file type | [optional] 

### Return type

[**FileDetails**](FileDetails.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vault_keys**
> GetKeysResponse get_vault_keys(subscriptionid)



Get Vault Keys

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
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
    api_instance = OmniCore.VaultApi(api_client)
    subscriptionid = 'subscriptionid_example' # str | Subscription ID

    try:
        api_response = api_instance.get_vault_keys(subscriptionid)
        print("The response of VaultApi->get_vault_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultApi->get_vault_keys: %s\n" % e)
```

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
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
    api_instance = OmniCore.VaultApi(api_client)
    subscriptionid = 'subscriptionid_example' # str | Subscription ID

    try:
        api_response = api_instance.get_vault_keys(subscriptionid)
        print("The response of VaultApi->get_vault_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultApi->get_vault_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionid** | **str**| Subscription ID | 

### Return type

[**GetKeysResponse**](GetKeysResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vault_metrics**
> MetricsResponse get_vault_metrics(subscriptionid, start_time=start_time, end_time=end_time)



Get vault metrics

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
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
    api_instance = OmniCore.VaultApi(api_client)
    subscriptionid = 'subscriptionid_example' # str | Subscription ID
    start_time = 'start_time_example' # str | start time (optional)
    end_time = 'end_time_example' # str | end time (optional)

    try:
        api_response = api_instance.get_vault_metrics(subscriptionid, start_time=start_time, end_time=end_time)
        print("The response of VaultApi->get_vault_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultApi->get_vault_metrics: %s\n" % e)
```

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
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
    api_instance = OmniCore.VaultApi(api_client)
    subscriptionid = 'subscriptionid_example' # str | Subscription ID
    start_time = 'start_time_example' # str | start time (optional)
    end_time = 'end_time_example' # str | end time (optional)

    try:
        api_response = api_instance.get_vault_metrics(subscriptionid, start_time=start_time, end_time=end_time)
        print("The response of VaultApi->get_vault_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultApi->get_vault_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionid** | **str**| Subscription ID | 
 **start_time** | **str**| start time | [optional] 
 **end_time** | **str**| end time | [optional] 

### Return type

[**MetricsResponse**](MetricsResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vault_status**
> VaultStatus get_vault_status(subscriptionid)



Get vault status

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
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
    api_instance = OmniCore.VaultApi(api_client)
    subscriptionid = 'subscriptionid_example' # str | Subscription ID

    try:
        api_response = api_instance.get_vault_status(subscriptionid)
        print("The response of VaultApi->get_vault_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultApi->get_vault_status: %s\n" % e)
```

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
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
    api_instance = OmniCore.VaultApi(api_client)
    subscriptionid = 'subscriptionid_example' # str | Subscription ID

    try:
        api_response = api_instance.get_vault_status(subscriptionid)
        print("The response of VaultApi->get_vault_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultApi->get_vault_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionid** | **str**| Subscription ID | 

### Return type

[**VaultStatus**](VaultStatus.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_export**
> Frame start_export(subscriptionid, start_export_body=start_export_body)



Start Export

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
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
    api_instance = OmniCore.VaultApi(api_client)
    subscriptionid = 'subscriptionid_example' # str | Subscription ID
    start_export_body = OmniCore.StartExportBody() # StartExportBody | application/json (optional)

    try:
        api_response = api_instance.start_export(subscriptionid, start_export_body=start_export_body)
        print("The response of VaultApi->start_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultApi->start_export: %s\n" % e)
```

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
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
    api_instance = OmniCore.VaultApi(api_client)
    subscriptionid = 'subscriptionid_example' # str | Subscription ID
    start_export_body = OmniCore.StartExportBody() # StartExportBody | application/json (optional)

    try:
        api_response = api_instance.start_export(subscriptionid, start_export_body=start_export_body)
        print("The response of VaultApi->start_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultApi->start_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionid** | **str**| Subscription ID | 
 **start_export_body** | [**StartExportBody**](StartExportBody.md)| application/json | [optional] 

### Return type

[**Frame**](Frame.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_replay**
> str start_replay(subscriptionid, replay_body=replay_body)



Start Replay

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
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
    api_instance = OmniCore.VaultApi(api_client)
    subscriptionid = 'subscriptionid_example' # str | Subscription ID
    replay_body = OmniCore.ReplayBody() # ReplayBody | application/json (optional)

    try:
        api_response = api_instance.start_replay(subscriptionid, replay_body=replay_body)
        print("The response of VaultApi->start_replay:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultApi->start_replay: %s\n" % e)
```

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
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
    api_instance = OmniCore.VaultApi(api_client)
    subscriptionid = 'subscriptionid_example' # str | Subscription ID
    replay_body = OmniCore.ReplayBody() # ReplayBody | application/json (optional)

    try:
        api_response = api_instance.start_replay(subscriptionid, replay_body=replay_body)
        print("The response of VaultApi->start_replay:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultApi->start_replay: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionid** | **str**| Subscription ID | 
 **replay_body** | [**ReplayBody**](ReplayBody.md)| application/json | [optional] 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

