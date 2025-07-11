# The main application for controlling routes and starting API.


from .lib.lib_2 import *
from fastapi import FastAPI

app = FastAPI()

app.include_router(data_router, tags=["Data"], prefix="/data")

app.include_router(candidate_results_router,
                   tags=["Candidate Results"],
                   prefix="/candidate_results")

app.include_router(survey_router, tags=["Survey"], prefix="/survey")
app.include_router(create_user_router, tags=["Create Users"], prefix="/sign_up")
app.include_router(token_router, tags=["Create Token"], prefix="/token")
app.include_router(job_submissions_router, tags=["Job Submissions"], prefix="/job_submissions")
app.include_router(processing_outcomes_route, tags=["Processing Outcomes"],
                   prefix="/processing_outcomes")
app.include_router(pipeline_versions_route, tags=["Pipeline Versions"],
                   prefix="/pipeline_versions")



@app.on_event("startup")
async def start_database():
    await initialize_database()


@app.get("/", tags=["Root"])
async def root() -> dict:
    return {"message": "Welcome to the TPP Database API."}
