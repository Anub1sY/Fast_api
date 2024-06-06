from fastapi import FastAPI, HTTPException, Response, status
from typing import Optional

app = FastAPI()

# Имитация учетных данных пользователя
fake_users_db = {
    "user123": "password123"
}

"""
FastAPI приложение для аутентификации на основе файлов cookie.

Приложение предоставляет две конечные точки:
1. `/login` - для аутентификации пользователя и установки файла cookie "session_token".
2. `/user` - для проверки аутентификации с использованием файла cookie "session_token".
"""


# Маршруты
@app.post("/login")
async def login(username: str, password: str, response: Response):
    """
    Аутентификация пользователя и установка файла cookie "session_token".

    Args:
    - username (str): Имя пользователя.
    - password (str): Пароль пользователя.
    - response (Response): Объект ответа для установки файла cookie.

    Returns:
    - dict: Сообщение об успешной аутентификации.

    Raises:
    - HTTPException: Если имя пользователя или пароль неверны.
    """
    if username in fake_users_db and fake_users_db[username] == password:
        # Установка файла cookie
        response.set_cookie(key="session_token", value="abc123xyz456", httponly=True)
        return {"message": "Logged in successfully"}
    else:
        raise HTTPException(status_code=401, detail="Incorrect username or password")


@app.get("/user")
async def read_user(session_token: Optional[str] = None):
    """
    Проверка аутентификации пользователя с использованием файла cookie "session_token".

    Args:
    - session_token (str, optional): Значение файла cookie "session_token".

    Returns:
    - dict: Информация о пользователе, если аутентификация успешна.

    Raises:
    - HTTPException: Если файл cookie "session_token" отсутствует или недействителен.
    """
    if session_token == "abc123xyz456":
        return {"username": "user123", "message": "Access granted"}
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")
