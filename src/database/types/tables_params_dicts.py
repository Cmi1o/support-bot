from datetime import datetime
from typing import TypedDict


class FilterData(TypedDict, total=False):
    id: int
    telegram_id: int
    thread_id: int | None
    added_time: datetime


class UpdateDataDict(TypedDict, total=False):
    telegram_id: int
    thread_id: int
    added_time: datetime
