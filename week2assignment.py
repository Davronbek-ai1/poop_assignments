class ConcertHall:
    def __init__(self, name: str, total_seats: int, booked_seats: int = 0) -> None:
        self._name = name
        self.total_seats = total_seats
        self.booked_seats = booked_seats
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def total_seats(self) -> int:
        return self._total_seats
    
    @total_seats.setter
    def total_seats(self, value: int) -> None:
        if value < 1:
            raise ValueError("Total seats must be at least 1")
        self._total_seats = value

    @property
    def booked_seats(self) -> int:
        return self._booked_seats
    
    @booked_seats.setter
    def booked_seats(self, value: int) -> None:
        if value < 0 :
            raise ValueError("Booked seats cannot be negative")
        if value > self._total_seats:
            raise ValueError("Booked seats cannot exceed total seats")
        self._booked_seats = value

    @property
    def available_seats(self) -> int:
        return self._total_seats - self._booked_seats
    
    @property
    def booking_rate(self) -> float:
        return round(self._booked_seats / self._total_seats * 100, 1)
    
    def reserve(self, seats: int) -> None:
        if seats < 0:
            raise ValueError("Number of seats must be positive")
        if seats > self.available_seats:
            raise ValueError("Not enough available seats")
        self._booked_seats += seats

    def cancel(self ,seats: int) -> None:
        if seats < 0:
            raise ValueError("Number of seats must be positive")
        if seats > self._booked_seats:
            raise ValueError("Cannot cancel more than booked")
        self._booked_seats -= seats

h = ConcertHall("Grand", 200)
print(h.name, h.available_seats, h.booking_rate)

h.reserve(150)
print(h.booked_seats, h.booking_rate)

h.cancel(30)
print(h.available_seats)

try:
    h.reserve(100)
except ValueError as e:
    print(e)

try:
    h.name = "X"
except AttributeError:
    print("Cannot change hall name")
