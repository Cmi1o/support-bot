import datetime

import app.utils.keyboards as kb

from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from app.filters import Auth
from app.utils.states import SupportStates
from database import controller


router = Router()

@router.callback_query(~Auth(), F.data != 'reg')
async def retry_registration(call: CallbackQuery) -> None:
    if call.message:
        await call.message.answer(
            text=(
                'К сожалению вы не зарегистрированы. Пожалуйста, пройдите регистрацию.'
                ' Для этого нажмите на кнопку:'
            ),
            reply_markup=kb.registration
        )


@router.callback_query(F.data == 'reg')
async def registration(call: CallbackQuery) -> None:
    if call.message:
        await call.message.answer('Подождите идет регистрация...', reply_markup=kb.remove)
        await controller.users.add(
            telegram_id=call.from_user.id, 
            added_time=datetime.datetime.now()
        )
        await call.message.answer('Регистрация прошла успешно', reply_markup=kb.support)


@router.callback_query(F.data == 'support')
async def support(call: CallbackQuery, state: FSMContext) -> None:
    await call.message.answer('Введите ваше сообщение:')  # type: ignore
    await state.set_state(SupportStates.get_msg)


@router.callback_query(F.data == 'end')
async def end_dialog(call: CallbackQuery, state: FSMContext) -> None:
    await state.clear()
    
    if call.message:
        await call.message.delete()
        await call.message.answer(
            text=(
                'Спасибо за обращение! Вы всегда можете снова обратиться '
                'к поддержке, нажав на кнопку:'
            ), 
            reply_markup=kb.support
        )
