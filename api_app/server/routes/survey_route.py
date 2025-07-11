from ..lib.lib_1 import *

from ..schemas.survey_schema import *


router = APIRouter()


@router.post("/", response_description="Survey documents added to the database.")
async def add_data(survey: Survey | List[Survey],
                   current_user: dict = Depends(get_current_user)) -> dict:
    try:
        inserted_ids = []
        if isinstance(survey, Survey):
            insert_survey = await survey.insert()
            inserted_ids.append(insert_survey.id)
        elif isinstance(survey, list):
            for document in survey:
                insert_data = await survey.insert()
                inserted_ids.append(insert_data.id)
        return {"message": "Survey document(s) added successfully", "inserted_id": inserted_ids}

    except DuplicateKeyError:
        return {"error": "Survey document(s) with the same name already exists."}


# Get all the raw_data documents
@router.get("/", response_description="Survey records retrieved")
async def get_data(skip: int = 0, limit: int = 10,
                   current_user: dict = Depends(get_current_user)) -> List[RetrieveSurvey]:
    docs = await RetrieveSurvey.find_all().to_list()
    return docs[skip: skip + limit]


# Count the number of documents in the collection
@router.get("/count", response_description="Survey documents counted")
async def get_data(current_user: dict = Depends(get_current_user)) -> dict:
    docs = await RetrieveSurvey.find_all().count()
    return {'total number of documents in survey': docs}


# Search data by passing a dictionary.
@router.get("/search_data",
            response_description="Survey records by criteria")
async def get_survey_by_criteria(docs: dict = None,
                                 current_user: dict = Depends(get_current_user)) -> List[RetrieveSurvey]:
    survey = await RetrieveSurvey.find(docs).to_list()
    return survey


# Get the raw_data documents from id
@router.get("/{id}", response_description="Survey record retrieved from id")
async def get_survey_by_id(id: PydanticObjectId,
                           current_user: dict = Depends(get_current_user)) -> RetrieveSurvey:
    data = await RetrieveSurvey.get(id)
    if not data:
        raise HTTPException(
            status_code=404,
            detail=f"No document found with the given id:{id}"
        )
    else:
        return data


# Update the data documents(patching)
@router.patch("/{id}", response_description="Data record updated")
async def update_data_by_id(id: PydanticObjectId, req: UpdateSurvey,
                            current_user: dict = Depends(get_current_user)) -> RetrieveSurvey:
    try:
        req = {k: v for k, v in req.dict().items() if v is not None}
        update_query = {"$set": {field: value for field, value in req.items()}}

        data = await RetrieveSurvey.get(id)
        if not data:
            raise HTTPException(
                status_code=404,
                detail='raw_data record not found!'
            )

        await data.update(update_query)
        return data
    except DuplicateKeyError:
        return {"error": "Survey document(s) with the same name already exists."}


@router.put("/{id}", response_description="Data record updated")
async def update_data_by_id(id: PydanticObjectId, req: UpdateSurvey,
                            current_user: dict = Depends(get_current_user)) -> RetrieveSurvey:
    try:
        req = {k: v for k, v in req.dict().items() if v is not None}
        update_query = {"$set": {field: value for field, value in req.items()}}

        data = await RetrieveSurvey.get(id)
        if not data:
            raise HTTPException(
                status_code=404,
                detail='data record not found!'
            )

        await data.update(update_query)
        return data

    except DuplicateKeyError:
        return {"error": "Survey document(s) with the same name already exists."}


# Delete raw data using id
@router.delete("/{id}", response_description='survey record has been deleted from the TPP database!')
async def delete_data(id: PydanticObjectId,
                      current_user: dict = Depends(get_current_user)) -> dict:
    data = await RetrieveSurvey.get(id)

    if not data:
        raise HTTPException(
            status_code=404,
            detail='survey data not found!'
        )

    await data.delete()
    return {
        "message": "survey record has been deleted successfully!"
    }
