from aiogram.filters import Filter
from aiogram.types import Message


class InTopic(Filter):
    async def __call__(self, message: Message) -> bool:
        return (
            message.chat.type != 'private' and message.message_thread_id is not None
        )
