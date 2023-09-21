# Описание проекта
Небольшое API, которое позволяет:
1) Передать пользователю данные(первое число, второе число и оператора) и получить в ответ id созданной задачи. Новой задаче автоматически присваивается статус 'started' и результат 'in process';
2) По id задачи пользователь может получить результат выполнения задачи;
3) Посмотреть информацию по всем задачам в БД(по каждой задаче выводится ее id и статус).

Документация к API - http://0.0.0.0:8000/api/openapi
### Технологии
- [Python](https://www.python.org/) - is an interpreted high-level general-purpose programming language.
- [PostgeSQL](https://www.postgresql.org/) - is an open source object-relational database system that uses and extends the SQL language combined with many features.
- [Docker](https://www.docker.com/) - is a set of platform as a service (PaaS) products that use OS-level virtualization to deliver software in packages (containers).
- [Gunicorn](https://gunicorn.org/) - is a Python WSGI HTTP Server for UNIX.
### Как развернуть проект
1. Переименовать ```.env.example``` в ```.env```
   
2. Скачать репозиторий, перейти в директорию с проектом

```git clone git@github.com:ваш-логин/api_pro.financy.git```

```cd /<путь-до-директории>/```

- создать виртуальное окружение, активировать его

```python3 -m venv venv```

```. venv/bin/activate```

- установить зависимости

```python -m pip install -r requirements.txt```

3. Выполнить команду ```docker compose up```
