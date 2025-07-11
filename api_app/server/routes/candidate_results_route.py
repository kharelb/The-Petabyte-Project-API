from ..lib.lib_1 import *

from ..schemas.candidate_results_schema import *


router = APIRouter()


@router.post("/", response_description="Documents added to the database.")
async def add_data(insert_doc: CandidateResults | List[CandidateResults],
                   current_user: dict = Depends(get_current_user)) -> dict:
    try:
        inserted_ids = []
        if isinstance(insert_doc, CandidateResults):
            insert_survey = await insert_doc.insert()
            inserted_ids.append(insert_survey.id)
        elif isinstance(insert_doc, list):
            for document in insert_doc:
                insert_data = await insert_doc.insert()
                inserted_ids.append(insert_data.id)
        return {"message": "Document(s) added successfully", "inserted_id": inserted_ids}

    except DuplicateKeyError:
        return {"error": "Document(s) with the same name already exists."}


# Get all the candidate_results documents
@router.get("/", response_description="Records retrieved")
async def get_data(skip: int = 0, limit: int = 10,
                   current_user: dict = Depends(get_current_user)) -> List[RetrieveCandidateResults]:
    docs = await RetrieveCandidateResults.find_all().to_list()
    return docs[skip: skip + limit]


# Count the number of documents in the collection
@router.get("/count", response_description="Documents counted")
async def get_data(current_user: dict = Depends(get_current_user)) -> dict:
    docs = await RetrieveCandidateResults.find_all().count()
    return {'total number of documents in the collection is': docs}


# Search data by passing a dictionary.
@router.get("/search_data",
            response_description="Search documents by criteria")
async def get_survey_by_criteria(docs: dict = None,
                                 current_user: dict = Depends(get_current_user)) -> List[RetrieveCandidateResults]:
    survey = await RetrieveCandidateResults.find(docs).to_list()
    return survey


# Get the candidate_results from id.
@router.get("/{id}", response_description="Record retrieved from id")
async def get_survey_by_id(id: PydanticObjectId,
                           current_user: dict = Depends(get_current_user)) -> RetrieveCandidateResults:
    data = await RetrieveCandidateResults.get(id)
    if not data:
        raise HTTPException(
            status_code=404,
            detail=f"No document found with the given id:{id}"
        )
    else:
        return data


# Update the data documents(patching)
@router.patch("/{id}", response_description="Record updated")
async def update_data_by_id(id: PydanticObjectId, req: UpdateCandidateResults,
                            current_user: dict = Depends(get_current_user)) -> RetrieveCandidateResults:
    try:
        req = {k: v for k, v in req.dict().items() if v is not None}
        update_query = {"$set": {field: value for field, value in req.items()}}

        data = await RetrieveCandidateResults.get(id)
        if not data:
            raise HTTPException(
                status_code=404,
                detail='Record with the id not found!'
            )

        await data.update(update_query)
        return data
    except DuplicateKeyError:
        return {"error": "Document(s) with the same name already exists."}


@router.put("/{id}", response_description="Record updated")
async def update_data_by_id(id: PydanticObjectId, req: UpdateCandidateResults,
                            current_user: dict = Depends(get_current_user)) -> RetrieveCandidateResults:
    try:
        req = {k: v for k, v in req.dict().items() if v is not None}
        update_query = {"$set": {field: value for field, value in req.items()}}

        data = await RetrieveCandidateResults.get(id)
        if not data:
            raise HTTPException(
                status_code=404,
                detail='Record with the id not found!'
            )

        await data.update(update_query)
        return data

    except DuplicateKeyError:
        return {"error": "Survey document(s) with the same name already exists."}


# Delete raw data using id
@router.delete("/{id}", response_description='Record has been deleted from the TPP database!')
async def delete_data(id: PydanticObjectId,
                      current_user: dict = Depends(get_current_user)) -> dict:
    data = await RetrieveCandidateResults.get(id)

    if not data:
        raise HTTPException(
            status_code=404,
            detail='survey data not found!'
        )

    await data.delete()
    return {
        "message": "Record has been deleted successfully!"
    }
