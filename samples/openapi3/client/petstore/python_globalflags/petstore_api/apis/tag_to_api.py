import typing_extensions

from petstore_api.apis.tags import TagValues
from petstore_api.apis.tags.user_api import UserApi
from petstore_api.apis.tags.database_api import DatabaseApi
from petstore_api.apis.tags.auth_api import AuthApi
from petstore_api.apis.tags.jwt_api import JwtApi
from petstore_api.apis.tags.stargate_api import StargateApi
from petstore_api.apis.tags.data_api import DataApi
from petstore_api.apis.tags.default_api import DefaultApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.USER: UserApi,
        TagValues.DATABASE: DatabaseApi,
        TagValues.AUTH: AuthApi,
        TagValues.JWT: JwtApi,
        TagValues.STARGATE: StargateApi,
        TagValues.DATA: DataApi,
        TagValues.DEFAULT: DefaultApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.USER: UserApi,
        TagValues.DATABASE: DatabaseApi,
        TagValues.AUTH: AuthApi,
        TagValues.JWT: JwtApi,
        TagValues.STARGATE: StargateApi,
        TagValues.DATA: DataApi,
        TagValues.DEFAULT: DefaultApi,
    }
)
