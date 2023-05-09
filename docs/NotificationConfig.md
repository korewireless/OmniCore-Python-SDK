# NotificationConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pubsub_topic_name** | **str** | PubsubTopicName: A Topic name. For example, &#x60;projects/myProject/topics/deviceEvents&#x60;. | [optional] 
**is_gcp_pub_sub** | [**Bool**](Bool.md) | Describe whether the topic is Gcp pubsub topic or Omni topic | [optional] 

## Example

```python
from OmniCore.models.notification_config import NotificationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationConfig from a JSON string
notification_config_instance = NotificationConfig.from_json(json)
# print the JSON string representation of the object
print NotificationConfig.to_json()

# convert the object into a dict
notification_config_dict = notification_config_instance.to_dict()
# create an instance of NotificationConfig from a dict
notification_config_form_dict = notification_config.from_dict(notification_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


