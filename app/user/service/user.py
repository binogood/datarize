from typing import Optional, Union, NoReturn

from app.user.models.user import User
from app.user.repository.user import UserRepo
from core.db.transaction import Transaction, Propagation
from core.exceptions.user import (
    UserNotFoundException,
    DuplicateEmailException,
)


class UserService:
    def __init__(self, user_repo: UserRepo):
        self.user_repo = user_repo

    @Transaction(propagation=Propagation.REQUIRED)
    async def create_user(self, email: str, password: str) -> Union[User, NoReturn]:
        if await self.user_repo.get_by_email(email=email):
            raise DuplicateEmailException

        user = User().create(
            email=email, password=password
        )
        user = await self.user_repo.save(user=user)
        return user

    async def get_user(self, user_id: int) -> Optional[User]:
        user = await self.user_repo.get_by_id(user_id=user_id)
        if not user:
            raise UserNotFoundException

        return user
