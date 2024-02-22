from sqlalchemy import Column, Integer, String
from app.database import Base

class Users(Base):
    __tablename__: str = 'users'

    id: Column[int] = Column(Integer, primary_key=True, nullable=False)
    email: Column[str] = Column(String, nullable=False)
    hashed_password: Column[str] = Column(String, nullable=False)
