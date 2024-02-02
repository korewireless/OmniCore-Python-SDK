# DeviceOnline


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**registry** | **str** |  | [optional] [readonly] 
**client_online** | **bool** |  | [optional] [readonly] 
**last_heartbeat_time** | **str** |  | [optional] [readonly] 
**subscription** | **str** |  | [optional] [readonly] 

## Example

```python
from OmniCore.models.device_online import DeviceOnline

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceOnline from a JSON string
device_online_instance = DeviceOnline.from_json(json)
# print the JSON string representation of the object
print DeviceOnline.to_json()

# convert the object into a dict
device_online_dict = device_online_instance.to_dict()
# create an instance of DeviceOnline from a dict
device_online_form_dict = device_online.from_dict(device_online_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


