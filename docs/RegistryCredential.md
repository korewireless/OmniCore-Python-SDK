# RegistryCredential


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_key_certificate** | [**PublicKeyCertificate**](PublicKeyCertificate.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 

## Example

```python
from OmniCore.models.registry_credential import RegistryCredential

# TODO update the JSON string below
json = "{}"
# create an instance of RegistryCredential from a JSON string
registry_credential_instance = RegistryCredential.from_json(json)
# print the JSON string representation of the object
print RegistryCredential.to_json()

# convert the object into a dict
registry_credential_dict = registry_credential_instance.to_dict()
# create an instance of RegistryCredential from a dict
registry_credential_form_dict = registry_credential.from_dict(registry_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


