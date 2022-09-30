# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from petstore_api.paths.user_auth_database_login import Api

from petstore_api.paths import PathValues

path = PathValues.USER_AUTH_DATABASE_LOGIN