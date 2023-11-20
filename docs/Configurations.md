# Configurations


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**List[Configuration]**](Configuration.md) |  | [optional] 

## Example

```python
from OmniCore.models.configurations import Configurations

# TODO update the JSON string below
json = "{}"
# create an instance of Configurations from a JSON string
configurations_instance = Configurations.from_json(json)
# print the JSON string representation of the object
print Configurations.to_json()

# convert the object into a dict
configurations_dict = configurations_instance.to_dict()
# create an instance of Configurations from a dict
configurations_form_dict = configurations.from_dict(configurations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


