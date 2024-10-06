from aiogram import Router

from app.handlers import (
    callback, 
    command, 
    message
)


def gather_routers(*routers: Router) -> Router:
    router = Router()
    router.include_routers(*routers)
    
    return router


router = gather_routers(
    command.router,
    callback.router,
    message.router
)
