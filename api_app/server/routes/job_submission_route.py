from ..lib.lib_1 import *

from ..schemas.job_submission_schema import *

router = APIRouter()


@router.post("/", response_description="Job Submissions data added to the database.")
async def add_data(data: JobSubmissions | List[JobSubmissions],
                   current_user: dict = Depends(get_current_user)) -> dict:
    inserted_ids = []
    if isinstance(data, JobSubmissions):
        insert_rawdata = await data.insert()
        inserted_ids.append(insert_rawdata.id)
    elif isinstance(data, list):
        for document in data:
            insert_data = await data.insert()
            inserted_ids.append(insert_data.id)
    return {"message": "Data added successfully", "inserted_id": inserted_ids}


# Get all the documents
@router.get("/", response_description="Job submissions data records retrieved")
async def get_data(skip: int = 0, limit: int = 10,
                   current_user: dict = Depends(get_current_user)) -> List[RetrieveJobSubmissions]:
    docs = await RetrieveJobSubmissions.find_all().to_list()
    return docs[skip: skip + limit]


# Count the number of documents in the collection
@router.get("/count", response_description="Job Submissions Data counted")
async def get_data(current_user: dict = Depends(get_current_user)) -> dict:
    docs = await RetrieveJobSubmissions.find_all().count()
    return {'total number of documents in job_submissions': docs}


# Search data by passing a dictionary.
@router.get("/search_data",
            response_description="Job Submissions data records by criteria")
async def get_data_by_criteria(docs: dict = None,
                               current_user: dict = Depends(get_current_user)) -> List[RetrieveJobSubmissions]:
    data = await RetrieveJobSubmissions.find(docs).to_list()
    return data


# Get the documents from id
@router.get("/{id}", response_description="Job Submissions data record retrieved from id")
async def get_data_by_id(id: PydanticObjectId,
                         current_user: dict = Depends(get_current_user)) -> RetrieveJobSubmissions:
    data = await RetrieveJobSubmissions.get(id)
    if not data:
        raise HTTPException(
            status_code=404,
            detail=f"No document found with the given id:{id}"
        )
    else:
        return data


# Update the data (patching)
@router.patch("/{id}", response_description="Job Submissions record updated")
async def update_data_by_id(id: PydanticObjectId, req: UpdateJobSubmissions,
                            current_user: dict = Depends(get_current_user)) -> RetrieveJobSubmissions:
    req = {k: v for k, v in req.dict().items() if v is not None}
    update_query = {"$set": {field: value for field, value in req.items()}}

    data = await RetrieveJobSubmissions.get(id)
    if not data:
        raise HTTPException(
            status_code=404,
            detail='Job Submissions data record not found!'
        )

    await data.update(update_query)
    return data


@router.put("/{id}", response_description="Job Submissions data record updated")
async def update_data_by_id(id: PydanticObjectId, req: UpdateJobSubmissions,
                            current_user: dict = Depends(get_current_user)) -> RetrieveJobSubmissions:
    req = {k: v for k, v in req.dict().items() if v is not None}
    update_query = {"$set": {field: value for field, value in req.items()}}

    data = await RetrieveJobSubmissions.get(id)
    if not data:
        raise HTTPException(
            status_code=404,
            detail='Job Submissions data record not found!'
        )

    await data.update(update_query)
    return data


# Delete data using id
@router.delete("/{id}", response_description='Job Submissions data record has been deleted from the TPP database!')
async def delete_data(id: PydanticObjectId,
                      current_user: dict = Depends(get_current_user)) -> dict:
    data = await RetrieveJobSubmissions.get(id)

    if not data:
        raise HTTPException(
            status_code=404,
            detail='Data not found!'
        )

    await data.delete()
    return {
        "message": "Job Submissions data  record has been deleted successfully!"
    }
