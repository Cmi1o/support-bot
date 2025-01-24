from datetime import datetime
from typing import TypedDict

__all__ = ('FilterData', 'UpdateDataDict', 'AddData', 'NegativeSettingsDict')


class BaseDataDTO(TypedDict, total=False):
    telegram_id: int
    thread_id: int | None
    request_time: datetime


class UpdateDataDict(BaseDataDTO, total=False):
    updated_at: datetime


class FilterData(UpdateDataDict, total=False):
    id: int | None
    created_at: datetime


class AddData(BaseDataDTO, total=False):
    id: int | None
    updated_at: datetime
    created_at: datetime


NegativeSettingsDict = FilterData
