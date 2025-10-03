"""Клавиатуры для выбора группы"""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from controllers.course import get_courses


def get_user_group_kb(user_tg_id: int) -> InlineKeyboardMarkup:

    inline_keyboard = [
        [
            InlineKeyboardButton(
                text=group["name"], callback_data=f"user_group_{usergroup['id']}"
            )
        ]
        for course in get_courses(user_tg_id=user_tg_id)
    ]
