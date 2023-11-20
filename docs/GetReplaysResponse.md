# GetReplaysResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**List[Replay]**](Replay.md) |  | [optional] 

## Example

```python
from OmniCore.models.get_replays_response import GetReplaysResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetReplaysResponse from a JSON string
get_replays_response_instance = GetReplaysResponse.from_json(json)
# print the JSON string representation of the object
print GetReplaysResponse.to_json()

# convert the object into a dict
get_replays_response_dict = get_replays_response_instance.to_dict()
# create an instance of GetReplaysResponse from a dict
get_replays_response_form_dict = get_replays_response.from_dict(get_replays_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


