from aiogram import Dispatcher

from . import set_fio


def add_routers(dp: Dispatcher) -> None:
    """Добавляет роутеры в диспетчер"""

    dp.include_routers(set_fio.router)
