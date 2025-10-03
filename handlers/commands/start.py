"""Обработка команды start"""


from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext

from controllers.user import get_user_by_tg_id
from states.user import SetUserInfo

router = Router()


@router.message(CommandStart())
async def start_cmd(message: Message, state: FSMContext):
    """Обработчик команды start"""
    try:
        user = get_user_by_tg_id(user_tg_id=message.from_user.id)
        text = (
                    "Вы запустили бота для дистанционного изучения "
                    " программирования."
                )
        if user['fio'] is None:
            text += (
                "\n"
                "\n"
                "Введите ваше ФИО!"
            )
        await message.answer(text=text)
        if user['fio'] is None:
            await state.set_state(state=SetUserInfo.input_FIO)
    except ValueError as ex:
        await message.answer(text=str(ex))
    except TelegramBadRequest as ex:
        print("start_cmd", message.from_user.id, ex)
