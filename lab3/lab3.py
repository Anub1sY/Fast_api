from fastapi import FastAPI
from models import User

app = FastAPI()

# Создание экземпляра класса User
user = User(name="John Doe", id=1)


@app.get("/users")
async def get_user():
    """
    Обрабатывает GET-запрос на маршруте /users и возвращает данные о пользователе.

    Returns:
    - dict: Словарь с данными о пользователе.
    """
    return user.dict()
