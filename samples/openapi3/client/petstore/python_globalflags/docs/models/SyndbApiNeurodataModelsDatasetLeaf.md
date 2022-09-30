# petstore_api.model.syndb_api_neurodata_models_dataset_leaf.SyndbApiNeurodataModelsDatasetLeaf

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**brain_structure_name** | str,  | str,  |  | 
**microscopy_method_name** | str,  | str,  |  | 
**animal_species** | str,  | str,  |  | 
**[targeted_mutation_names](#targeted_mutation_names)** | list, tuple,  | tuple,  |  | 
**dataset_size** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**upload_complete** | bool,  | BoolClass,  |  | [optional] if omitted the server will use the default value of False
**label** | str,  | str,  |  | [optional] 
**notes** | None, str,  | NoneClass, str,  |  | [optional] 

# targeted_mutation_names

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

