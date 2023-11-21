# CreateVaultKeyBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**key** | **str** |  | [optional] 

## Example

```python
from OmniCore.models.create_vault_key_body import CreateVaultKeyBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVaultKeyBody from a JSON string
create_vault_key_body_instance = CreateVaultKeyBody.from_json(json)
# print the JSON string representation of the object
print CreateVaultKeyBody.to_json()

# convert the object into a dict
create_vault_key_body_dict = create_vault_key_body_instance.to_dict()
# create an instance of CreateVaultKeyBody from a dict
create_vault_key_body_form_dict = create_vault_key_body.from_dict(create_vault_key_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


