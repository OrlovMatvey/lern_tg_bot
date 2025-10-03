"""Состояния для действия c вводом пользователя"""

from aiogram.fsm.state import StatesGroup, State


class SetUserInfo(StatesGroup):
    """Состояния для добавления ФИО пользователя"""

    input_FIO = State()
