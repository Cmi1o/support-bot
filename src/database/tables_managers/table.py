from typing import Any, AsyncGenerator, Generic

from sqlalchemy import sql

from database.core import session_factory
from database.types import MT
from .base import ITableManager


class Table(ITableManager, Generic[MT]):
    def __init__(self, table: MT) -> None:
        self.__table = type(table)
    
    async def get_all(self) -> AsyncGenerator[MT, None]:
        stmt = sql.select(self.__table)
        
        async with session_factory() as session:
            async for row in await session.stream(stmt):
                yield row[0]
    
    async def get_many_with(self, **filter_data) -> AsyncGenerator[MT, None]:
        stmt = sql.select(self.__table).filter_by(**filter_data)
        
        async with session_factory() as session:
            async for row in await session.stream(stmt):
                yield row[0]
    
    async def get_by(self, **filter_data) -> MT | None:
        async with session_factory() as session:
            return await session.scalar(
                sql.select(self.__table).filter_by(
                    **filter_data
                )
            )
