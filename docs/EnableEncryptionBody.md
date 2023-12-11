# EnableEncryptionBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**is_encrypted** | **bool** |  | [optional] 
**encryption_key_id** | **int** |  | [optional] 

## Example

```python
from OmniCore.models.enable_encryption_body import EnableEncryptionBody

# TODO update the JSON string below
json = "{}"
# create an instance of EnableEncryptionBody from a JSON string
enable_encryption_body_instance = EnableEncryptionBody.from_json(json)
# print the JSON string representation of the object
print EnableEncryptionBody.to_json()

# convert the object into a dict
enable_encryption_body_dict = enable_encryption_body_instance.to_dict()
# create an instance of EnableEncryptionBody from a dict
enable_encryption_body_form_dict = enable_encryption_body.from_dict(enable_encryption_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


