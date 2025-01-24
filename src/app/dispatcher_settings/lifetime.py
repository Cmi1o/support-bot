import logging

from aiogram import Bot

from database.core import Base, engine

from .logging_bot import LoggingBot

__all__ = ('on_startup', 'on_shutdown')

logger = logging.getLogger(__name__)


async def on_startup(bot: Bot) -> None:
    bot_in_log = await LoggingBot(bot).in_log()

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    await bot.delete_webhook()
    logger.info(f'Started polling for {bot_in_log}')


async def on_shutdown(bot: Bot) -> None:
    bot_in_log = await LoggingBot(bot).in_log()

    await bot.session.close()
    logger.info(f'Finished polling for {bot_in_log}')
