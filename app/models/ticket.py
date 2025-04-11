from pydantic import BaseModel, PositiveFloat, Field
from uuid import UUID
from typing import Annotated, Literal
from datetime import datetime
from .passenger import Passenger
from .flight import Flight


class Ticket(BaseModel):
    id: Annotated[UUID, Field(strict=True)]
    passenger: Passenger
    flight: Flight
    travel_class: Literal["economy", "business", "first"]
    price: PositiveFloat

    def to_json(self):
        return self.model_dump_json()
