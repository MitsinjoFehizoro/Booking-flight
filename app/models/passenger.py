from pydantic import BaseModel, Field, EmailStr, field_validator
from uuid import UUID, uuid4
from typing import Annotated
from datetime import date


class Passenger(BaseModel):
    id: Annotated[UUID, Field(strict=True)]
    last_name: Annotated[str, Field(min_length=2, max_length=30)]
    first_name: Annotated[str, Field(min_length=2, max_length=50)]
    email: EmailStr
    birth_date: date

    @field_validator("last_name", mode="after")
    @classmethod
    def upper_last_name(cls, value: str):
        return value.upper()

    @field_validator("first_name", mode="after")
    def capitalize_firt_name(cls, value: str):
        return value.capitalize()

    @field_validator("birth_date", mode="after")
    @classmethod
    def verify_age_of_passenger(cls, value: date):
        age = date.today().year - value.year
        if age < 16:
            raise ValueError("The passenger must be at least 16 years old.")
        else:
            return value
