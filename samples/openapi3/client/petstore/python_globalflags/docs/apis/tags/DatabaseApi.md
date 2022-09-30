<a name="__pageTop"></a>
# petstore_api.apis.tags.database_api.DatabaseApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_database_login_user_auth_database_login_post**](#auth_database_login_user_auth_database_login_post) | **post** /user/auth/database/login | Auth:Database.Login
[**auth_database_logout_user_auth_database_logout_post**](#auth_database_logout_user_auth_database_logout_post) | **post** /user/auth/database/logout | Auth:Database.Logout

# **auth_database_login_user_auth_database_login_post**
<a name="auth_database_login_user_auth_database_login_post"></a>
> bool, date, datetime, dict, float, int, list, str, none_type auth_database_login_user_auth_database_login_post()

Auth:Database.Login

### Example

```python
import petstore_api
from petstore_api.apis.tags import database_api
from petstore_api.model.body_auth_database_login_user_auth_database_login_post import BodyAuthDatabaseLoginUserAuthDatabaseLoginPost
from petstore_api.model.http_validation_error import HTTPValidationError
from petstore_api.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = petstore_api.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with petstore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = database_api.DatabaseApi(api_client)

    # example passing only optional values
    body = dict(
        grant_type="password",
        username="username_example",
        password="password_example",
        scope="",
        client_id="client_id_example",
        client_secret="client_secret_example",
    )
    try:
        # Auth:Database.Login
        api_response = api_instance.auth_database_login_user_auth_database_login_post(
            body=body,
        )
        pprint(api_response)
    except petstore_api.ApiException as e:
        print("Exception when calling DatabaseApi->auth_database_login_user_auth_database_login_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/x-www-form-urlencoded' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**BodyAuthDatabaseLoginUserAuthDatabaseLoginPost**](../../models/BodyAuthDatabaseLoginUserAuthDatabaseLoginPost.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#auth_database_login_user_auth_database_login_post.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#auth_database_login_user_auth_database_login_post.ApiResponseFor404) | Not found
400 | [ApiResponseFor400](#auth_database_login_user_auth_database_login_post.ApiResponseFor400) | Bad Request
204 | [ApiResponseFor204](#auth_database_login_user_auth_database_login_post.ApiResponseFor204) | No Content
422 | [ApiResponseFor422](#auth_database_login_user_auth_database_login_post.ApiResponseFor422) | Validation Error

#### auth_database_login_user_auth_database_login_post.ApiResponseFor200
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

#### auth_database_login_user_auth_database_login_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### auth_database_login_user_auth_database_login_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### auth_database_login_user_auth_database_login_post.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### auth_database_login_user_auth_database_login_post.ApiResponseFor422
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

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **auth_database_logout_user_auth_database_logout_post**
<a name="auth_database_logout_user_auth_database_logout_post"></a>
> bool, date, datetime, dict, float, int, list, str, none_type auth_database_logout_user_auth_database_logout_post()

Auth:Database.Logout

### Example

* Api Key Authentication (APIKeyCookie):
* OAuth Authentication (OAuth2PasswordBearer):
```python
import petstore_api
from petstore_api.apis.tags import database_api
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
    api_instance = database_api.DatabaseApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Auth:Database.Logout
        api_response = api_instance.auth_database_logout_user_auth_database_logout_post()
        pprint(api_response)
    except petstore_api.ApiException as e:
        print("Exception when calling DatabaseApi->auth_database_logout_user_auth_database_logout_post: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#auth_database_logout_user_auth_database_logout_post.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#auth_database_logout_user_auth_database_logout_post.ApiResponseFor404) | Not found
401 | [ApiResponseFor401](#auth_database_logout_user_auth_database_logout_post.ApiResponseFor401) | Missing token or inactive user.

#### auth_database_logout_user_auth_database_logout_post.ApiResponseFor200
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

#### auth_database_logout_user_auth_database_logout_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### auth_database_logout_user_auth_database_logout_post.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[APIKeyCookie](../../../README.md#APIKeyCookie), [OAuth2PasswordBearer](../../../README.md#OAuth2PasswordBearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

