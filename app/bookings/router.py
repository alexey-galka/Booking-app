from fastapi import APIRouter
from app.bookings.service import BookingService
from app.bookings.interface import SBooking


# Create a router
router = APIRouter(
    prefix='/bookings',
    tags=['Bookings'],
)


# Endpoints
@router.get('')
async def get_bookings() -> list[SBooking]:
    return await BookingService.find_all()
