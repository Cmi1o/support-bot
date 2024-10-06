from datetime import datetime
from typing import TypedDict


__all__ = (
    'FilterData',
    'UpdateDataDict',
)


class UpdateDataDict(TypedDict, total=False):
    telegram_id: int
    thread_id: int | None
    added_time: datetime


class FilterData(UpdateDataDict, total=False):
    id: int
