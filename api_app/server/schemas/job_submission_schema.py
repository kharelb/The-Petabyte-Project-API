# This is a schema for "job_submissions" collection.
# =================================================

from ..lib.lib_3 import *


class Status(BaseModel):
    completed: Optional[bool]
    date_of_completion: Optional[datetime]
    error: Optional[str]


class JobSubmissions(Document):
    pipelineID: str
    dataID: str
    started_globus: Optional[datetime]                   # "YYYY-mm-ddThh:mm:ss"
    started_transfer_data: Optional[datetime]            # "YYYY-mm-ddThh:mm:ss"
    started_slurm: Optional[datetime]                    # "YYYY-mm-ddThh:mm:ss"
    status: Optional[Status]
    username: Optional[str]                              # Who is submitting the pipeline
    duration: Optional[float]                            # end-to-end job time including transfer
    target_directory: Optional[str]                      # directory where results were written
    log_name: Optional[str]
    log_dir: Optional[str]


    class Settings:
        name = 'job_submissions'

    class Config:
        extra = Extra.forbid
        anystr_strip_whitespace = True


# This is only required to be populated if we update schema in the future otherwise pass only.
class RetrieveJobSubmissions(JobSubmissions):
    pass



class UpdateJobSubmissions(BaseModel):
    pipelineID: Optional[str]
    dataID: Optional[str]
    started_globus: Optional[datetime]                   # "YYYY-mm-ddThh:mm:ss"
    started_transfer_data: Optional[datetime]            # "YYYY-mm-ddThh:mm:ss"
    started_slurm: Optional[datetime]                    # "YYYY-mm-ddThh:mm:ss"
    status: Optional[Status]
    username: Optional[str]                              # Who is submitting the pipeline
    duration: Optional[float]                            # end-to-end job time including transfer
    target_directory: Optional[str]                      # directory where results were written
    log_name: Optional[str]
    log_dir: Optional[str]


    class Config:
        extra = Extra.forbid
        anystr_strip_whitespace = True