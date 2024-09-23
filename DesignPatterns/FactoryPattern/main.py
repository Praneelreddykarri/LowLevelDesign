from VehicleFactory import VehicleFactory

def main():
    vehicle_type = input("Enter the type of vehicle (car, bike, truck): ").lower()

    try:
        vehicle = VehicleFactory.create_vehicle(vehicle_type)
        print(vehicle.manufacture())
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
