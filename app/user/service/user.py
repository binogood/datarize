
import jwt
import bcrypt

from typing import Optional, Union, NoReturn

from pythondi import inject

from core.config import config
from app.user.models.user import User
from app.user.repository.user import UserRepo
from core.db.transaction import Transaction, Propagation
from core.exceptions.user import (
    UserNotFoundException,
    DuplicateEmailException,
)


class UserService:
    @inject()
    def __init__(self, user_repo: UserRepo):
        self.user_repo = user_repo

    @Transaction(propagation=Propagation.REQUIRED)
    async def create_user(self, email: str, password: str) -> Union[User, NoReturn]:
        if await self.user_repo.get_by_user(email=email):
            raise DuplicateEmailException

        hash_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode('utf-8')
        user = User().create(
            email=email, password=hash_pw
        )
        user = await self.user_repo.save(user=user)
        return user

    @Transaction(propagation=Propagation.REQUIRED)
    async def login_user(self, email: str, password: str) -> Optional[User]:
        user = await self.user_repo.get_by_user(email)
        hash_pw = await self.user_repo.check_password(user, password)
        if not hash_pw:
            raise UserNotFoundException

        access_token = jwt.encode(
            {'user': user.id},
            config.JWT_SECRET_KEY,
            algorithm=config.JWT_ALGORITHM)
        return access_token
