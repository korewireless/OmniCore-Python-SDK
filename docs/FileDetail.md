# FileDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from OmniCore.models.file_detail import FileDetail

# TODO update the JSON string below
json = "{}"
# create an instance of FileDetail from a JSON string
file_detail_instance = FileDetail.from_json(json)
# print the JSON string representation of the object
print FileDetail.to_json()

# convert the object into a dict
file_detail_dict = file_detail_instance.to_dict()
# create an instance of FileDetail from a dict
file_detail_form_dict = file_detail.from_dict(file_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


