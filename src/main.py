from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1 import tasks
from core.config import settings
from db.postgres import create_database, purge_database

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)


@app.on_event('startup')
async def startup():
    # Импорт моделей необходим для их автоматического создания
    from models.tasks import Task
    await create_database()


@app.on_event('shutdown')
async def shutdown():
    await purge_database()

app.include_router(tasks.router, prefix='/api/v1/tasks', tags=['tasks'])
