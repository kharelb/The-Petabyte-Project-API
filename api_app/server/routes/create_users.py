from ..lib.lib_1 import *

from ..schemas.users import Users, NewUsers
from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter()


def password_hasher(password):
    return password_context.hash(password)


@router.post("/")
async def sign_up(user: NewUsers):
    try:
        new_user = Users(username=user.username,
                         password=password_hasher(user.password))

        insert_new_user = await new_user.insert()

        return {"message": f"A new user with the username: \"{insert_new_user.username}\" "
                           f" has been created."}

    except DuplicateKeyError:
        return {"error": "A user with that username already exists."}
