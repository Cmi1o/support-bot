from typing import TypeVar

from database.core.base import Base


__all__ = (
    'MT',
)


MT = TypeVar('MT', bound=Base)
