# AuditResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audit** | [**List[Audit]**](Audit.md) |  | [optional] 
**total_count** | **int** |  | [optional] 
**page_number** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 

## Example

```python
from OmniCore.models.audit_result import AuditResult

# TODO update the JSON string below
json = "{}"
# create an instance of AuditResult from a JSON string
audit_result_instance = AuditResult.from_json(json)
# print the JSON string representation of the object
print AuditResult.to_json()

# convert the object into a dict
audit_result_dict = audit_result_instance.to_dict()
# create an instance of AuditResult from a dict
audit_result_form_dict = audit_result.from_dict(audit_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


