# This is a schema for "data" collection.
# ========================================

from ..lib.lib_3 import *


# Model defined for posting data
class Data(Document):
    start_date_time: float  # MJD (45000-63000)
    obs_length: float  # seconds (1, 40_000)
    ra_j: float  # decimal degrees (0, 360)
    dec_j: float  # decimal degrees (-90, 90)
    source_name: str
    beam: int = 0  # default to zero if observing system doesn't have beams.
    regex_filename: str  # check if it is a string or not
    n_files: int
    md5_file: List[str]  # Array of strings
    location_on_filesystem: str  # at least check for sensible format
    survey: str  # Linked to Survey Collection
    size: int  # In the units of MB.

    # new_field: str

    # validator for start_date_time
    @validator('start_date_time')
    def range_of_start_date_time(cls, v):
        if v < 45_000 or v > 62_000:
            raise ValueError('start_date_time should be in the range 45000-62000 MJD')
        return v

    # validator for obs length
    @validator('obs_length')
    def range_of_obs_length(cls, v):
        if v < 1 or v > 40_000:
            raise ValueError('obs_length should be in the range 1-40_000 Seconds')
        return v

    # validator for ra_j
    @validator('ra_j')
    def range_of_ra_j(cls, v):
        if v < 0 or v > 360:
            raise ValueError('ra_j should be in the range 0-360 decimal degrees')

        return v

    @validator('survey')
    def len_of_survey(cls, v):
        if len(v) > 20:
            raise ValueError('survey should have length of only 20 characters')

        return v

    # validator for dec_j
    @validator('dec_j')
    def range_dec_j(cls, v):
        if v < -90 or v > 90:
            raise ValueError('dec_j should be in the range -90 - 90 decimal degrees')

        return v

    @validator('regex_filename')
    def regex_filename_constraint(cls, v):
        if '/' in list(v):
            raise ValueError("regex_filename shouldn't contain '/' ")

        return v

    class Settings:
        name = 'data'  # set the name of the collection ----> data

    class Config:
        extra = Extra.forbid
        anystr_strip_whitespace = True


# Model defined for retrieving raw data
# This is only required if we update our schema for insertion in the future.
class RetrieveData(Data):
    """
    If a new field is added in the raw_data in the future or a field is removed
    then that field's value should be mentioned here as optional as this:
    new_field: Optional[str]
    """
    pass


# Model defined for updating data
# I am defining two different models so that inserting requires compulsory fields
# while updating requires optional fields.
class UpdateData(BaseModel):
    start_date_time: Optional[float]  # MJD (45000-62000)
    obs_length: Optional[float]  # seconds (1, 40_000)
    ra_j: Optional[float]  # decimal degrees (0, 360)
    dec_j: Optional[float]  # decimal degrees (-90, 90)
    source_name: Optional[str]
    beam: Optional[int]   # default to zero if observing system doesn't have beams.
    regex_filename: Optional[str]  # check if it is a string or not
    n_file: Optional[int]
    md5_file: Optional[List[str]]
    location_on_filesystem: Optional[str]  # at least check for sensible format
    survey: Optional[str]  # (maybe limit to 20 characters) Linked to Survey Collection
    size: Optional[int]  # In the units of MB
    # new_field: Optional

    @validator('start_date_time')
    def range_of_start_date_time(cls, v):
        if v < 45_000 or v > 62_000:
            raise ValueError('start_date_time should be in the range 45000-62000 MJD')
        return v

    @validator('obs_length')
    def range_of_obs_length(cls, v):
        if v < 1 or v > 40_000:
            raise ValueError('obs_length should be in the range 1-40_000 Seconds')
        return v

    @validator('ra_j')
    def range_of_ra_j(cls, v):
        if v < 0 or v > 360:
            raise ValueError('ra_j should be in the range 0-360 decimal degrees')
        return v

    @validator('dec_j')
    def range_dec_j(cls, v):
        if v < -90 or v > 90:
            raise ValueError('dec_j should be in the range -90 - 90 decimal degrees')
        return v

    @validator('regex_filename')
    def regex_filename_constraint(cls, v):
        if '/' in list(v):
            raise ValueError("regex_filename shouldn't contain '/' ")

        return v

    class Config:
        extra = Extra.forbid
        anystr_strip_whitespace = True

