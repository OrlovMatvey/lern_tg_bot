"""ыыыы"""
from peewee import *
from typing import Any, Dict, List
from models import Group, UserGroup


def get_groups_by_user(user_tg_id: int) -> List[Dict[str, Any]]:
    """Вернуть список групп для выбора пользователем"""
    query = (Group
             .select(Group.name)
             .join(UserGroup, on=(Group.id == UserGroup.group_id))
             .where(UserGroup.user_id == user_tg_id))

    result = list(query)

    return result
