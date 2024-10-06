from typing import Final as const

from .loader import settings


__all__ = (
    'database_url', 
    'bot_token', 
    'admin_id', 
    'forum_topic_id'
)


database_url: const = str(settings.database_url)
bot_token: const = settings.bot_token.get_secret_value()
admin_id: const = settings.admin_id
forum_topic_id: const = settings.forum_topic_id.get_secret_value()
