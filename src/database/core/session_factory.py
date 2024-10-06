from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine
)

from config import database_url


engine = create_async_engine(database_url, echo=False)
session_factory = async_sessionmaker(
    bind=engine, 
    autocommit=False, 
    autoflush=False,
    expire_on_commit=False
)
