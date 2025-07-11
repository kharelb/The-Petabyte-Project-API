# This is a schema for "pipeline_versions" collection.
# ====================================================

from ..lib.lib_3 import *


class PipelineVersions(Document):
    launcher_version: str
    pipeline_version: str
    heimdall_version: str
    your_version: str
    candcsvmaker_version: str
    decimate_version: str
    ddplan_version: str

    class Settings:
        name = 'pipeline_versions'

    class Config:
        extra = Extra.forbid
        anystr_strip_whitespace = True



class RetrievePipelineVersions(PipelineVersions):
    pass


class UpdatePipelineVersions(BaseModel):
    launcher_version: Optional[str]
    pipeline_version: Optional[str]
    heimdall_version: Optional[str]
    your_version: Optional[str]
    candcsvmaker_version: Optional[str]
    decimate_version: Optional[str]
    ddplan_version: Optional[str]

    class Config:
        extra = Extra.forbid
        anystr_strip_whitespace = True