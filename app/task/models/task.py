from typing import Union, NoReturn, Optional

from sqlalchemy import Column, Integer, ForeignKey, Boolean, String

from core.db.session import Base
from core.db.timestamp_mixin import TimestampMixin


class Task(Base, TimestampMixin):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    name = Column(String(length=50), nullable=False)
    completed = Column(Boolean, nullable=False, default=False)

    def create(self, name: str, user_id: int) -> Union["Task", NoReturn]:
        return Task(name=name, user_id=user_id)
