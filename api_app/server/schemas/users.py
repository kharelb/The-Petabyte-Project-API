# This is the schema for users using the api for database.
# =======================================================

from ..lib.lib_3 import *


class Users(Document):
    """
        MongoDB document model representing users.

        Fields:
        - 'username': Indexed string field representing the username. It has a unique index.
        - 'password': String field representing the user's password.

        Class Attributes:
        - 'Settings': Inner class used to specify additional settings for the document model.
        - 'Config': Inner class used to configure the behavior of the document model.

        Note:
        - The document model is named 'users' in the MongoDB collection.

    """
    username: Indexed(str, unique=True)
    password: str

    class Settings:
        name = 'users'

    class Config:
        extra = Extra.forbid
        anystr_strip_whitespace = True


class NewUsers(BaseModel):
    username: Indexed(str, unique=True)
    password: str


    class Config:
        extra = Extra.forbid
        anystr_strip_whitespace = True


