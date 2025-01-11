from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

import app.utils.keyboards as kb
import requests
from app.filters import Admin, InPrivateChat
from app.utils.states import AdminStates
from database import controller

router = Router()


@router.message(Admin(), Command('admin_panel'), InPrivateChat())
async def admin_panel(message: Message) -> None:
    await message.answer('Возможные команды админа:', reply_markup=kb.admin)


@router.callback_query(Admin(), F.data == 'mail')
async def get_admin_message(call: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(AdminStates.get_msg)
    await call.message.answer('Пришлите ваше сообщение для рассылки')  # type: ignore


@router.message(AdminStates.get_msg)
async def send_mail(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer('Подождите идет рассылка...')

    async for user in controller.users.get_all():
        await requests.send_copy(message, chat_id=user.telegram_id)

    await message.answer('Рассылка завершена', reply_markup=kb.remove)
