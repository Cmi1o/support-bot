from aiogram import Router

from app.bot.admin import handlers as admin_message
from app.bot.handlers import callback, command, message


def gather_routers(*routers: Router) -> Router:
    router = Router()
    router.include_routers(*routers)

    return router


router = gather_routers(
    admin_message.router, callback.router, command.router, message.router
)
