# VaultEncryptionKey


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**key** | **str** |  | [optional] 

## Example

```python
from OmniCore.models.vault_encryption_key import VaultEncryptionKey

# TODO update the JSON string below
json = "{}"
# create an instance of VaultEncryptionKey from a JSON string
vault_encryption_key_instance = VaultEncryptionKey.from_json(json)
# print the JSON string representation of the object
print VaultEncryptionKey.to_json()

# convert the object into a dict
vault_encryption_key_dict = vault_encryption_key_instance.to_dict()
# create an instance of VaultEncryptionKey from a dict
vault_encryption_key_form_dict = vault_encryption_key.from_dict(vault_encryption_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


