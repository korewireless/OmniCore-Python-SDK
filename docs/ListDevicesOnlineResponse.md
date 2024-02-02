# ListDevicesOnlineResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | [**List[DeviceOnline]**](DeviceOnline.md) |  | 
**page_number** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from OmniCore.models.list_devices_online_response import ListDevicesOnlineResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListDevicesOnlineResponse from a JSON string
list_devices_online_response_instance = ListDevicesOnlineResponse.from_json(json)
# print the JSON string representation of the object
print ListDevicesOnlineResponse.to_json()

# convert the object into a dict
list_devices_online_response_dict = list_devices_online_response_instance.to_dict()
# create an instance of ListDevicesOnlineResponse from a dict
list_devices_online_response_form_dict = list_devices_online_response.from_dict(list_devices_online_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


