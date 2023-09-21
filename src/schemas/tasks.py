from typing import Optional

from pydantic import BaseModel, Field


# Модели для валидации входящих запросов и отправляемых ответов API
class TaskCreate(BaseModel):
    first_number: int = Field(title='First number')
    second_number: int = Field(title='Second number')
    operator: str = Field(title='Operator')


class TaskInDb(BaseModel):
    id: str = Field(title='Task id')

    class Config:
        orm_mode = True


class TaskResult(BaseModel):
    result: Optional[str] = Field(title='Task result')


class TaskStatus(BaseModel):
    id: str = Field(title='Task id')
    status: Optional[str] = Field(title='Task status')
