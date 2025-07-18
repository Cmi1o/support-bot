from datetime import datetime
from typing import AsyncGenerator, Unpack

from sqlalchemy import sql

from database.core import session_factory
from database.types import AddData, FilterData, NegativeSettingsDict, UpdateDataDict

from .base import MT, ITableController


class Table(ITableController[MT]):
    async def get_all(
        self,
        *,
        table_index: int = 0,
        negative_settings: NegativeSettingsDict | None = None,
        **filter_data: Unpack[FilterData]
    ) -> AsyncGenerator[MT, None]:
        async with session_factory() as session:
            stmt = (
                sql.select(self._table)
                .filter_by(**filter_data)
                .filter(*self._convert_settings(negative_settings))
            )
            async for row in await session.stream(stmt):
                yield row[table_index]

    async def get_by(
        self,
        *,
        negative_settings: NegativeSettingsDict | None = None,
        **filter_data: Unpack[FilterData]
    ) -> MT | None:
        async with session_factory() as session:
            return await session.scalar(
                sql.select(self._table)
                .filter_by(**filter_data)
                .filter(*self._convert_settings(negative_settings))
            )

    async def update_by(
        self,
        *,
        values: UpdateDataDict,
        negative_settings: NegativeSettingsDict | None = None,
        **filter_data: Unpack[FilterData]
    ) -> None:
        values['updated_at'] = datetime.now()

        async with session_factory() as session:
            stmt = (
                sql.update(self._table)
                .filter_by(**filter_data)
                .filter(*self._convert_settings(negative_settings))
            )
            await session.execute(stmt.values(**values))
            await session.commit()

    async def delete_by(
        self,
        *,
        negative_settings: NegativeSettingsDict | None = None,
        **filter_data: Unpack[FilterData]
    ) -> None:
        async with session_factory() as session:
            await session.execute(
                sql.delete(self._table)
                .filter_by(**filter_data)
                .filter(*self._convert_settings(negative_settings))
            )
            await session.commit()

    async def add(self, **data: Unpack[AddData]) -> None:
        data['created_at'] = data['updated_at'] = datetime.now()

        async with session_factory() as session:
            session.add(self._table(**data))
            await session.commit()
