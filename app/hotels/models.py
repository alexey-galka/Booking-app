# Create a database model
from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from app.database import Base


class Hotels(Base):
    __tablename__ = 'hotels'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    services = Column(JSON)
    rooms_quantity = Column(Integer, nullable=False)
    image_id = Column(Integer)


class Rooms(Base):
    __tablename__: str = 'rooms'

    id: Column[int] = Column(Integer, primary_key=True, nullable=False)
    hotel_id: Column[int] = Column(ForeignKey('hotels.id'), nullable=False)
    name: Column[str] = Column(String, nullable=False)
    description: Column[str] = Column(String, nullable=False)
    price: Column[int] = Column(Integer, nullable=False)
    services: Column[list] = Column(JSON, nullable=True)
    quantity: Column[int] = Column(Integer, nullable=False)
    image_id: Column[int] = Column(Integer)


# nullable - column can't be empty
# primary_key - starting count of columns from 1

# Creating migration
# alembic init migrations - create migration files for DB. Folder will be created
# to migrations/env.py import Base (from app.database import Base)
# in migrations/env.py change target_metadata to Base.metadata
# to migrations/env.py import from app.hotels.models import Hotels
# after that env.py will know about the model of hotels
# in env.py need to set link to database after config = context.config. and
# Add config.set_main_option('sqlalchemy.url', f'{DATABASE_URL}?async_fallback=True')
# import from app.database import DATABASE_URL to env.py

# install pip install greenlet
# then start with migration by alembic revision --autogenerate -m 'Initial migration' in terminal
# make upgrade by running alembic upgrade head (revision)