import datetime

import app.utils.keyboards as kb

from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.filters import InChat, InTopic
from database import controller
from .support import router as support_router


router = Router()
router.include_router(support_router)


@router.message(Command('help', ignore_case=True))
async def help(message: Message) -> None:
    await message.answer(
        text='Для того чтоб написать сообщение для поддержки нажмите на кнопку',
        reply_markup=kb.support
    )


@router.message(CommandStart(ignore_case=True), InChat())
async def private_chat_start(message: Message, state: FSMContext) -> None:
    if not message.from_user: return
    
    await state.clear()
    
    if not await controller.users.get_by(telegram_id=message.from_user.id):
        await controller.users.add(
            telegram_id=message.from_user.id, 
            request_time=datetime.datetime.now()
        )
    
    await message.answer('Приветствую вас, этот бот поможет связаться вам с поддержкой')
    await message.answer(
        text='Для отправки сообщения поддержке нажмите на кнопку',
        reply_markup=kb.support
    )


@router.message(CommandStart(ignore_case=True), InTopic())
async def topic_start(message: Message) -> None:
    await message.answer('Для просмотра действий доступных админу введите /admin_panel')
