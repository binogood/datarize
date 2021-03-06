from abc import ABCMeta, abstractmethod
from typing import Optional

from app.user.models.user import User
from core.db.session import session


class UserRepo:
    __metaclass__ = ABCMeta

    @abstractmethod
    async def get_by_user(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    async def save(self, user: User) -> User:
        pass


class UserMySQLRepo(UserRepo):
    async def get_by_user(self, email: str) -> Optional[User]:
        return session.query(User).filter(User.email == email).first()

    async def save(self, user: User) -> User:
        session.add(user)
        return user

