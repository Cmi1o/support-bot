import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramNetworkError

from app import middlewares
from app.dispatcher_builder import *
from app.users_cleaner import InactiveUsersCleaner
from config import bot_token, forum_topic_id


async def main() -> None:
    bot = Bot(bot_token, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    cleaner = InactiveUsersCleaner(bot_token, forum_topic_id)
    
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    
    dp.update.outer_middleware(middlewares.outer.AntiFlood(1))
    dp.update.outer_middleware(middlewares.outer.Auth())
    
    dp.include_router(router)
    
    await asyncio.gather(
        dp.start_polling(bot),
        cleaner.start_polling()
    )


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, TelegramNetworkError) as error:
        if isinstance(error, TelegramNetworkError):
            print('Network error')
