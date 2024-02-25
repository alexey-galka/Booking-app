from app.users.auth import get_password_hash, authenticate_user, create_access_token
from fastapi import APIRouter, status, Response, HTTPException
from app.users.interface import SUserAuth
from app.users.service import UsersService


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register")
async def register_user(user_data: SUserAuth):
    existing_user = await UsersService.find_one_or_none(email=user_data.email)

    if existing_user:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    hashed_password = get_password_hash(user_data.password)
    await UsersService.add(email=user_data.email, hashed_password=hashed_password)


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(email=user_data.email, password=user_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = create_access_token({"sub": user.id})
    response.set_cookie("booking_access_token", access_token, httponly=True)
    return access_token
