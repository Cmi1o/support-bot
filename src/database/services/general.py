from database.models import User
from database.controllers import Table


class GeneralService:
    @property
    def users(self) -> Table[User]:
        return Table[User](User())


general_service = GeneralService()
