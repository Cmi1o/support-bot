from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

import app.utils.keyboards as kb
from app.utils.states import SupportStates

router = Router()


@router.callback_query(F.data == 'support')
async def support(call: CallbackQuery, state: FSMContext) -> None:
    await call.message.answer('Введите ваше сообщение:')  # type: ignore
    await state.set_state(SupportStates.get_msg)


@router.callback_query(F.data == 'end')
async def end_dialog(call: CallbackQuery, state: FSMContext) -> None:
    await state.clear()

    if call.message:
        await call.message.delete()  # type: ignore
        await call.message.answer(
            text=(
                'Спасибо за обращение! Вы всегда можете снова обратиться '
                'к поддержке, нажав на кнопку:'
            ),
            reply_markup=kb.support,
        )
