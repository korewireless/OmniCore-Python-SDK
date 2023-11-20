# OperationMetrics


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**no_of_files** | **int** |  | [optional] 
**file_size** | **float** |  | [optional] 
**operation** | **str** |  | [optional] 
**noofoperations** | **int** |  | [optional] 
**updatedon** | **str** |  | [optional] 
**registryid** | **str** |  | [optional] 

## Example

```python
from OmniCore.models.operation_metrics import OperationMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of OperationMetrics from a JSON string
operation_metrics_instance = OperationMetrics.from_json(json)
# print the JSON string representation of the object
print OperationMetrics.to_json()

# convert the object into a dict
operation_metrics_dict = operation_metrics_instance.to_dict()
# create an instance of OperationMetrics from a dict
operation_metrics_form_dict = operation_metrics.from_dict(operation_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


