from pydantic import BaseModel, Field, model_validator
from typing import Annotated
from datetime import datetime
from uuid import UUID


class Flight(BaseModel):
    id: Annotated[UUID, Field(strict=True)]
    flight_number: Annotated[str, Field(pattern=r"^[A-Z]{2}[0-9]{3,4}$")]
    airline: Annotated[str, Field(min_length=3, max_length=50)]
    departure: Annotated[str, Field(min_length=3, max_length=3)]
    arrival: Annotated[str, Field(min_length=3, max_length=3)]
    departure_time: datetime
    arrival_time: datetime

    @model_validator(mode="after")
    def arrival_time_validator(self):
        if self.departure_time >= self.arrival_time:
            raise ValueError("Arrival_time must be after departure_time")
        else:
            return self
