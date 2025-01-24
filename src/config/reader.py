from typing import Final as const

from .loader import settings

__all__ = ('database_url', 'bot_token', 'admin_id', 'forum_topic_id')


database_url: const = settings.database.url.get_secret_value().unicode_string()
bot_token: const = settings.bot.token.get_secret_value()
admin_id: const = settings.bot.admin_id.get_secret_value()
forum_topic_id: const = settings.bot.forum_topic_id.get_secret_value()
