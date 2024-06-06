from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

# Имитация учетных данных пользователя
USERS = {
    "user1": "password1",
    "user2": "password2"
}

# Инициализация HTTP Basic Auth
security = HTTPBasic()


def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    """
    Аутентификация пользователя на основе предоставленных учетных данных.

    Args:
    - credentials (HTTPBasicCredentials): Учетные данные пользователя.

    Returns:
    - None: Если аутентификация успешна.

    Raises:
    - HTTPException: Если учетные данные неверны или не предоставлены.
    """
    correct_username = USERS.get(credentials.username)
    if not correct_username or correct_username != credentials.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )


# Маршруты
@app.get("/login", dependencies=[Depends(authenticate)])
async def login():
    """
    Конечная точка для аутентификации пользователя.

    Returns:
    - dict: Секретное сообщение, если аутентификация успешна.
    """
    return {"message": "You got my secret, welcome"}
