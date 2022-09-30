<a name="__pageTop"></a>
# petstore_api.apis.tags.data_api.DataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_datasets_stargate_neurodata_dataset_my_datasets_get**](#user_datasets_stargate_neurodata_dataset_my_datasets_get) | **get** /stargate/neurodata/dataset/my_datasets | User Datasets
[**user_projects_stargate_neurodata_dataset_my_projects_get**](#user_projects_stargate_neurodata_dataset_my_projects_get) | **get** /stargate/neurodata/dataset/my_projects | User Projects

# **user_datasets_stargate_neurodata_dataset_my_datasets_get**
<a name="user_datasets_stargate_neurodata_dataset_my_datasets_get"></a>
> SyndbApiNeurodataModelsDatasetLeafList user_datasets_stargate_neurodata_dataset_my_datasets_get()

User Datasets

### Example

* Api Key Authentication (APIKeyCookie):
* OAuth Authentication (OAuth2PasswordBearer):
```python
import petstore_api
from petstore_api.apis.tags import data_api
from petstore_api.model.syndb_api_neurodata_models_dataset_leaf_list import SyndbApiNeurodataModelsDatasetLeafList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = petstore_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyCookie
configuration.api_key['APIKeyCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyCookie'] = 'Bearer'

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = petstore_api.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with petstore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_api.DataApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # User Datasets
        api_response = api_instance.user_datasets_stargate_neurodata_dataset_my_datasets_get()
        pprint(api_response)
    except petstore_api.ApiException as e:
        print("Exception when calling DataApi->user_datasets_stargate_neurodata_dataset_my_datasets_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_datasets_stargate_neurodata_dataset_my_datasets_get.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#user_datasets_stargate_neurodata_dataset_my_datasets_get.ApiResponseFor404) | Not found

#### user_datasets_stargate_neurodata_dataset_my_datasets_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SyndbApiNeurodataModelsDatasetLeafList**](../../models/SyndbApiNeurodataModelsDatasetLeafList.md) |  | 


#### user_datasets_stargate_neurodata_dataset_my_datasets_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKeyCookie](../../../README.md#APIKeyCookie), [OAuth2PasswordBearer](../../../README.md#OAuth2PasswordBearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_projects_stargate_neurodata_dataset_my_projects_get**
<a name="user_projects_stargate_neurodata_dataset_my_projects_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type user_projects_stargate_neurodata_dataset_my_projects_get()

User Projects

### Example

* Api Key Authentication (APIKeyCookie):
* OAuth Authentication (OAuth2PasswordBearer):
```python
import petstore_api
from petstore_api.apis.tags import data_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = petstore_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyCookie
configuration.api_key['APIKeyCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyCookie'] = 'Bearer'

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = petstore_api.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with petstore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_api.DataApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # User Projects
        api_response = api_instance.user_projects_stargate_neurodata_dataset_my_projects_get()
        pprint(api_response)
    except petstore_api.ApiException as e:
        print("Exception when calling DataApi->user_projects_stargate_neurodata_dataset_my_projects_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_projects_stargate_neurodata_dataset_my_projects_get.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#user_projects_stargate_neurodata_dataset_my_projects_get.ApiResponseFor404) | Not found

#### user_projects_stargate_neurodata_dataset_my_projects_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### user_projects_stargate_neurodata_dataset_my_projects_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKeyCookie](../../../README.md#APIKeyCookie), [OAuth2PasswordBearer](../../../README.md#OAuth2PasswordBearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

