from datetime import datetime
from typing import TypedDict


__all__ = (
    'FilterData',
    'UpdateDataDict',
    'AddData'
)


class UpdateDataDict(TypedDict, total=False):
    telegram_id: int
    thread_id: int | None
    added_time: datetime


class FilterData(UpdateDataDict, total=False):
    id: int


class AddData(UpdateDataDict, total=False):
    id: int
