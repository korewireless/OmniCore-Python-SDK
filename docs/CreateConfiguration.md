# CreateConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from OmniCore.models.create_configuration import CreateConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConfiguration from a JSON string
create_configuration_instance = CreateConfiguration.from_json(json)
# print the JSON string representation of the object
print CreateConfiguration.to_json()

# convert the object into a dict
create_configuration_dict = create_configuration_instance.to_dict()
# create an instance of CreateConfiguration from a dict
create_configuration_form_dict = create_configuration.from_dict(create_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


