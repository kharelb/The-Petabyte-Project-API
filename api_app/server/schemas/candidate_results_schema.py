# This is the schema for candidate results
# =========================================

from ..lib.lib_3 import *

class Interesting(BaseModel):
    is_interesting: Optional[bool]
    user: Optional[str] = Field(max_length=20)


class Periodicity(BaseModel):
    periodicity_done: Optional[bool]
    user: Optional[str] = Field(max_length=20)


class Differencing(BaseModel):
    differencing_done: Optional[bool]
    user: Optional[str] = Field(max_length=20)

class Inspection(BaseModel):
    was_inspected: Optional[bool]
    user: Optional[str] = Field(max_length=20)


class Note(BaseModel):
    note: Optional[str] = Field(max_length=200)  # limited to 200 characters
    when_submitted: Optional[datetime]
    user: Optional[str] = Field(max_length=20)

    # @validator('note')
    # def length_of_note(cls, v):
    #     if len(v) > 200:
    #         raise ValueError('The length of note characters should not exceed 200 characters.')
    #
    #     return v


# Define model(schema) for candidate_results collection:
class CandidateResults(Document):
    submissionID: str
    outcomeID: str
    dataID: str
    dm: Optional[float]                               # range: 0-10_000   unit: pc/cm^3
    tcand: Optional[float]                            # MJD range: 45_000-62_000                     # MJD range: 45_000-62_000
    gl: Optional[float]                               # unit: degrees, range:0-360
    gb: Optional[float]                               # unit: degrees, range: -90 - 90
    f_ctr: Optional[float]                            # unit: MHz, range:200-50000
    width: Optional[float]                            # unit: ms, range: 0-128
    sn: Optional[float]                               # unitless
    fetch_score: Optional[float]                      # range: 0-1
    ymw_dm_mw: Optional[float]                        # pc/cc
    ymw_dist: Optional[float]                         # kpc
    ymw_z: Optional[float]
    ne_dm_mw: Optional[float]
    ne_dist: Optional[float]
    result_name: Optional[str]                        # name of candidate plot or hdf5 file on disk
    proposed_type: Optional[str]                      # range: 6-characters
    confirmed_type: Optional[str]                     # range: 6-characters, human-confirmed version of proposed type.
    interesting_info: Optional[Interesting]
    periodicity_info: Optional[Periodicity]
    differencing_info: Optional[Differencing]
    inspection_info: Optional[Inspection]
    note_info: Optional[Note]

    @validator('*')
    def validate_fields(cls, v, field):
        if field.name == 'dm' and (v < 0 or v > 10_000):
            raise ValueError('Dispersion measure usually ranges from 0-10000')
        elif field.name in ['tcand'] and (v < 45_000 or v > 62_000):
            raise ValueError(f'{field.name} value should be in the range 45000-62000 MJD. ')
        elif field.name in ['width'] and (v < 0 or v > 128):
            raise ValueError(f'{field.name} value should be in the range of 0-128ms.')
        elif field.name == 'fetch_score' and (v < 0 or v > 1):
            raise ValueError(f'{field.name} value should be in the range of 0-1.')
        elif field.name in ['proposed_type', 'confirmed_type'] and len(v) > 6:
            raise ValueError(f'{field.name} should be maximum of 6 characters long.')
        elif field.name == 'gl' and (v < 0 or v > 360):
            raise ValueError(f'{field.name} should be in the range 0-360 degrees.')
        elif field.name == 'gb' and (v < -90 or v > 90):
            raise ValueError(f'{field.name} should be in the range -90 - +90 degrees.')
        elif field.name == 'f_ctr' and (v < 200 or v > 50000):
            raise ValueError(f'{field.name} should be in the range 200-50000 MHz.')

        return v

    # Set the name of the collection.
    class Settings:
        name = 'candidate_results'

    class Config:
        extra = Extra.forbid
        anystr_strip_whitespace = True


class RetrieveCandidateResults(CandidateResults):
    """
    If a new field is added in the raw_data in the future or a field is removed
    then that field's value should be mentioned here as optional as this:
    new_field: Optional[str]
    """
    submissionID: Optional[str]
    outcomeID: Optional[str]
    dataID: Optional[str]
    dm: Optional[float]  # range: 0-10_000   unit: pc/cm^3
    tcand: Optional[float]  # MJD range: 45_000-62_000
    fetch_width: Optional[float]  # unit: ms, range: 0-128
    gl: Optional[float]  # unit: degrees, range:0-360
    gb: Optional[float]  # unit: degrees, range: -90 - 90
    f_ctr: Optional[float]  # unit: MHz, range:200-50000
    detected_width: Optional[float]  # unit: ms, range: 0-128
    sn: Optional[float]  # unitless
    fetch_score: Optional[float]  # range: 0-1
    ymw_dm_mw: Optional[float]  # pc/cc
    ymw_dist: Optional[float]  # kpc
    ymw_z: Optional[float]
    ne_dm_mw: Optional[float]
    ne_dist: Optional[float]
    result_name: Optional[str]  # name of candidate plot or hdf5 file on disk
    proposed_type: Optional[str]  # range: 6-characters
    confirmed_type: Optional[str]  # range: 6-characters, human-confirmed version of proposed type.
    interesting_info: Optional[Interesting]
    periodicity_info: Optional[Periodicity]
    differencing_info: Optional[Differencing]
    inspection_info: Optional[Inspection]
    note_info: Optional[Note]

    @validator('*')
    def validate_fields(cls, v, field):
        """
        Overriding validator in the CandidateResults class to avoid any schema
        while retrieving the data from the canidate_results collection.
        Should implement this to avoid schema being implemented while retriving
         data from a collection. This is super important where there are optional
          fields as well as valiators defined explicitly with @validator decora-
          tor.
        """
        return v


class UpdateCandidateResults(BaseModel):
    submissionID: Optional[str]
    outcomeID: Optional[str]
    dataId: Optional[str]
    dm: Optional[float]
    tcand: Optional[float]
    fetch_width: Optional[float]
    gl: Optional[float]
    gb: Optional[float]
    f_ctr: Optional[float]
    detected_width: Optional[float]
    sn: Optional[float]
    fetch_score: Optional[float]
    ymw_dm_mw: Optional[float]
    ymw_dist: Optional[float]
    ymw_z: Optional[float]
    ne_dm_mw: Optional[float]
    ne_dist: Optional[float]
    data_name: Optional[str]
    output_location: Optional[str]
    proposed_type: Optional[str]
    confirmed_type: Optional[str]
    interesting_info: Optional[Interesting]
    periodicity_info: Optional[Periodicity]
    differencing_info: Optional[Differencing]
    inspection_info: Optional[Inspection]
    note_info: Optional[Note]

    @validator('*')
    def validate_fields(cls, v, field):
        if field.name == 'dm' and (v < 0 or v > 10_000):
            raise ValueError('Dispersion measure usually ranges from 0-10000')
        elif field.name in ['tcand'] and (v < 45_000 or v > 62_000):
            raise ValueError(f'{field.name} value should be in the range 45000-62000 MJD. ')
        elif field.name in ['fetch_width', 'detected_width'] and (v < 0 or v > 128):
            raise ValueError(f'{field.name} value should be in the range of 0-128ms.')
        elif field.name == 'fetch_score' and (v < 0 or v > 1):
            raise ValueError(f'{field.name} value should be in the range of 0-1.')
        elif field.name in ['proposed_type', 'confirmed_type'] and len(v) > 6:
            raise ValueError(f'{field.name} should be maximum of 6 characters long.')
        elif field.name == 'gl' and (v < 0 or v > 360):
            raise ValueError(f'{field.name} should be in the range 0-360 degrees.')
        elif field.name == 'gb' and (v < -90 or v > 90):
            raise ValueError(f'{field.name} should be in the range -90 - +90 degrees.')
        elif field.name == 'f_ctr' and (v < 200 or v > 50000):
            raise ValueError(f'{field.name} should be in the range 200-50000 MHz.')

        return v

    class Config:
        extra = Extra.forbid
        anystr_strip_whitespace = True
