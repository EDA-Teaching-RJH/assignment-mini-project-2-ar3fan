from validators import validate_registration


# This class represents a vehicle
class Vehicle:
    def __init__(self, registration, make, model, year):
        # Validate registration using regex
        if not validate_registration(registration):
            raise ValueError("Invalid registration format")

        # Store vehicle details
        self.registration = registration
        self.make = make
        self.model = model
        self.year = year

    # Return a readable string for printing
    def __str__(self):
        return f"{self.registration} - {self.make} {self.model} ({self.year})"


# Car class inherits from Vehicle
class Car(Vehicle):
    def __init__(self, registration, make, model, year, mileage):
        # Call parent constructor
        super().__init__(registration, make, model, year)

        # Store additional attribute
        self.mileage = mileage