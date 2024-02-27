from datetime import datetime
from fastapi import Request, Depends
from jose import JWTError, jwt
from app.config import settings
from app.users.service import UsersService
from app.exceptions import ExpiredTokenException, NoTokenException, IncorrectTokenFormatException, UserNotFoundException


def get_token(request: Request) -> str:
    token: str = request.cookies.get('booking_access_token')
    if not token:
        raise NoTokenException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token=token, key=settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    except JWTError:
        raise IncorrectTokenFormatException

    expire: str = payload.get('exp')
    if (not expire) or (int(expire) < datetime.now().timestamp()):
        raise ExpiredTokenException

    user_id = payload.get('sub')
    if not user_id:
        raise UserNotFoundException

    user = await UsersService.find_by_id(int(user_id))
    if not user:
        raise UserNotFoundException
    return user
