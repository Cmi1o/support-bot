import re
from datetime import datetime

from sqlalchemy import BigInteger, DateTime
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column


class Base(AsyncAttrs, DeclarativeBase):
    id: Mapped[int] = mapped_column(BigInteger(), primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(), default=datetime.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(), default=datetime.now())

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return re.sub(r'(?<!^)(?=[A-Z])', '_', cls.__name__).lower() + 's'
