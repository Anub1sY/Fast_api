from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

"""
Приложение FastAPI, которое обслуживает HTML-страницу по корневому URL.
"""


@app.get("/", response_class=HTMLResponse, tags=["Главная страница"])
async def read_root():
    """
    Обработчик GET-запроса для корневого URL.

    Возвращает:
    - HTMLResponse: HTML-страница, прочитанная из файла 'index1.html'.

    Эта функция открывает файл 'index1.html', читает его содержимое и возвращает в виде HTML-ответа.
    """
    with open("index1.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return html_content
