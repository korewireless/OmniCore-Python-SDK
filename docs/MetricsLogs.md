# MetricsLogs


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**no_of_files** | **int** |  | [optional] 
**file_size** | **float** |  | [optional] 
**noofoperations** | **int** |  | [optional] 
**updatedon** | **str** |  | [optional] 
**replay_file_size** | **float** |  | [optional] 
**export_file_size** | **float** |  | [optional] 

## Example

```python
from OmniCore.models.metrics_logs import MetricsLogs

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsLogs from a JSON string
metrics_logs_instance = MetricsLogs.from_json(json)
# print the JSON string representation of the object
print MetricsLogs.to_json()

# convert the object into a dict
metrics_logs_dict = metrics_logs_instance.to_dict()
# create an instance of MetricsLogs from a dict
metrics_logs_form_dict = metrics_logs.from_dict(metrics_logs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


