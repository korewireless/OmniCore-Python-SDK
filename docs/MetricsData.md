# MetricsData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MetricsLogs]**](MetricsLogs.md) |  | [optional] 
**total_export_size** | **float** |  | [optional] 
**total_replay_size** | **float** |  | [optional] 

## Example

```python
from OmniCore.models.metrics_data import MetricsData

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsData from a JSON string
metrics_data_instance = MetricsData.from_json(json)
# print the JSON string representation of the object
print MetricsData.to_json()

# convert the object into a dict
metrics_data_dict = metrics_data_instance.to_dict()
# create an instance of MetricsData from a dict
metrics_data_form_dict = metrics_data.from_dict(metrics_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


