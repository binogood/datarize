from typing import Optional, Union, NoReturn

from app.task.models.task import Task
from app.task.repository.task import TaskRepo
from core.db.transaction import Transaction, Propagation
from core.exceptions.user import (
    UserNotFoundException,
    DuplicateEmailException,
)


class TaskService:
    def __init__(self, task_repo: TaskRepo):
        self.task_repo = task_repo

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
