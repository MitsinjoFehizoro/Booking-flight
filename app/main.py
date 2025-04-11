from pydantic import ValidationError
from .models.passenger import Passenger
from .models.flight import Flight
from .models.ticket import Ticket
from uuid import uuid4
from datetime import date, datetime

data_passenger = {
    "id": uuid4(),
    "last_name": "ranaivoarisaona",
    "first_name": "mitsinjo fehizoro",
    "email": "mitsinjo@gmail.com",
    "birth_date": date(2009, 3, 26),
}

data_flight = {
    "id": uuid4(),
    "flight_number": "AF909",
    "airline": "Air Madagascar",
    "departure": "ABA",
    "arrival": "TYI",
    "departure_time": datetime(2025, 4, 15, 5, 30, 00),
    "arrival_time": datetime(2025, 4, 16, 6, 00, 00),
}

# Booking
data_ticket = {"id": uuid4(), "travel_class": "first", "price": 2154}


print("---------------------- Debut ---------------------------\n")
try:
    passenger = Passenger.model_validate(data_passenger)
    print("===== PASSENGER =====")
    print(f"{passenger}\n")

    flight = Flight.model_validate(data_flight)
    print("===== FLIGHT =====")
    print(f"{flight}\n")

    data_ticket["passenger"] = passenger
    data_ticket["flight"] = flight
    ticket = Ticket(**data_ticket)
    print("===== BOOKING FLIGHT =====")
    print(f"{ticket.to_json()}\n")

except ValidationError as e:
    print(e)

print("---------------------- Fin ---------------------------\n")
