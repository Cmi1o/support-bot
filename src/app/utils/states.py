from aiogram.fsm.state import State, StatesGroup


class SupportStates(StatesGroup):
    get_msg = State()
    confirm = State()


class AdminStates(StatesGroup):
    get_msg = State()
