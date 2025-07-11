# Imports for files in schema
#-----------------------------
from beanie import Document, PydanticObjectId, Indexed
from pydantic import BaseModel, Extra, validator, Field
from typing import Optional, Union, List
from fastapi import HTTPException
from datetime import datetime