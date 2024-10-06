from abc import ABC, abstractmethod
from typing import Generic, Unpack, AsyncGenerator

from database.types import *


class ITableManager(ABC, Generic[MT]):
    @abstractmethod
    def get_all(self) -> AsyncGenerator[MT, None]:
        '''Asynchronous generator for getting all rows from table
        
        Yields
        -------
        Table row data
        '''
    
    @abstractmethod
    def get_many_with(
        self, 
        **filter_data: Unpack[FilterData]
    ) -> AsyncGenerator[MT, None]:
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
    def get_by(self, **filter_data: Unpack[FilterData]) -> MT | None:
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
    def update_by(
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
    
    @abstractmethod
    def add(self, **data: Unpack[AddData]) -> None:
        '''Add new row to table with given `data`
        
        Parameters
        ----------
        data : AddData
            `TypedDict` with valid data for add
        '''
