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


class SyndbApiNeurodataModelsAnimalLeaf(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "species",
        }
        
        class properties:
            
            
            class species(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 200
            __annotations__ = {
                "species": species,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    species: MetaOapg.properties.species
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["species"]) -> MetaOapg.properties.species: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["species"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["species"]) -> MetaOapg.properties.species: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["species"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        species: typing.Union[MetaOapg.properties.species, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SyndbApiNeurodataModelsAnimalLeaf':
        return super().__new__(
            cls,
            *args,
            species=species,
            _configuration=_configuration,
        )
