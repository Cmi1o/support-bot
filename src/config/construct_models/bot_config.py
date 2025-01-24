from pydantic import BaseModel, Secret, SecretStr


class BotConfig(BaseModel):
    token: SecretStr
    admin_id: Secret[int]
    forum_topic_id: SecretStr
