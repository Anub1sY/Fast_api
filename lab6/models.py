from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: Optional[int] = None
    is_subscribed: Optional[bool] = False

    @field_validator('age')
    def validate_age(cls, value):
        if value is not None and value < 0:
            raise ValueError("Age must be a positive integer or None")
        return value
