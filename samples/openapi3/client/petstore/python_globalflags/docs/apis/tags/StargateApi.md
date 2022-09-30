<a name="__pageTop"></a>
# petstore_api.apis.tags.stargate_api.StargateApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jwks_stargate_neurodata_stargate_jwks_json_get**](#jwks_stargate_neurodata_stargate_jwks_json_get) | **get** /stargate/neurodata/stargate/jwks.json | Jwks
[**read_neuro_data_stargate_neurodata_stargate_read_neuro_data_json_get**](#read_neuro_data_stargate_neurodata_stargate_read_neuro_data_json_get) | **get** /stargate/neurodata/stargate/read_neuro_data.json | Read Neuro Data
[**upload_existing_dataset_stargate_neurodata_stargate_upload_existing_dataset_id_get**](#upload_existing_dataset_stargate_neurodata_stargate_upload_existing_dataset_id_get) | **get** /stargate/neurodata/stargate/upload/existing/{dataset_id} | Upload Existing Dataset
[**upload_new_dataset_stargate_neurodata_stargate_upload_new_post**](#upload_new_dataset_stargate_neurodata_stargate_upload_new_post) | **post** /stargate/neurodata/stargate/upload/new | Upload New Dataset
[**user_datasets_stargate_neurodata_dataset_my_datasets_get**](#user_datasets_stargate_neurodata_dataset_my_datasets_get) | **get** /stargate/neurodata/dataset/my_datasets | User Datasets
[**user_projects_stargate_neurodata_dataset_my_projects_get**](#user_projects_stargate_neurodata_dataset_my_projects_get) | **get** /stargate/neurodata/dataset/my_projects | User Projects

# **jwks_stargate_neurodata_stargate_jwks_json_get**
<a name="jwks_stargate_neurodata_stargate_jwks_json_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type jwks_stargate_neurodata_stargate_jwks_json_get()

Jwks

### Example

```python
import petstore_api
from petstore_api.apis.tags import stargate_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = petstore_api.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with petstore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stargate_api.StargateApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Jwks
        api_response = api_instance.jwks_stargate_neurodata_stargate_jwks_json_get()
        pprint(api_response)
    except petstore_api.ApiException as e:
        print("Exception when calling StargateApi->jwks_stargate_neurodata_stargate_jwks_json_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#jwks_stargate_neurodata_stargate_jwks_json_get.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#jwks_stargate_neurodata_stargate_jwks_json_get.ApiResponseFor404) | Not found

#### jwks_stargate_neurodata_stargate_jwks_json_get.ApiResponseFor200
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

#### jwks_stargate_neurodata_stargate_jwks_json_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **read_neuro_data_stargate_neurodata_stargate_read_neuro_data_json_get**
<a name="read_neuro_data_stargate_neurodata_stargate_read_neuro_data_json_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type read_neuro_data_stargate_neurodata_stargate_read_neuro_data_json_get()

Read Neuro Data

### Example

* Api Key Authentication (APIKeyCookie):
* OAuth Authentication (OAuth2PasswordBearer):
```python
import petstore_api
from petstore_api.apis.tags import stargate_api
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
    api_instance = stargate_api.StargateApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Read Neuro Data
        api_response = api_instance.read_neuro_data_stargate_neurodata_stargate_read_neuro_data_json_get()
        pprint(api_response)
    except petstore_api.ApiException as e:
        print("Exception when calling StargateApi->read_neuro_data_stargate_neurodata_stargate_read_neuro_data_json_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#read_neuro_data_stargate_neurodata_stargate_read_neuro_data_json_get.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#read_neuro_data_stargate_neurodata_stargate_read_neuro_data_json_get.ApiResponseFor404) | Not found

#### read_neuro_data_stargate_neurodata_stargate_read_neuro_data_json_get.ApiResponseFor200
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

#### read_neuro_data_stargate_neurodata_stargate_read_neuro_data_json_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKeyCookie](../../../README.md#APIKeyCookie), [OAuth2PasswordBearer](../../../README.md#OAuth2PasswordBearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **upload_existing_dataset_stargate_neurodata_stargate_upload_existing_dataset_id_get**
<a name="upload_existing_dataset_stargate_neurodata_stargate_upload_existing_dataset_id_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type upload_existing_dataset_stargate_neurodata_stargate_upload_existing_dataset_id_get(dataset_id)

Upload Existing Dataset

### Example

* Api Key Authentication (APIKeyCookie):
* OAuth Authentication (OAuth2PasswordBearer):
```python
import petstore_api
from petstore_api.apis.tags import stargate_api
from petstore_api.model.http_validation_error import HTTPValidationError
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
    api_instance = stargate_api.StargateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dataset_id': "dataset_id_example",
    }
    try:
        # Upload Existing Dataset
        api_response = api_instance.upload_existing_dataset_stargate_neurodata_stargate_upload_existing_dataset_id_get(
            path_params=path_params,
        )
        pprint(api_response)
    except petstore_api.ApiException as e:
        print("Exception when calling StargateApi->upload_existing_dataset_stargate_neurodata_stargate_upload_existing_dataset_id_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
dataset_id | DatasetIdSchema | | 

# DatasetIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#upload_existing_dataset_stargate_neurodata_stargate_upload_existing_dataset_id_get.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#upload_existing_dataset_stargate_neurodata_stargate_upload_existing_dataset_id_get.ApiResponseFor404) | Not found
422 | [ApiResponseFor422](#upload_existing_dataset_stargate_neurodata_stargate_upload_existing_dataset_id_get.ApiResponseFor422) | Validation Error

#### upload_existing_dataset_stargate_neurodata_stargate_upload_existing_dataset_id_get.ApiResponseFor200
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

#### upload_existing_dataset_stargate_neurodata_stargate_upload_existing_dataset_id_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### upload_existing_dataset_stargate_neurodata_stargate_upload_existing_dataset_id_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKeyCookie](../../../README.md#APIKeyCookie), [OAuth2PasswordBearer](../../../README.md#OAuth2PasswordBearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **upload_new_dataset_stargate_neurodata_stargate_upload_new_post**
<a name="upload_new_dataset_stargate_neurodata_stargate_upload_new_post"></a>
> bool, date, datetime, dict, float, int, list, str, none_type upload_new_dataset_stargate_neurodata_stargate_upload_new_post(create_dataset)

Upload New Dataset

### Example

* Api Key Authentication (APIKeyCookie):
* OAuth Authentication (OAuth2PasswordBearer):
```python
import petstore_api
from petstore_api.apis.tags import stargate_api
from petstore_api.model.http_validation_error import HTTPValidationError
from petstore_api.model.create_dataset import CreateDataset
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
    api_instance = stargate_api.StargateApi(api_client)

    # example passing only required values which don't have defaults set
    body = CreateDataset(
        upload_complete=False,
        dataset_size=-9.223372036854776E+18,
        label="label_example",
        notes="notes_example",
        project=SyndbApiNeurodataModelsProjectLeaf(
            id="id_example",
            doi="doi_example",
            label="label_example",
            notes="notes_example",
        ),
        animal=SyndbApiNeurodataModelsAnimalLeaf(
            species="species_example",
        ),
        brain_structure=SyndbApiNeurodataModelsBrainStructureLeaf(
            name="name_example",
        ),
        targeted_mutation=SyndbApiNeurodataModelsTargetedMutationLeaf(
            gene="gene_example",
            is_knock_in=False,
            method="method_example",
        ),
        microscopy_method=SyndbApiNeurodataModelsMicroscopyMethodLeaf(
            name="name_example",
        ),
    )
    try:
        # Upload New Dataset
        api_response = api_instance.upload_new_dataset_stargate_neurodata_stargate_upload_new_post(
            body=body,
        )
        pprint(api_response)
    except petstore_api.ApiException as e:
        print("Exception when calling StargateApi->upload_new_dataset_stargate_neurodata_stargate_upload_new_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateDataset**](../../models/CreateDataset.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#upload_new_dataset_stargate_neurodata_stargate_upload_new_post.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#upload_new_dataset_stargate_neurodata_stargate_upload_new_post.ApiResponseFor404) | Not found
422 | [ApiResponseFor422](#upload_new_dataset_stargate_neurodata_stargate_upload_new_post.ApiResponseFor422) | Validation Error

#### upload_new_dataset_stargate_neurodata_stargate_upload_new_post.ApiResponseFor200
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

#### upload_new_dataset_stargate_neurodata_stargate_upload_new_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### upload_new_dataset_stargate_neurodata_stargate_upload_new_post.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKeyCookie](../../../README.md#APIKeyCookie), [OAuth2PasswordBearer](../../../README.md#OAuth2PasswordBearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_datasets_stargate_neurodata_dataset_my_datasets_get**
<a name="user_datasets_stargate_neurodata_dataset_my_datasets_get"></a>
> SyndbApiNeurodataModelsDatasetLeafList user_datasets_stargate_neurodata_dataset_my_datasets_get()

User Datasets

### Example

* Api Key Authentication (APIKeyCookie):
* OAuth Authentication (OAuth2PasswordBearer):
```python
import petstore_api
from petstore_api.apis.tags import stargate_api
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
    api_instance = stargate_api.StargateApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # User Datasets
        api_response = api_instance.user_datasets_stargate_neurodata_dataset_my_datasets_get()
        pprint(api_response)
    except petstore_api.ApiException as e:
        print("Exception when calling StargateApi->user_datasets_stargate_neurodata_dataset_my_datasets_get: %s\n" % e)
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
from petstore_api.apis.tags import stargate_api
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
    api_instance = stargate_api.StargateApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # User Projects
        api_response = api_instance.user_projects_stargate_neurodata_dataset_my_projects_get()
        pprint(api_response)
    except petstore_api.ApiException as e:
        print("Exception when calling StargateApi->user_projects_stargate_neurodata_dataset_my_projects_get: %s\n" % e)
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

