from aiogram import Bot
from aiogram.types import BotName

from app.gather_routers import gather_routers
from app.handlers import (
    callback, 
    command, 
    message
)


__all__ = (
    'on_startup',
    'on_shutdown'
)


class LogBot:
    def __init__(self, bot: Bot) -> None:
        self.bot = bot
    
    async def get_name(self) -> BotName:
        return await self.bot.get_my_name()
    
    async def in_log(self) -> str:
        return f'bot({await self.get_name()}, id={self.bot.id})'


async def on_startup(bot: Bot) -> None:
    await bot.delete_webhook()
    print(f'Started polling for {await LogBot(bot).in_log()}')


async def on_shutdown(bot: Bot) -> None:
    print(f'Finished polling for {await LogBot(bot).in_log()}')


router = gather_routers(
    command.router,
    callback.router,
    message.router
)
