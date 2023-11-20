# VaultConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**subscription** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**data** | **str** |  | [optional] 

## Example

```python
from OmniCore.models.vault_configuration import VaultConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of VaultConfiguration from a JSON string
vault_configuration_instance = VaultConfiguration.from_json(json)
# print the JSON string representation of the object
print VaultConfiguration.to_json()

# convert the object into a dict
vault_configuration_dict = vault_configuration_instance.to_dict()
# create an instance of VaultConfiguration from a dict
vault_configuration_form_dict = vault_configuration.from_dict(vault_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


