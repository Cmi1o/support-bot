from aiogram import Bot
from aiogram.types import BotName


class LogBot:
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    async def get_name(self) -> BotName:
        return await self.bot.get_my_name()

    async def in_log(self) -> str:
        return f'bot({await self.get_name()}, id={self.bot.id})'
