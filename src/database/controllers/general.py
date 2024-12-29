from database.models import User
from database.tables_managers import Table


class GeneralController:
    @property
    def users(self) -> Table[User]:
        return Table[User](User())


general_controller = GeneralController()
