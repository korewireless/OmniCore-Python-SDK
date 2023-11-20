# FolderData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**List[Folder]**](Folder.md) |  | [optional] 

## Example

```python
from OmniCore.models.folder_data import FolderData

# TODO update the JSON string below
json = "{}"
# create an instance of FolderData from a JSON string
folder_data_instance = FolderData.from_json(json)
# print the JSON string representation of the object
print FolderData.to_json()

# convert the object into a dict
folder_data_dict = folder_data_instance.to_dict()
# create an instance of FolderData from a dict
folder_data_form_dict = folder_data.from_dict(folder_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


