from typing import Union, NoReturn, Optional

from sqlalchemy import Column, Integer, Unicode

from core.db.session import Base
from core.db.timestamp_mixin import TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    password = Column(Unicode(255), nullable=False)
    email = Column(Unicode(255), nullable=False, unique=True)

    def create(self, email: str, password: str) -> Union["User", NoReturn]:
        return User(email=email, password=password)