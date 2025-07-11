# This is the schema for "survey" collection.
# ==========================================

from ..lib.lib_3 import *


# Define model(schema) for survey collection:
class Survey(Document):
    survey: Indexed(str, unique=True)       # Default to 20 characters
    parent_survey: str                      # limit to 20 characters
    f_hi: float                             # MHz(250 - 40_000)
    f_low: float                            # MHz(250 - 40_000)
    zap_array: List[int]                    # Array of integers(0, 32000)
    sampling_time: float                    # Microseconds(1 - 40_000)
    number_of_frequency_channels: int       # (10-20_000)
    backend: str                             # Default to 16 characters
    backend_mode: str                        # Default to 16 characters
    telescope: str                           # Default to 16 charcters
    number_of_bits: int                      # (1 - 64)
    no_of_pols: int                          # (1 - 4)
    pol_type: str                            # Type of polarization(less than 10 characters)
    t_sys: float                             # (0 - 500) T_rec + T_sky in Kelvin

    @validator('*')
    def validate_fields(cls, v, field):
        if field.name in ['survey', 'parent_survey'] and len(v) > 20:
            raise ValueError('The length of survey characters should not exceed 20.')
        elif field.name in ['f_hi', 'f_low'] and (v < 250 or v > 40000):
            raise ValueError('Frequency should be in the range of 250 - 40000 MHz')
        elif field.name == 'sampling_time' and (v < 1 or v > 40000):
            raise ValueError('Sampling time should be in the range of 1 - 40000 microseconds')
        elif field.name in ['backend', 'backend_mode', 'telescope'] and len(v) > 16:
            raise ValueError('The length of the field should not exceed 16 characters.')
        elif field.name == 'number_of_bits' and (v < 1 or v > 64):
            raise ValueError('The number of bits should be in the range of 1 - 64.')
        elif field.name == 'no_of_pols' and (v < 1 or v > 4):
            raise ValueError('The number of pols should be in the range of 1 - 4.')
        elif field.name == 'zap_array' and not all(0 <= value <= 32_000 for value in v):
            raise ValueError('zap_array should be in the range of 0-32000')
        elif field.name == 'number_of_frequency_channels' and (v < 10 or v > 32_000):
            raise ValueError('number_of_frequency_channels should be in the range 10-20_000')
        elif field.name == 'pol_type' and (len(v)>10):
            raise ValueError('characters length for pol_type should not exceed 10')
        elif field.name == 't_sys' and (v<0 or v>500):
            raise  ValueError('System temperature should be in the range 0-500 Kelvin')
        return v

    # Set the name of the collection.
    class Settings:
        name = 'survey'

    class Config:
        extra = Extra.forbid
        anystr_strip_whitespace = True


class RetrieveSurvey(Survey):
    """
    If a new field is added in the raw_data in the future or a field is removed
    then that field's value should be mentioned here as optional as this:
    new_field: Optional[str]
    """
    survey: Optional[Indexed(str, unique=True)]  # Default to 20 characters
    parent_survey: Optional[str]  # limit to 20 characters
    f_hi: Optional[float]  # MHz(250 - 40_000)
    f_low: Optional[float ] # MHz(250 - 40_000)
    zap_array: Optional[List[int]]  # Array of integers(0, 32000)
    sampling_time: Optional[float]  # Microseconds(1 - 40_000)
    number_of_frequency_channels: Optional[int]  # (10-20_000)
    backend: Optional[str]  # Default to 16 characters
    backend_mode: Optional[str]  # Default to 16 characters
    telescope: Optional[str]  # Default to 16 charcters
    number_of_bits: Optional[int]  # (1 - 64)
    no_of_pols: Optional[int]  # (1 - 4)
    pol_type: Optional[str]  # Type of polarization(less than 10 characters)
    t_sys: Optional[float]

    @validator('*')
    def validate_fields(cls, v, field):
        """
        Bypass validation on retrieving
        """
        return  v


class UpdateSurvey(BaseModel):
    survey: Optional[Indexed(str, unique=True)]  # Default to 20 characters
    parent_survey: Optional[str]  # limit to 20 characters
    f_hi: Optional[float]  # MHz(250 - 40_000)
    f_low: Optional[float]  # MHz(250 - 40_000)
    sampling_time: Optional[float]  # Microseconds(1 - 40_000)
    backend: Optional[str]  # Default to 16 characters
    backend_mode: Optional[str]  # Default to 16 characters
    telescope: Optional[str]  # Default to 16 charcters
    number_of_bits: Optional[int]  # (1 - 64)
    no_of_pols: Optional[int]  # (1 - 4)
    t_sys: Optional[float]     # (0-500)

    @validator('*')
    def validate_fields(cls, v, field):
        if field.name in ['survey', 'parent_survey'] and len(v) > 20:
            raise ValueError('The length of survey characters should not exceed 20.')
        elif field.name in ['f_hi', 'f_low'] and (v < 250 or v > 40000):
            raise ValueError('Frequency should be in the range of 250 - 40000 MHz')
        elif field.name == 'sampling_time' and (v < 1 or v > 40000):
            raise ValueError('Sampling time should be in the range of 1 - 40000 microseconds')
        elif field.name in ['backend', 'backend_mode', 'telescope'] and len(v) > 16:
            raise ValueError('The length of the field should not exceed 16 characters.')
        elif field.name == 'number_of_bits' and (v < 1 or v > 64):
            raise ValueError('The number of bits should be in the range of 1 - 64.')
        elif field.name == 'no_of_pols' and (v < 1 or v > 4):
            raise ValueError('The number of pols should be in the range of 1 - 4.')
        elif field.name == 'zap_array' and not all(0 <= value <= 32_000 for value in v):
            raise ValueError('zap_array should be in the range of 0-32000')
        elif field.name == 'number_of_frequency_channels' and (v < 10 or v > 32_000):
            raise ValueError('number_of_frequency_channels should be in the range 10-20_000')
        elif field.name == 'pol_type' and (len(v) > 10):
            raise ValueError('characters length for pol_type should not exceed 10')
        elif field.name == 't_sys' and (v<0 or v>500):
            raise  ValueError('System temperature should be in the range 0-500 Kelvin')

        return v

    class Config:
        extra = Extra.forbid
        anystr_strip_whitespace = True
