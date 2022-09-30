# petstore_api.model.create_dataset.CreateDataset

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**dataset_size** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**upload_complete** | bool,  | BoolClass,  |  | [optional] if omitted the server will use the default value of False
**label** | str,  | str,  |  | [optional] 
**notes** | None, str,  | NoneClass, str,  |  | [optional] 
**project** | [**SyndbApiNeurodataModelsProjectLeaf**](SyndbApiNeurodataModelsProjectLeaf.md) | [**SyndbApiNeurodataModelsProjectLeaf**](SyndbApiNeurodataModelsProjectLeaf.md) |  | [optional] 
**animal** | [**SyndbApiNeurodataModelsAnimalLeaf**](SyndbApiNeurodataModelsAnimalLeaf.md) | [**SyndbApiNeurodataModelsAnimalLeaf**](SyndbApiNeurodataModelsAnimalLeaf.md) |  | [optional] 
**brain_structure** | [**SyndbApiNeurodataModelsBrainStructureLeaf**](SyndbApiNeurodataModelsBrainStructureLeaf.md) | [**SyndbApiNeurodataModelsBrainStructureLeaf**](SyndbApiNeurodataModelsBrainStructureLeaf.md) |  | [optional] 
**targeted_mutation** | [**SyndbApiNeurodataModelsTargetedMutationLeaf**](SyndbApiNeurodataModelsTargetedMutationLeaf.md) | [**SyndbApiNeurodataModelsTargetedMutationLeaf**](SyndbApiNeurodataModelsTargetedMutationLeaf.md) |  | [optional] 
**microscopy_method** | [**SyndbApiNeurodataModelsMicroscopyMethodLeaf**](SyndbApiNeurodataModelsMicroscopyMethodLeaf.md) | [**SyndbApiNeurodataModelsMicroscopyMethodLeaf**](SyndbApiNeurodataModelsMicroscopyMethodLeaf.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

