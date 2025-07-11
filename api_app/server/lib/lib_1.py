# Imports for files in routes.
# ===========================
from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, Query, Body
from typing import List, Dict, Union
from datetime import datetime
from pymongo.errors import DuplicateKeyError
from fastapi import Depends

# These are internal imports
from ..auth import authenticated_route
from ..auth import get_current_user