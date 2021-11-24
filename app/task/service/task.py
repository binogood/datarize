from typing import Optional, Union, NoReturn

from pythondi import inject

from app.task.models.task import Task
from app.user.models.user import User

from app.task.repository.task import TaskRepo
from core.db.transaction import Transaction, Propagation
from core.exceptions.task import TaskNotFoundException
from core.utiles.token_helper import TokenHelper


class TaskService:
    @inject()
    def __init__(self, task_repo: TaskRepo):
        self.task_repo = task_repo

    @Transaction(propagation=Propagation.REQUIRED)
    async def create_task(self, name: str, token: str) -> Union[Task, NoReturn]:
        user = self._check_user(token)
        print(user)
        task = Task.create(user_id=user, name=name)
        task = await self.task_repo.save(task)
        return task

    @Transaction(propagation=Propagation.REQUIRED)
    async def update_task(self, task_id: int, name: str, completed: bool, token: str) -> Union[Task, NoReturn]:
        task = Task.update(task_id=task_id, name=name, completed=completed)


    async def get_task(self, task_id: int, token: str) -> Optional[Task]:
        task = await self.task_repo.get_by_id(task_id)
        if not task:
            raise TaskNotFoundException

        return task

    async def all_get_task(self, user_id: int, token: str) -> Optional[Task]:
        task_list = await self.task_repo.get_by_task_list(user_id)
        if not task_list:
            raise TaskNotFoundException

        return task_list

    async def _check_user(self, token: str) -> Union[User, NoReturn]:
        return await TokenHelper.decode(token)