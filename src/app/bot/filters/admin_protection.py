from aiogram.filters import Filter
from aiogram.types import Message

from config import admin_id


class Admin(Filter):
    async def __call__(self, message: Message) -> bool:
        if not message.from_user:
            return False
        return message.from_user.id == admin_id
