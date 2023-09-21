from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from db.postgres import Base


# Модель для БД
class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    first_number = Column(Integer)
    second_number = Column(Integer)
    operator = Column(String(50))
    result = Column(String(255))
    status = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, first_number: int, second_number: int, operator: str) -> None:
        self.first_number = first_number
        self.second_number = second_number
        self.operator = operator

    def __repr__(self) -> str:
        return f'<Task {self.id}>'
