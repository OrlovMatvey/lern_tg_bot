"""Модуль добавления пользователем ФИО"""

from aiogram import Router, F
from aiogram.types import Message, ContentType
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramBadRequest

from controllers.user import set_user_fio
from states.user import SetUserInfo

router = Router()


@router.message(
    SetUserInfo.input_FIO,
    F.content_type == ContentType.TEXT,
    )
async def input_user_fio_handler(
    message: Message, state: FSMContext
) -> None:
    """Обрабатываем ввод ФИО пользователя"""
    try:
        set_user_fio(user_tg_id=message.from_user.id, fio=message.text)
        await message.answer(
            text=f"Приятно познакомиться, {message.text}"
        )
        await state.clear()
    except TelegramBadRequest as ex:
        print("input_user_fio_handler", message.from_user.id, ex)
    except ValueError as ex:
        await message.answer(text=str(ex))
