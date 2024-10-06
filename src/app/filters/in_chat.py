from aiogram.types import Message
from aiogram.filters import Filter


class InChat(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.chat.type == 'private'
