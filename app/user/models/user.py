from typing import Union, NoReturn

from sqlalchemy import Column, Integer, Unicode, DateTime, func

from core.db.session import Base
from core.db.timestamp_mixin import TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    password = Column(Unicode(255), nullable=False)
    email = Column(Unicode(255), nullable=False, unique=True)
    created_at = Column(
                        DateTime,
                        nullable=False,
                        default=func.utc_timestamp(),
                        onupdate=func.utc_timestamp()
                )
    updated_at = Column(
                        DateTime,
                        nullable=False,
                        default=func.utc_timestamp(),
                        onupdate=func.utc_timestamp()
                )

    def create(self, email: str, password: str) -> Union["User", NoReturn]:
        return User(email=email, password=password)