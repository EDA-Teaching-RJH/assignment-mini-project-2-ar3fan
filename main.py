from vehicle import Car
from service_record import ServiceRecord
from tracker import ServiceTracker

tracker = ServiceTracker()

# Load existing vehicles
tracker.load_vehicles()

# Only add car if list is empty (prevents duplicates)
if len(tracker.vehicles) == 0:
    car1 = Car(""AB12CDE"", "Audi", "A1", 2014, 100000)
    tracker.add_vehicle(car1)

# Add a service record (you can improve this later)
service1 = ServiceRecord("AB12CDE", "2026-03-26", "Oil Change", 120, "Changed oil and filter")
tracker.add_service(service1)

print("Vehicles:")
tracker.view_vehicles()

print("\nService Records:")
tracker.view_services()

# Save vehicles
tracker.save_vehicles()