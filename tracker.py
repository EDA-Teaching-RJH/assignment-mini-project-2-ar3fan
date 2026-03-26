import csv


# This class manages vehicles and service records
class ServiceTracker:
    def __init__(self):
        self.vehicles = []
        self.records = []

    # Add a vehicle to the list
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    # Add a service record
    def add_service(self, record):
        self.records.append(record)

    # Display all vehicles
    def view_vehicles(self):
        for vehicle in self.vehicles:
            print(vehicle)

    # Display all service records
    def view_services(self):
        for record in self.records:
            print(record)

    # Save vehicles to CSV file
    def save_vehicles(self):
        with open("vehicles.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["registration", "make", "model", "year", "mileage"])

            for vehicle in self.vehicles:
                writer.writerow([
                    vehicle.registration,
                    vehicle.make,
                    vehicle.model,
                    vehicle.year,
                    vehicle.mileage
                ])

    # Load vehicles from CSV file
    def load_vehicles(self):
        try:
            with open("vehicles.csv", "r") as file:
                reader = csv.reader(file)
                next(reader)

                from vehicle import Car

                for row in reader:
                    registration, make, model, year, mileage = row
                    car = Car(registration, make, model, int(year), int(mileage))
                    self.vehicles.append(car)

        except FileNotFoundError:
            print("No file found.")