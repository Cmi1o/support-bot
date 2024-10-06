from datetime import datetime
from typing import Annotated

from sqlalchemy import BigInteger, DateTime
from sqlalchemy.orm import mapped_column


__all__ = (
    'big_int', 
    'nullable_int', 
    'time'
)


big_int = Annotated[int, mapped_column(BigInteger())]
nullable_int = Annotated[int, mapped_column(nullable=True)]
time = Annotated[datetime, mapped_column(DateTime())]
