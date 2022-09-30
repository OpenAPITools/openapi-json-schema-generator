# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from petstore_api.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    USER_AUTH_JWT_LOGIN = "/user/auth/jwt/login"
    USER_AUTH_JWT_LOGOUT = "/user/auth/jwt/logout"
    USER_AUTH_DATABASE_LOGIN = "/user/auth/database/login"
    USER_AUTH_DATABASE_LOGOUT = "/user/auth/database/logout"
    USER_REGISTER = "/user/register"
    USER_REQUESTVERIFYTOKEN = "/user/request-verify-token"
    USER_VERIFY = "/user/verify"
    USER_PROFILE_JSON = "/user/profile.json"
    STARGATE_NEURODATA_STARGATE_UPLOAD_EXISTING_DATASET_ID = "/stargate/neurodata/stargate/upload/existing/{dataset_id}"
    STARGATE_NEURODATA_STARGATE_UPLOAD_NEW = "/stargate/neurodata/stargate/upload/new"
    STARGATE_NEURODATA_STARGATE_READ_NEURO_DATA_JSON = "/stargate/neurodata/stargate/read_neuro_data.json"
    STARGATE_NEURODATA_STARGATE_JWKS_JSON = "/stargate/neurodata/stargate/jwks.json"
    STARGATE_NEURODATA_DATASET_MY_DATASETS = "/stargate/neurodata/dataset/my_datasets"
    STARGATE_NEURODATA_DATASET_MY_PROJECTS = "/stargate/neurodata/dataset/my_projects"
    SOLIDUS = "/"
