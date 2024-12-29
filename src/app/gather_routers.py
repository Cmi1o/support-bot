from aiogram import Router


def gather_routers(*routers: Router) -> Router:
    router = Router()
    router.include_routers(*routers)

    return router
