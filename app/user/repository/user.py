from abc import ABCMeta, abstractmethod
from typing import Optional

import bcrypt

from app.user.models.user import User
from core.db.session import session


class UserRepo:
    __metaclass__ = ABCMeta

    @abstractmethod
    async def get_by_user(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    async def check_password(self, email: str, password: str) -> Optional[User]:
        pass

    @abstractmethod
    async def save(self, user: User) -> User:
        pass


class UserMySQLRepo(UserRepo):
    async def check_password(self, user, password: str) -> bool:
        check_pw = bcrypt.checkpw(
            password.encode("utf8"),
            user.password.encode("utf-8")
        )
        return check_pw

    async def get_by_user(self, email: str) -> Optional[User]:
        return (
            session.query(User)
            .filter(User.email == email).first()
        )

    async def save(self, user: User) -> User:
        session.add(User)
        return user

