from functools import lru_cache

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.postgres import get_session
from models.tasks import Task


class TaskService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_tasks(self) -> list[Task]:
        tasks = await self.session.execute(select(Task))
        return tasks.scalars().all()

    async def get_task_by_id(self, task_id: str) -> Task:
        task = await self.session.execute(select(Task).where(Task.id == task_id))
        return task.scalars().one_or_none()


@lru_cache()
def get_task_service(
        session: AsyncSession = Depends(get_session),
) -> TaskService:
    return TaskService(session)
