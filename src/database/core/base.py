from sqlalchemy import BigInteger
from sqlalchemy.orm import (
    mapped_column,
    DeclarativeBase,
    Mapped, declared_attr
)
from sqlalchemy.ext.asyncio import AsyncAttrs


class Base(AsyncAttrs, DeclarativeBase):
    id: Mapped[int] = mapped_column(BigInteger(), primary_key=True)
    
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f'{cls.__name__.lower()}s'
