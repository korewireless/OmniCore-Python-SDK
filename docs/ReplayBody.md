# ReplayBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registry** | **str** |  | [optional] 
**start_time** | **int** |  | [optional] 
**end_time** | **int** |  | [optional] 
**destination** | **str** |  | [optional] 
**source** | **str** |  | [optional] 

## Example

```python
from OmniCore.models.replay_body import ReplayBody

# TODO update the JSON string below
json = "{}"
# create an instance of ReplayBody from a JSON string
replay_body_instance = ReplayBody.from_json(json)
# print the JSON string representation of the object
print ReplayBody.to_json()

# convert the object into a dict
replay_body_dict = replay_body_instance.to_dict()
# create an instance of ReplayBody from a dict
replay_body_form_dict = replay_body.from_dict(replay_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


