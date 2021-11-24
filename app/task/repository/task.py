from abc import ABCMeta, abstractmethod
from typing import Optional

from app.task.models.task import Task
from app.user.models.user import User
from core.db.session import session


class TaskRepo:
    __metaclass__ = ABCMeta

    @abstractmethod
    async def get_by_id(self, task_id: int) -> Optional[Task]:
        pass

    @abstractmethod
    async def get_by_task_user_id(self, task: Task, user: User) -> Optional[Task]:
        pass

    @abstractmethod
    async def get_by_task_list(self, user_id: int) -> Optional[Task]:
        pass

    @abstractmethod
    async def all_task_delete(self, task: Task, user: User) -> None:
        pass

    @abstractmethod
    async def task_delete(self, task: Task) -> None:
        pass

    @abstractmethod
    async def save(self, task: Task) -> Task:
        pass


class TaskMySQLRepo(TaskRepo):
    async def get_by_id(self, task_id: int) -> Optional[Task]:
        pass

    async def get_by_task_user_id(self, task: Task, user: User) -> Optional[Task]:
        return (
            session.query(Task)
            .filter(Task.user_id == user.id, Task.id == task.id)
            .first()
        )

    async def get_by_task_list(self, user: User) -> Optional[Task]:
        return session.query(Task).filter(Task.user_id == user.id)

    async def save(self, task: Task) -> Task:
        session.add(task)
        return task

    async def all_task_delete(self, task: Task, user: User) -> None:
        session.delete(task.user_id == user.id)

    async def task_delete(self, task: Task) -> None:
        session.delete(task.id)
