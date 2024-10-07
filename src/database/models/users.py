from sqlalchemy.orm import Mapped

from database.core import Base
from database.core.annotations import *


class User(Base):
    telegram_id: Mapped[big_int]
    thread_id: Mapped[nullable_int]
    request_time: Mapped[time]
