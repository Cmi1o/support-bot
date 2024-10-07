import app.utils.keyboards as kb
import requests

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.filters import InChat, InTopic, FailCommand
from config import bot_token
from database import controller



router = Router()

@router.message(InTopic(), FailCommand())
async def fail_command_echo(message: Message) -> None:
    await message.answer('Этой команды не существует, попробуйте другую')


@router.message(InTopic(), F.text)
async def topic_echo(message: Message) -> None: 
    user = await controller.users.get_by(thread_id=message.message_thread_id)
    
    if user and user.telegram_id:
        await requests.send_message(
            bot_token=bot_token, 
            chat_id=user.telegram_id, 
            text=f'Пришел ответ от администратора:'
        )
        
        await requests.send_copy(message, chat_id=user.telegram_id)
