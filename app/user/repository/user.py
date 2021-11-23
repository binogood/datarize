from abc import ABCMeta, abstractmethod
from typing import Optional

from app.user.models.user import User
from core.db.session import session


class UserRepo:
    __metaclass__ = ABCMeta

    @abstractmethod
    async def get_by_id(self, user_id: int) -> Optional[User]:
        pass

    @abstractmethod
    async def get_by_email(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    async def save(self, user:User) -> User:
        pass


class UserMySQLRepo(UserRepo):
    async def get_by_id(self, user_id: int) -> Optional[User]:
        pass

    async def get_by_email(self, email: str) -> Optional[User]:
        return (
            session.query(User)
            .filter(User.email == email).first()
        )

    async def save(self, user: User) -> User:
        session.add(User)
        return user