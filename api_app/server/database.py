from beanie import init_beanie
import motor.motor_asyncio
from dotenv import load_dotenv
import os


from .schemas.data_schema import Data
from .schemas.survey_schema import Survey
from .schemas.candidate_results_schema import CandidateResults, RetrieveCandidateResults
from .schemas.users import Users
from .schemas.job_submission_schema import JobSubmissions
from .schemas.processing_outcomes_schema import ProcessingOutcomes
from .schemas.pipeline_versions_schema import PipelineVersions

async def initialize_database():
    """
        Connect to the MongoDB database using the provided connection string and
        initialize the database client.

        Returns:
            motor.motor_asyncio.AsyncIOMotorClient: The initialized MongoDB client.

    """
    load_dotenv()
    db_admin_passwd = os.environ.get("DB_ADMIN_PASSWORD")
    db_port = os.environ.get("DB_PORT")
    client = motor.motor_asyncio.AsyncIOMotorClient(
        f"mongodb://admin:{db_admin_passwd}@db:{db_port}"
    )

    await init_beanie(database=client.TPP, document_models=[Data,
                                                            Survey,
                                                            CandidateResults,
                                                            JobSubmissions,
                                                            ProcessingOutcomes,
                                                            PipelineVersions,
                                                            Users])
