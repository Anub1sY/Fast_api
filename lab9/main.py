from fastapi import FastAPI, HTTPException
from typing import Dict

app = FastAPI()


# Маршруты
@app.get("/headers")
async def read_headers(user_agent: str = None, accept_language: str = None) -> Dict[str, str]:
    """
    Конечная точка для извлечения и возврата заголовков запроса.

    Args:
    - user_agent (str): Заголовок "User-Agent" запроса.
    - accept_language (str): Заголовок "Accept-Language" запроса.

    Returns:
    - dict: Словарь с заголовками и их значениями.

    Raises:
    - HTTPException: Если заголовки "User-Agent" или "Accept-Language" отсутствуют.
    """
    if not user_agent:
        raise HTTPException(status_code=400, detail="Missing 'User-Agent' header")
    if not accept_language:
        raise HTTPException(status_code=400, detail="Missing 'Accept-Language' header")

    # Проверка формата заголовка "Accept-Language"
    if not is_valid_accept_language(accept_language):
        raise HTTPException(status_code=400, detail="Invalid 'Accept-Language' format")

    return {
        "User-Agent": user_agent,
        "Accept-Language": accept_language
    }


def is_valid_accept_language(accept_language: str) -> bool:
    """
    Проверяет, что заголовок "Accept-Language" имеет правильный формат.

    Args:
    - accept_language (str): Значение заголовка "Accept-Language".

    Returns:
    - bool: True, если формат правильный, иначе False.
    """
    # Простая проверка формата, например, разделители запятые и точки с запятой
    parts = accept_language.split(',')
    for part in parts:
        if ';' not in part:
            continue
        lang, _ = part.split(';')
        if ',' in lang:
            return False
    return True
