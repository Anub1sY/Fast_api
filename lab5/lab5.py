from fastapi import FastAPI
from models import Feedback

app = FastAPI()

# Хранилище для отзывов
feedbacks = []


@app.post("/feedback")
async def submit_feedback(feedback: Feedback):
    """
    Обрабатывает POST-запрос на маршруте /feedback.

    Принимает данные JSON, представляющие отзыв, и сохраняет их в хранилище.

    Args:
    - feedback (Feedback): Объект Feedback с полями name и message.

    Returns:
    - dict: Словарь с сообщением об успешном получении отзыва.

    curl -X POST "http://localhost:8000/feedback" -H "Content-Type: application/json" -d "{\"name\": \"Alice\", \"message\": \"Great course! I'm learning a lot.\"}"

    """
    feedbacks.append(feedback.dict())
    return {
        "message": f"Feedback received. Thank you, {feedback.name}!"
    }
