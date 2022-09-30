import typing_extensions

from petstore_api.paths import PathValues
from petstore_api.apis.paths.user_auth_jwt_login import UserAuthJwtLogin
from petstore_api.apis.paths.user_auth_jwt_logout import UserAuthJwtLogout
from petstore_api.apis.paths.user_auth_database_login import UserAuthDatabaseLogin
from petstore_api.apis.paths.user_auth_database_logout import UserAuthDatabaseLogout
from petstore_api.apis.paths.user_register import UserRegister
from petstore_api.apis.paths.user_request_verify_token import UserRequestVerifyToken
from petstore_api.apis.paths.user_verify import UserVerify
from petstore_api.apis.paths.user_profile_json import UserProfileJson
from petstore_api.apis.paths.stargate_neurodata_stargate_upload_existing_dataset_id import StargateNeurodataStargateUploadExistingDatasetId
from petstore_api.apis.paths.stargate_neurodata_stargate_upload_new import StargateNeurodataStargateUploadNew
from petstore_api.apis.paths.stargate_neurodata_stargate_read_neuro_data_json import StargateNeurodataStargateReadNeuroDataJson
from petstore_api.apis.paths.stargate_neurodata_stargate_jwks_json import StargateNeurodataStargateJwksJson
from petstore_api.apis.paths.stargate_neurodata_dataset_my_datasets import StargateNeurodataDatasetMyDatasets
from petstore_api.apis.paths.stargate_neurodata_dataset_my_projects import StargateNeurodataDatasetMyProjects
from petstore_api.apis.paths. import 

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.USER_AUTH_JWT_LOGIN: UserAuthJwtLogin,
        PathValues.USER_AUTH_JWT_LOGOUT: UserAuthJwtLogout,
        PathValues.USER_AUTH_DATABASE_LOGIN: UserAuthDatabaseLogin,
        PathValues.USER_AUTH_DATABASE_LOGOUT: UserAuthDatabaseLogout,
        PathValues.USER_REGISTER: UserRegister,
        PathValues.USER_REQUESTVERIFYTOKEN: UserRequestVerifyToken,
        PathValues.USER_VERIFY: UserVerify,
        PathValues.USER_PROFILE_JSON: UserProfileJson,
        PathValues.STARGATE_NEURODATA_STARGATE_UPLOAD_EXISTING_DATASET_ID: StargateNeurodataStargateUploadExistingDatasetId,
        PathValues.STARGATE_NEURODATA_STARGATE_UPLOAD_NEW: StargateNeurodataStargateUploadNew,
        PathValues.STARGATE_NEURODATA_STARGATE_READ_NEURO_DATA_JSON: StargateNeurodataStargateReadNeuroDataJson,
        PathValues.STARGATE_NEURODATA_STARGATE_JWKS_JSON: StargateNeurodataStargateJwksJson,
        PathValues.STARGATE_NEURODATA_DATASET_MY_DATASETS: StargateNeurodataDatasetMyDatasets,
        PathValues.STARGATE_NEURODATA_DATASET_MY_PROJECTS: StargateNeurodataDatasetMyProjects,
        PathValues.SOLIDUS: ,
    }
)

path_to_api = PathToApi(
    {
        PathValues.USER_AUTH_JWT_LOGIN: UserAuthJwtLogin,
        PathValues.USER_AUTH_JWT_LOGOUT: UserAuthJwtLogout,
        PathValues.USER_AUTH_DATABASE_LOGIN: UserAuthDatabaseLogin,
        PathValues.USER_AUTH_DATABASE_LOGOUT: UserAuthDatabaseLogout,
        PathValues.USER_REGISTER: UserRegister,
        PathValues.USER_REQUESTVERIFYTOKEN: UserRequestVerifyToken,
        PathValues.USER_VERIFY: UserVerify,
        PathValues.USER_PROFILE_JSON: UserProfileJson,
        PathValues.STARGATE_NEURODATA_STARGATE_UPLOAD_EXISTING_DATASET_ID: StargateNeurodataStargateUploadExistingDatasetId,
        PathValues.STARGATE_NEURODATA_STARGATE_UPLOAD_NEW: StargateNeurodataStargateUploadNew,
        PathValues.STARGATE_NEURODATA_STARGATE_READ_NEURO_DATA_JSON: StargateNeurodataStargateReadNeuroDataJson,
        PathValues.STARGATE_NEURODATA_STARGATE_JWKS_JSON: StargateNeurodataStargateJwksJson,
        PathValues.STARGATE_NEURODATA_DATASET_MY_DATASETS: StargateNeurodataDatasetMyDatasets,
        PathValues.STARGATE_NEURODATA_DATASET_MY_PROJECTS: StargateNeurodataDatasetMyProjects,
        PathValues.SOLIDUS: ,
    }
)
