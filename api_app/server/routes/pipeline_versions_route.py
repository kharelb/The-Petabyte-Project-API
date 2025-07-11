from ..lib.lib_1 import *

from ..schemas.pipeline_versions_schema import *

router = APIRouter()


@router.post("/", response_description="Pipeline Versions data added to the database.")
async def add_data(data: PipelineVersions | List[PipelineVersions],
                   current_user: dict = Depends(get_current_user)) -> dict:
    inserted_ids = []
    if isinstance(data, PipelineVersions):
        insert_rawdata = await data.insert()
        inserted_ids.append(insert_rawdata.id)
    elif isinstance(data, list):
        for document in data:
            insert_data = await data.insert()
            inserted_ids.append(insert_data.id)
    return {"message": "Data added successfully", "inserted_id": inserted_ids}


# Get all the documents
@router.get("/", response_description="Pipeline Versions data records retrieved")
async def get_data(skip: int = 0, limit: int = 10,
                   current_user: dict = Depends(get_current_user)) -> List[RetrievePipelineVersions]:
    docs = await RetrievePipelineVersions.find_all().to_list()
    return docs[skip: skip + limit]


# Count the number of documents in the collection
@router.get("/count", response_description="Pipeline Versions Data counted")
async def get_data(current_user: dict = Depends(get_current_user)) -> dict:
    docs = await RetrievePipelineVersions.find_all().count()
    return {'total number of documents in pipeline_versions': docs}


# Search data by passing a dictionary.
@router.get("/search_data",
            response_description="Pipeline Versions data records by criteria")
async def get_data_by_criteria(docs: dict = None,
                               current_user: dict = Depends(get_current_user)) -> List[RetrievePipelineVersions]:
    data = await RetrievePipelineVersions.find(docs).to_list()
    return data

# Get the latest inserted document(only one document)
@router.get("/latest", response_description="Latest Pipeline Versions data record retrieved")
async def get_latest_data(current_user: dict = Depends(get_current_user)) -> List[RetrievePipelineVersions]:
    data = await RetrievePipelineVersions.find_all().sort([("_id", -1)]).limit(1).to_list()
    return data



# Get the documents from id
@router.get("/{id}", response_description="Processing Outcomes data record retrieved from id")
async def get_data_by_id(id: PydanticObjectId,
                         current_user: dict = Depends(get_current_user)) -> RetrievePipelineVersions:
    data = await RetrievePipelineVersions.get(id)
    if not data:
        raise HTTPException(
            status_code=404,
            detail=f"No document found with the given id:{id}"
        )
    else:
        return data


# Update the data (patching)
@router.patch("/{id}", response_description="Pipeline Versions record updated")
async def update_data_by_id(id: PydanticObjectId, req: UpdatePipelineVersions,
                            current_user: dict = Depends(get_current_user)) -> RetrievePipelineVersions:
    req = {k: v for k, v in req.dict().items() if v is not None}
    update_query = {"$set": {field: value for field, value in req.items()}}

    data = await RetrievePipelineVersions.get(id)
    if not data:
        raise HTTPException(
            status_code=404,
            detail='Pipeline Versions data record not found!'
        )

    await data.update(update_query)
    return data


@router.put("/{id}", response_description="Pipeline Versions data record updated")
async def update_data_by_id(id: PydanticObjectId, req: UpdatePipelineVersions,
                            current_user: dict = Depends(get_current_user)) -> UpdatePipelineVersions:
    req = {k: v for k, v in req.dict().items() if v is not None}
    update_query = {"$set": {field: value for field, value in req.items()}}

    data = await RetrievePipelineVersions.get(id)
    if not data:
        raise HTTPException(
            status_code=404,
            detail='Processing Outcomes data record not found!'
        )

    await data.update(update_query)
    return data


# Delete data using id
@router.delete("/{id}", response_description='Pipeline Versions data record has been deleted from the TPP database!')
async def delete_data(id: PydanticObjectId,
                      current_user: dict = Depends(get_current_user)) -> dict:
    data = await RetrievePipelineVersions.get(id)

    if not data:
        raise HTTPException(
            status_code=404,
            detail='Data not found!'
        )

    await data.delete()
    return {
        "message": "Pipeline Versions data record has been deleted successfully!"
    }
