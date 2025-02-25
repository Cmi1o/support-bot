from datetime import datetime

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import app.bot.utils.keyboards as kb
import requests
from app.bot.utils import topics
from app.bot.utils.states import SupportStates
from config import bot_token, forum_topic_id
from database import service

router = Router()


@router.message(SupportStates.get_msg, F.text == '/admin_panel')
async def protect_admin_commands(message: Message) -> None:
    await message.answer('Извините, но эта команда вам недоступна')


@router.message(SupportStates.get_msg)
async def support_get_msg(message: Message, state: FSMContext) -> None:
    if not message.from_user:
        return

    await message.answer('Ваше сообщение:')
    await requests.send_copy(message, chat_id=message.from_user.id)

    await message.answer(
        'Если желаете переписать введите "Нет"', reply_markup=kb.confirm
    )

    # message data of json: aiogram.types.Message
    await state.update_data(message=message)
    await state.set_state(SupportStates.confirm)


@router.message(SupportStates.confirm, F.text == 'Да')
async def support_yes(message: Message, state: FSMContext) -> None:
    if not message.from_user:
        return

    data = await state.get_data()
    user = await service.users.get_by(telegram_id=message.from_user.id)

    if not user:
        await message.answer('Похоже, что вы не зарегистрированы в нашей системе')
        return

    await state.clear()

    if not user.thread_id:
        topic_response = await topics.create_topic(
            bot_token=bot_token,
            forum_id=forum_topic_id,
            name=f'Обращение №{user.id}',
        )
        topic_response = await topic_response.json()
        thread_id = topic_response['result']['message_thread_id']

        await service.users.update_by(id=user.id, values={'thread_id': thread_id})
        user.thread_id = thread_id

    await requests.send_copy(
        message=data['message'],
        chat_id=forum_topic_id,
        message_thread_id=user.thread_id,
    )  # send message to forum topic

    await service.users.update_by(
        id=user.id, values={'request_time': datetime.now()}
    )

    await message.answer(
        text='Ваше сообщение отправлено администратору', reply_markup=kb.remove
    )
    await state.set_state(SupportStates.get_msg)
    await message.answer(
        text='Ваш диалог продолжается, однако если вы желаете завершить его, то нажмите на кнопку',
        reply_markup=kb.end_dialog,
    )


@router.message(SupportStates.confirm, F.text == 'Нет')
async def support_no(message: Message, state: FSMContext) -> None:
    await message.answer('Перепишите ваше сообщение:', reply_markup=kb.remove)
    await state.set_state(SupportStates.get_msg)
