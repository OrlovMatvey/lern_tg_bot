"""Модуль содержит функции работы с пользователем"""

from models import User


def get_user_by_tg_id(user_tg_id: int) -> dict:
    '''Вернуть информацию о пользователе'''

    user = User.get_or_none(tg_id=user_tg_id)

    if user is None:
        raise ValueError(
            f"Пользователь с ID '{user_tg_id}' не найден"
        )

    return dict(user)


def set_user_fio(user_tg_id: int, fio: str) -> dict:
    '''Записываем ФИО пользователя и возращаем словарь'''

    user = User.get_or_none(tg_id=user_tg_id)

    if user is None:
        raise ValueError(
            f"Пользователь с ID '{user_tg_id}' не найден"
        )

    user.fio = fio
    user.save()
    return dict(user)
