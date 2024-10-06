from abc import ABC, abstractmethod
from typing import Any, Unpack, AsyncGenerator

from database.types import *


class ITableManager(ABC):
    @abstractmethod
    def __init__(self, **negative_settings: Any) -> None: ...
    
    @abstractmethod
    def get_all(self) -> AsyncGenerator[Any, None]:
        '''Asynchronous generator for getting all rows from table
        
        Yields
        -------
        Table row data
        '''
    
    @abstractmethod
    def get_many_with(
        self, 
        **filter_data: Unpack[FilterData]
    ) -> AsyncGenerator[Any, None]:
        '''Asynchronous generator for getting rows from table with filter data
        
        Parameters
        ----------
        filter_data : Unpack[FilterData]
            `FilterData` is a `TypedDict`
        
        Yields
        -------
        Table row data
        '''
    
    @abstractmethod
    def get_by(self, **filter_data: Unpack[FilterData]) -> Any | None:
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
        values: UpdateDataDict,
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
