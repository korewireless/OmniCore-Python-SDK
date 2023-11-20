# StartExportBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**destination** | **str** |  | [optional] 

## Example

```python
from OmniCore.models.start_export_body import StartExportBody

# TODO update the JSON string below
json = "{}"
# create an instance of StartExportBody from a JSON string
start_export_body_instance = StartExportBody.from_json(json)
# print the JSON string representation of the object
print StartExportBody.to_json()

# convert the object into a dict
start_export_body_dict = start_export_body_instance.to_dict()
# create an instance of StartExportBody from a dict
start_export_body_form_dict = start_export_body.from_dict(start_export_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


