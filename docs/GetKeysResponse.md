# GetKeysResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**List[VaultEncryptionKey]**](VaultEncryptionKey.md) |  | [optional] 

## Example

```python
from OmniCore.models.get_keys_response import GetKeysResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetKeysResponse from a JSON string
get_keys_response_instance = GetKeysResponse.from_json(json)
# print the JSON string representation of the object
print GetKeysResponse.to_json()

# convert the object into a dict
get_keys_response_dict = get_keys_response_instance.to_dict()
# create an instance of GetKeysResponse from a dict
get_keys_response_form_dict = get_keys_response.from_dict(get_keys_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


