# This is an authentication mechanism for using the API.
# =====================================================

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
import datetime
from dotenv import load_dotenv
import os

load_dotenv()
secret_key = os.environ.get("SECRET_JWT_KEY")
algorithm = os.environ.get("JWT_ALGORITHM")

SECRET_KEY = secret_key  # Secret key to generate Json Web Tokens(JWT)
ALGORITHM = algorithm  # Algorithm used for signing JWT
TOKEN_EXPIRATION_TIME = 30  # The default expiration time of JWT--> 30 days.

# OAuth2PasswordBearer is the authentication scheme for password-based authetiation.
# Client should send request to /get_token endpoint of the API to obtain an access token.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="get_token")


def create_access_token(data: dict, time=TOKEN_EXPIRATION_TIME):
    """
        Create an access token using the provided data and expiration time.

        Args:
            data (dict): The username and password of a user.
            time (int): The expiration time for the access token, in days.
                        Default is TOKEN_EXPIRATION_TIME.

        Returns:
            str: The encoded access token.

    """
    expiration = datetime.datetime.utcnow() + datetime.timedelta(days=time)
    to_encode = data.copy()
    to_encode.update({"exp": expiration})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str):
    """
        Decode and verify the provided access token.

        Args:
            token (str): The access token to decode and verify.

        Returns:
            dict: The payload of the decoded access token.

        Raises:
            HTTPException: If the token is invalid or cannot be decoded.

    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")


def get_current_user(token: str = Depends(oauth2_scheme)):
    """
        Retrieve the current user's payload using the provided access token.

        Args:
            token (str): The access token obtained from the client.

        Returns:
            dict: The payload of the decoded access token representing the current user.

        Raises:
            HTTPException: If the token is invalid or cannot be decoded(From decode_access_token funtion.)

    """
    payload = decode_access_token(token)
    return payload


# Decorator to apply authentication to all routes
def authenticated_route(route_func):
    """
        Decorator to apply authentication to all routes.

        This decorator can be applied to FastAPI route functions to enforce authentication on all routes where it is used.
        It ensures that the `get_current_user` dependency is executed before the decorated route function.

        Args:
            route_func (callable): The route function to decorate.

        Returns:
            callable: The decorated route function.

    """
    async def wrapper(current_user: dict = Depends(get_current_user), **kwargs):
        return await route_func(current_user=current_user, **kwargs)

    return wrapper