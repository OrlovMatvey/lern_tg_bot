"""Пользователь прикрпленный к учебной группе"""

from peewee import ForeignKeyField
from .table import Table
from .user import User
from .group import Group


class UserGroup(Table):
    """Пользователь прикрпленный к учебной группе"""

    user = ForeignKeyField(model=User)
    group = ForeignKeyField(model=Group)

    def __iter__(self):
        yield "id", self.id
        yield "user_id", self.user_id
        yield "group_id", self.group_id
