from app.shared.base import CommonService
from app.bookings.models import Bookings


# Database requests
class BookingService(CommonService):
    model = Bookings
