import asyncio
from datetime import datetime
from typing import NoReturn

import constants
from app.utils import topics
from database import service


class InactiveUsersCleaner:
    def __init__(self, bot_token: str, forum_topic_id: int | str) -> None:
        self.__token = bot_token
        self.__forum_id = forum_topic_id

    async def delete_old_requests(self) -> None:
        async for user in service.users.get_all():
            if (datetime.now() - user.request_time).days >= 14:
                await topics.delete_topic(
                    self.__token, self.__forum_id, user.thread_id
                )
                await service.users.delete_by(telegram_id=user.telegram_id)

    async def start_polling(self) -> NoReturn:
        while True:
            await asyncio.gather(self.delete_old_requests())
            await asyncio.sleep(constants.MAX_INACTIVE_TIME)
