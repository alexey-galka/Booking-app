from fastapi import APIRouter, Depends
from app.bookings.service import BookingService
from app.bookings.interface import SBooking
from app.users.models import Users
from app.users.dependencies import get_current_user


# Create a router
router = APIRouter(
    prefix='/bookings',
    tags=['Bookings'],
)


# Endpoints
@router.get('')
async def get_bookings(user: Users = Depends(get_current_user)):
    return await BookingService.find_all(user_id=user.id)
