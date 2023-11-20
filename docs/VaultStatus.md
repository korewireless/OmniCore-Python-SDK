# VaultStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**VaultStatusDetails**](VaultStatusDetails.md) |  | [optional] 

## Example

```python
from OmniCore.models.vault_status import VaultStatus

# TODO update the JSON string below
json = "{}"
# create an instance of VaultStatus from a JSON string
vault_status_instance = VaultStatus.from_json(json)
# print the JSON string representation of the object
print VaultStatus.to_json()

# convert the object into a dict
vault_status_dict = vault_status_instance.to_dict()
# create an instance of VaultStatus from a dict
vault_status_form_dict = vault_status.from_dict(vault_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


