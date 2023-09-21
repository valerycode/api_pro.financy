from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession

from db.postgres import get_session
from models.tasks import Task
from schemas.tasks import TaskCreate, TaskInDb, TaskResult, TaskStatus
from services.tasks import TaskService, get_task_service

router = APIRouter()


@router.post("/create_task", response_model=TaskInDb, status_code=HTTPStatus.CREATED)
async def create_task(data: TaskCreate, db: AsyncSession = Depends(get_session)) -> TaskInDb:
    task_dto = jsonable_encoder(data)
    new_task = Task(**task_dto)
    try:
        db.add(new_task)
    except:
        await db.rollback()
    else:
        new_task.status = 'started'
        new_task.result = 'in process'
        await db.commit()
        await db.refresh(new_task)
    return new_task


@router.get("/{task_id}", response_model=TaskResult)
async def task_details(task_id: int, task_service: TaskService = Depends(get_task_service)) -> TaskResult:
    task = await task_service.get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=f'Task with id {task_id} not found')
    return TaskResult(result=task.result)


@router.get("/", response_model=list[TaskStatus])
async def get_tasks(task_service: TaskService = Depends(get_task_service)) -> list[TaskStatus]:
    tasks = await task_service.get_tasks()
    if not tasks:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Tasks not found')
    return [TaskStatus(id=task.id, status=task.status) for task in tasks]
