from aiogram.filters import Filter
from aiogram.types import CallbackQuery

from database import controller


class Auth(Filter):
    async def __call__(self, call: CallbackQuery) -> bool:
        return bool(await controller.users.get_by(telegram_id=call.from_user.id))
