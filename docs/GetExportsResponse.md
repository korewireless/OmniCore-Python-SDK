# GetExportsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**List[ExportDetail]**](ExportDetail.md) |  | [optional] 

## Example

```python
from OmniCore.models.get_exports_response import GetExportsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetExportsResponse from a JSON string
get_exports_response_instance = GetExportsResponse.from_json(json)
# print the JSON string representation of the object
print GetExportsResponse.to_json()

# convert the object into a dict
get_exports_response_dict = get_exports_response_instance.to_dict()
# create an instance of GetExportsResponse from a dict
get_exports_response_form_dict = get_exports_response.from_dict(get_exports_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


