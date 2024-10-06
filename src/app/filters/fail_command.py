from aiogram.types import Message
from aiogram.filters import Filter


class FailCommand(Filter):
    async def __call__(self, message: Message) -> bool:
        if not message.text or not message.from_user:
            return False
        return not message.from_user.is_bot and message.text.startswith('/')
