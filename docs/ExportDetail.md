# ExportDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**destination** | **str** |  | [optional] 
**created_on** | **str** |  | [optional] 
**nooffiles** | **int** |  | [optional] 
**file_size** | **float** |  | [optional] 
**done** | **bool** |  | [optional] 

## Example

```python
from OmniCore.models.export_detail import ExportDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ExportDetail from a JSON string
export_detail_instance = ExportDetail.from_json(json)
# print the JSON string representation of the object
print ExportDetail.to_json()

# convert the object into a dict
export_detail_dict = export_detail_instance.to_dict()
# create an instance of ExportDetail from a dict
export_detail_form_dict = export_detail.from_dict(export_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


