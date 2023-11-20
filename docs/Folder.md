# Folder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**no_of_files** | **int** |  | [optional] 
**file_size** | **float** |  | [optional] 
**noofoperations** | **int** |  | [optional] 
**updatedon** | **str** |  | [optional] 
**registryid** | **str** |  | [optional] 

## Example

```python
from OmniCore.models.folder import Folder

# TODO update the JSON string below
json = "{}"
# create an instance of Folder from a JSON string
folder_instance = Folder.from_json(json)
# print the JSON string representation of the object
print Folder.to_json()

# convert the object into a dict
folder_dict = folder_instance.to_dict()
# create an instance of Folder from a dict
folder_form_dict = folder.from_dict(folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


