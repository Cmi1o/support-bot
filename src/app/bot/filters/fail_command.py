from aiogram.filters import Filter
from aiogram.types import Message


class FailCommand(Filter):
    async def __call__(self, message: Message) -> bool:
        if not message.text or not message.from_user:
            return False
        return not message.from_user.is_bot and message.text.startswith('/')
