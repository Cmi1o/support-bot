from datetime import datetime
from typing import Any, Dict
from typing import Callable, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from database import controller


class AddToDatabase(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        telegram_id = data['event_from_user'].id
        user = await controller.users.get_by(telegram_id=telegram_id)
        
        if not user:
            await controller.users.add(
                telegram_id=telegram_id,
                request_time=datetime.now()
            )
        
        return await handler(event, data)