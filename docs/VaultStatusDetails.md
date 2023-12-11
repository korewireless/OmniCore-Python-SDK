# VaultStatusDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **str** |  | [optional] 
**storage_type** | **str** |  | [optional] 
**is_enabled** | **bool** |  | [optional] 
**is_created** | **bool** |  | [optional] 
**updatedon** | **str** |  | [optional] 
**created_on** | **str** |  | [optional] 
**mqtt_id** | **str** |  | [optional] 
**retention_period** | **int** |  | [optional] 
**encryption_key_id** | **int** |  | [optional] 
**is_encrypted** | **bool** |  | [optional] 

## Example

```python
from OmniCore.models.vault_status_details import VaultStatusDetails

# TODO update the JSON string below
json = "{}"
# create an instance of VaultStatusDetails from a JSON string
vault_status_details_instance = VaultStatusDetails.from_json(json)
# print the JSON string representation of the object
print VaultStatusDetails.to_json()

# convert the object into a dict
vault_status_details_dict = vault_status_details_instance.to_dict()
# create an instance of VaultStatusDetails from a dict
vault_status_details_form_dict = vault_status_details.from_dict(vault_status_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


