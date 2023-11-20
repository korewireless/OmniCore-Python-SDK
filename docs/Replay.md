# Replay


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**registry** | **str** |  | [optional] 
**start_time** | **int** |  | [optional] 
**end_time** | **int** |  | [optional] 
**subscription** | **str** |  | [optional] 
**destination** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from OmniCore.models.replay import Replay

# TODO update the JSON string below
json = "{}"
# create an instance of Replay from a JSON string
replay_instance = Replay.from_json(json)
# print the JSON string representation of the object
print Replay.to_json()

# convert the object into a dict
replay_dict = replay_instance.to_dict()
# create an instance of Replay from a dict
replay_form_dict = replay.from_dict(replay_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


