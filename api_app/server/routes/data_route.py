from ..lib.lib_1 import *

from ..schemas.data_schema import *

router = APIRouter()


@router.post("/", response_description="Raw data added to the database.")
async def add_data(data: Data | List[Data],
                   current_user: dict = Depends(get_current_user)) -> dict:
    inserted_ids = []
    if isinstance(data, Data):
        insert_rawdata = await data.insert()
        inserted_ids.append(insert_rawdata.id)
    elif isinstance(data, list):
        for document in data:
            insert_data = await data.insert()
            inserted_ids.append(insert_data.id)
    return {"message": "Data added successfully", "inserted_id": inserted_ids}


# Get all the raw_data documents
@router.get("/", response_description="Data records retrieved")
async def get_data(skip: int = 0, limit: int = 10,
                   current_user: dict = Depends(get_current_user)) -> List[RetrieveData]:
    docs = await RetrieveData.find_all().to_list()
    return docs[skip: skip + limit]


# Count the number of documents in the collection
@router.get("/count", response_description="Data counted")
async def get_data(current_user: dict = Depends(get_current_user)) -> dict:
    docs = await RetrieveData.find_all().count()
    return {'total number of documents in data': docs}


# Search data by passing a dictionary.
@router.get("/search_data",
            response_description="Data records by criteria")
async def get_data_by_criteria(docs: dict = None,
                               current_user: dict = Depends(get_current_user)) -> List[RetrieveData]:
    data = await RetrieveData.find(docs).to_list()
    return data


# Get the raw_data documents from id
@router.get("/{id}", response_description="Data record retrieved from id")
async def get_data_by_id(id: PydanticObjectId,
                         current_user: dict = Depends(get_current_user)) -> RetrieveData:
    data = await RetrieveData.get(id)
    if not data:
        raise HTTPException(
            status_code=404,
            detail=f"No document found with the given id:{id}"
        )
    else:
        return data


# Update the data documents(patching)
@router.patch("/{id}", response_description="Data record updated")
async def update_data_by_id(id: PydanticObjectId, req: UpdateData,
                            current_user: dict = Depends(get_current_user)) -> RetrieveData:
    req = {k: v for k, v in req.dict().items() if v is not None}
    update_query = {"$set": {field: value for field, value in req.items()}}

    data = await RetrieveData.get(id)
    if not data:
        raise HTTPException(
            status_code=404,
            detail='raw_data record not found!'
        )

    await data.update(update_query)
    return data


@router.put("/{id}", response_description="Data record updated")
async def update_data_by_id(id: PydanticObjectId, req: UpdateData,
                            current_user: dict = Depends(get_current_user)) -> RetrieveData:
    req = {k: v for k, v in req.dict().items() if v is not None}
    update_query = {"$set": {field: value for field, value in req.items()}}

    data = await RetrieveData.get(id)
    if not data:
        raise HTTPException(
            status_code=404,
            detail='data record not found!'
        )

    await data.update(update_query)
    return data


# Delete raw data using id
@router.delete("/{id}", response_description='data record has been deleted from the TPP database!')
async def delete_data(id: PydanticObjectId,
                      current_user: dict = Depends(get_current_user)) -> dict:
    data = await RetrieveData.get(id)

    if not data:
        raise HTTPException(
            status_code=404,
            detail='raw_data not found!'
        )

    await data.delete()
    return {
        "message": "data record has been deleted successfully!"
    }
