from abc import ABC, abstractmethod
from typing import AsyncGenerator, Generic, Unpack

from database.types import *


class ITableController(ABC, Generic[MT]):
    def __init__(self, table: MT) -> None:
        self._table = type(table)

    @abstractmethod
    def get_all(
        self,
        *,
        table_index: int = 0,
        negative_settings: NegativeSettingsDict | None = None,
        **filter_data: Unpack[FilterData]
    ) -> AsyncGenerator[MT, None]:
        '''Asynchronous generator for getting all rows from table

        Yields
        -------
        Table row data
        '''

    @abstractmethod
    async def get_by(
        self,
        *,
        negative_settings: NegativeSettingsDict | None = None,
        **filter_data: Unpack[FilterData]
    ) -> MT | None:
        '''Asynchronous method for getting row from table by `filter_data`

        Parameters
        ----------
        filter_data : Unpack[FilterData]
            This is a `TypedDict`

        Returns
        -------
        table row | None
        '''

    @abstractmethod
    async def update_by(
        self,
        *,
        values: UpdateDataDict,
        negative_settings: NegativeSettingsDict | None = None,
        **filter_data: Unpack[FilterData]
    ) -> None:
        '''Update table by given `filter_data`

        Parameters
        ----------
        values : UpdateDataDict
            `TypedDict` with valid data for update
        filter_data : Unpack[FilterData]
            This is a `TypedDict`
        '''

    @abstractmethod
    async def add(self, **data: Unpack[AddData]) -> None:
        '''Add new row to table with given `data`

        Parameters
        ----------
        data : AddData
            `TypedDict` with valid data for add
        '''

    @abstractmethod
    async def delete_by(
        self,
        *,
        negative_settings: NegativeSettingsDict | None = None,
        **filter_data: Unpack[FilterData]
    ) -> None:
        '''Delete row from table by given `filter_data`

        Parameters
        ----------
        filter_data : Unpack[FilterData]
            This is a `TypedDict`
        '''

    def _convert_settings(
        self, negative_settings: NegativeSettingsDict | None
    ) -> list:
        if not negative_settings:
            return []
        return [getattr(self._table, k) != v for k, v in negative_settings.items()]
