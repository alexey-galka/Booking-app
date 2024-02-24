from sqlalchemy import Column, Integer, Date, ForeignKey, Computed
from app.database import Base


# Object-relation mapping (ORM)
class Bookings(Base):
    __tablename__: str = 'bookings'

    id = Column(Integer, primary_key=True)
    room_id = Column(Integer, ForeignKey('rooms.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)
    total_days = Column(Integer, Computed(date_to - date_from), nullable=False)
    total_cost = Column(Integer, Computed((date_to - date_from) * price), nullable=False)
