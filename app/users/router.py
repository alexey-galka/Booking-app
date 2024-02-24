from http.client import HTTPException
from app.users.auth import get_password_hash
from fastapi import APIRouter
from app.users.interface import SUserRegister
from app.users.service import UsersService


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register")
async def register_user(user_data: SUserRegister):
    existing_user = await UsersService.find_one_or_none(email=user_data.email)

    if existing_user:
        raise HTTPException()
    hashed_password = get_password_hash(user_data.password)
    await UsersService.add(email=user_data.email, hashed_password=hashed_password)
