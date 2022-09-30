# coding: utf-8

"""
    Synapse DB

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.4.1
    Generated by: https://openapi-generator.tech
"""

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


class SyndbApiNeurodataModelsTargetedMutationLeaf(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "method",
            "gene",
        }
        
        class properties:
            
            
            class gene(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 80
            
            
            class method(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 200
            is_knock_in = schemas.BoolSchema
            __annotations__ = {
                "gene": gene,
                "method": method,
                "is_knock_in": is_knock_in,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    method: MetaOapg.properties.method
    gene: MetaOapg.properties.gene
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["method"]) -> MetaOapg.properties.method: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gene"]) -> MetaOapg.properties.gene: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_knock_in"]) -> MetaOapg.properties.is_knock_in: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["method"], typing_extensions.Literal["gene"], typing_extensions.Literal["is_knock_in"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["method"]) -> MetaOapg.properties.method: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gene"]) -> MetaOapg.properties.gene: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_knock_in"]) -> typing.Union[MetaOapg.properties.is_knock_in, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["method"], typing_extensions.Literal["gene"], typing_extensions.Literal["is_knock_in"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        method: typing.Union[MetaOapg.properties.method, str, ],
        gene: typing.Union[MetaOapg.properties.gene, str, ],
        is_knock_in: typing.Union[MetaOapg.properties.is_knock_in, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SyndbApiNeurodataModelsTargetedMutationLeaf':
        return super().__new__(
            cls,
            *args,
            method=method,
            gene=gene,
            is_knock_in=is_knock_in,
            _configuration=_configuration,
        )
