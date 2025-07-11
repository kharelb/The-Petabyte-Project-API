from ..schemas.users import Users

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from ..auth import create_access_token
from passlib.context import CryptContext
import datetime
import json

router = APIRouter()
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/")
async def login(time: int | None = None, form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password
    user = await Users.find_one({"username": username})
    if user:
        user_dict = json.loads(user.json())
        password_check = password_context.verify(password, user_dict['password'])
        if password_check:
            if time:
                access_token = create_access_token({"sub": user_dict['username']}, time=time)
                return {"access_token": access_token, "token_type": "bearer",
                        "valid_till": datetime.datetime.now()+datetime.timedelta(days=time)}
            else:
                access_token = create_access_token({"sub": user_dict['username']})
                return {"access_token": access_token, "token_type": "bearer",
                        "valid_till": datetime.datetime.now()+datetime.timedelta(days=30)}

        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Invalid credentials")
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid credentials")

