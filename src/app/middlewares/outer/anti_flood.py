from typing import Any, Dict
from typing import Callable, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from cachetools import TTLCache


number = float | int

class AntiFlood(BaseMiddleware):
    def __init__(self, time_limit: number=2) -> None:
        self.limit = TTLCache(10_000, ttl=time_limit)
    
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        if data['event_from_user'] in self.limit: 
            return
        self.limit[data['event_from_user']] = None
        
        return await handler(event, data)
