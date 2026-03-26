# This class represents a service record
class ServiceRecord:
    def __init__(self, registration, date, service_type, cost, notes):
        # Store service details
        self.registration = registration
        self.date = date
        self.service_type = service_type
        self.cost = cost
        self.notes = notes

    # Return readable format
    def __str__(self):
        return f"{self.registration} | {self.date} | {self.service_type} | £{self.cost} | {self.notes}"