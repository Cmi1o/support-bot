from database.controllers import Table
from database.models import User


class GeneralService:
    @property
    def users(self) -> Table[User]:
        return Table[User](User())


general_service = GeneralService()
