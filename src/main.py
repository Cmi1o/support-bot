import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramNetworkError

from app.bot import middlewares
from app.dispatcher_settings import *
from app.users_cleaner import InactiveUsersCleaner
from config import bot_token, forum_topic_id


async def main() -> None:
    bot = Bot(
        token=bot_token,
        session=AiohttpSession(),
        default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN),
    )
    dp = Dispatcher()
    cleaner = InactiveUsersCleaner(bot_token, forum_topic_id)

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    dp.update.outer_middleware(middlewares.outer.AntiFlood(1))
    dp.update.outer_middleware(middlewares.outer.Auth())

    dp.include_router(router)

    await dp.start_polling(bot)
    await cleaner.start_polling()


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO, format='[%(asctime)s] [%(levelname)s] %(message)s'
    )

    try:
        asyncio.run(main())
    except (KeyboardInterrupt, TelegramNetworkError) as error:
        if isinstance(error, TelegramNetworkError):
            logging.error('Network error')
