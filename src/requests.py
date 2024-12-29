import aiohttp
from aiogram.types import Message


async def send_copy(message: Message, **data) -> None:
    try:
        await message.send_copy(**data)
    except TypeError:
        ...


async def send_message(bot_token: str, **data) -> None:
    async with aiohttp.ClientSession() as session:
        await session.post(
            url=f'https://api.telegram.org/bot{bot_token}/sendMessage', json=data
        )
