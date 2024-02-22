from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, AsyncEngine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.config import settings


# Connect to DB
engine: AsyncEngine = create_async_engine(settings.DATABASE_URL)


# Create session generator
async_session_maker: sessionmaker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# Used for migrations
class Base(DeclarativeBase):
    pass
