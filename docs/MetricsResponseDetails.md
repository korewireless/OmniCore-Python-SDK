# MetricsResponseDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **str** |  | [optional] 
**no_of_files** | **int** |  | [optional] 
**file_size** | **float** |  | [optional] 
**noofoperations** | **int** |  | [optional] 
**no_of_replays** | **int** |  | [optional] 
**no_of_exports** | **int** |  | [optional] 
**operations** | [**List[OperationMetrics]**](OperationMetrics.md) |  | [optional] 
**details_for_time_period** | [**MetricsData**](MetricsData.md) |  | [optional] 

## Example

```python
from OmniCore.models.metrics_response_details import MetricsResponseDetails

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsResponseDetails from a JSON string
metrics_response_details_instance = MetricsResponseDetails.from_json(json)
# print the JSON string representation of the object
print MetricsResponseDetails.to_json()

# convert the object into a dict
metrics_response_details_dict = metrics_response_details_instance.to_dict()
# create an instance of MetricsResponseDetails from a dict
metrics_response_details_form_dict = metrics_response_details.from_dict(metrics_response_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


