# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3

from petstore_api import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401

# query params
SomeVarSchema = schemas.StrSchema
SomeVarSchema = schemas.StrSchema
SomeVarSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'someVar': typing.Union[SomeVarSchema, str, ],
        'SomeVar': typing.Union[SomeVarSchema, str, ],
        'some_var': typing.Union[SomeVarSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_some_var = api_client.QueryParameter(
    name="someVar",
    style=api_client.ParameterStyle.FORM,
    schema=SomeVarSchema,
    required=True,
    explode=True,
)
request_query_some_var2 = api_client.QueryParameter(
    name="SomeVar",
    style=api_client.ParameterStyle.FORM,
    schema=SomeVarSchema,
    required=True,
    explode=True,
)
request_query_some_var3 = api_client.QueryParameter(
    name="some_var",
    style=api_client.ParameterStyle.FORM,
    schema=SomeVarSchema,
    required=True,
    explode=True,
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
)


class BaseApi(api_client.Api):

    @typing.overload
    def _case_sensitive_params_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = False,
    ) -> typing.Union[
        ApiResponseFor200,
    ]:
        ...

    @typing.overload
    def _case_sensitive_params_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[True] = True,
    ) -> api_client.ApiResponseWithoutDeserialization:
        ...

    @typing.overload
    def _case_sensitive_params_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        ...

    def _case_sensitive_params_oapg(
        self,
        query_params = frozendict.frozendict(),
        stream = False,
        timeout = None,
        skip_deserialization = False,
    ):
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_some_var,
            request_query_some_var2,
            request_query_some_var3,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
        # TODO add cookie handling

        response = self.api_client.call_api(
            resource_path=used_path,
            method='put'.upper(),
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)

        return api_response


class CaseSensitiveParams(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def case_sensitive_params(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = False,
    ) -> typing.Union[
        ApiResponseFor200,
    ]:
        ...

    @typing.overload
    def case_sensitive_params(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[True] = True,
    ) -> api_client.ApiResponseWithoutDeserialization:
        ...

    @typing.overload
    def case_sensitive_params(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        ...

    def case_sensitive_params(
        self,
        query_params = frozendict.frozendict(),
        stream = False,
        timeout = None,
        skip_deserialization = False,
    ):
        return self._case_sensitive_params_oapg(
            query_params=query_params,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def put(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = False,
    ) -> typing.Union[
        ApiResponseFor200,
    ]:
        ...

    @typing.overload
    def put(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[True] = True,
    ) -> api_client.ApiResponseWithoutDeserialization:
        ...

    @typing.overload
    def put(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        ...

    def put(
        self,
        query_params = frozendict.frozendict(),
        stream = False,
        timeout = None,
        skip_deserialization = False,
    ):
        return self._case_sensitive_params_oapg(
            query_params=query_params,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


