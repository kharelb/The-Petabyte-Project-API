# This is a schema for "processing_outcomes" collection.
# =====================================================

from ..lib.lib_3 import *

class ProcessingOutcomes(Document):
    submissionID: str
    dataID: str
    node_name: Optional[str]                    # Node or system pipeline running
    rfi_fraction: Optional[float]
    rms_prezap: Optional[float]
    rms_postzap: Optional[float]
    job_start: Optional[datetime]
    job_end: Optional[datetime]
    job_state_time: Optional[datetime]
    job_state: Optional[str]
    fetch_histogram: Optional[List[float]]
    n_members: Optional[int]
    n_detections: Optional[int]
    n_candidates: Optional[int]
    working_directory: Optional[str]
    output_directory: Optional[str]

    @validator('*')
    def validate_fields(cls, v, field):
        if field.name in ['n_members', 'n_detections', 'n_candidates'] and v < 0:
            raise ValueError(f'{field.name} value should be greater than or equal to 0.')

        return v

    class Settings:
        name = 'processing_outcomes'

    class Config:
        extra = Extra.forbid
        anystr_strip_whitespace = True


class RetrieveProcessingOutcomes(ProcessingOutcomes):
    submissionID: Optional[str]
    dataID: Optional[str]
    node_name: Optional[str]  # Node or system pipeline running
    rfi_fraction: Optional[float]
    rms_prezap: Optional[float]
    rms_postzap: Optional[float]
    job_start: Optional[datetime]
    job_end: Optional[datetime]
    job_state_time: Optional[datetime]
    job_state: Optional[str]
    fetch_histogram: Optional[List[float]]
    n_members: Optional[int]
    n_detections: Optional[int]
    n_candidates: Optional[int]
    working_directory: Optional[str]
    output_directory: Optional[str]

    @validator('*')
    def validate_fields(cls, v, field):
        return v


class UpdateProcessingOutcomes(BaseModel):
    submissionID: Optional[str]
    dataID: Optional[str]
    node_name: Optional[str]
    rfi_fraction: Optional[float]
    rms_prezap: Optional[float]
    rms_postzap: Optional[float]
    job_start: Optional[datetime]
    job_end: Optional[datetime]
    job_state_time: Optional[datetime]
    job_state: Optional[str]
    fetch_histogram: Optional[List[float]]
    n_members: Optional[int]
    n_detections: Optional[int]
    n_candidates: Optional[int]
    working_directory: Optional[str]
    output_directory: Optional[str]

    class Config:
        extra = Extra.forbid
        anystr_strip_whitespace = True
