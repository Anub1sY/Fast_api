from fastapi import FastAPI
from typing import List, Optional

app = FastAPI()

# Данные продуктов для примера
sample_products = [
    {"product_id": 123, "name": "Smartphone", "category": "Electronics", "price": 599.99},
    {"product_id": 456, "name": "Phone Case", "category": "Accessories", "price": 19.99},
    {"product_id": 789, "name": "Iphone", "category": "Electronics", "price": 1299.99},
    {"product_id": 101, "name": "Headphones", "category": "Accessories", "price": 99.99},
    {"product_id": 202, "name": "Smartwatch", "category": "Electronics", "price": 299.99},
]

"""
FastAPI приложение для управления продуктами.

Приложение предоставляет две конечные точки:
1. `/product/{product_id}` - для получения информации о продукте по его идентификатору.
2. `/products/search` - для поиска продуктов по ключевому слову, категории и ограничению количества результатов.
"""


# Шаг 2: Конечная точка для получения информации о продукте
@app.get("/product/{product_id}")
async def get_product(product_id: int):
    """
    Получает информацию о продукте по его идентификатору.

    Args:
    - product_id (int): Идентификатор продукта.

    Returns:
    - dict: Словарь с информацией о продукте или сообщение об ошибке, если продукт не найден.
    """
    product = next((p for p in sample_products if p["product_id"] == product_id), None)
    if product:
        return product
    else:
        return {"error": "Product not found"}


@app.get("/products/search")
async def search_products(keyword: str, category: Optional[str] = None, limit: Optional[int] = 10):
    """
    Выполняет поиск продуктов по ключевому слову и категории.

    Args:
    - keyword (str): Ключевое слово для поиска в названии продукта.
    - category (str, optional): Категория продукта для фильтрации.
    - limit (int, optional): Максимальное количество результатов для возврата.

    Returns:
    - List[dict]: Список словарей с информацией о продуктах, соответствующих критериям поиска.
    """
    filtered_products = [p for p in sample_products if keyword.lower() in p["name"].lower()]
    if category:
        filtered_products = [p for p in filtered_products if p["category"].lower() == category.lower()]
    return filtered_products[:limit]

# Примеры запросов:
# Получение информации о продукте
# curl -X GET "http://localhost:8000/product/123"

# Поиск товаров
# curl -X GET "http://localhost:8000/products/search?keyword=phone&category=Electronics&limit=5"
