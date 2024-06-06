from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class CalculationRequest(BaseModel):
    num1: int
    num2: int


@app.post("/calculate")
async def calculate(request: CalculationRequest):
    """
    Обрабатывает POST-запрос на маршрут /calculate.

    Принимает два числа (num1 и num2) и возвращает их сумму.

    curl -X POST "http://localhost:8000/calculate" -H "Content-Type: application/json" -d "{\"num1\": 5, \"num2\": 10}"
    
    Args:
    - request (CalculationRequest): Объект запроса с полями num1 и num2.

    Returns:
    - dict: Словарь с результатом суммы чисел.
    """
    result = request.num1 + request.num2
    return {"result": result}