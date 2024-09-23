# Factory Design Pattern

## What is the Factory Design Pattern?

The **Factory Design Pattern** is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

In simpler terms, the **Factory Pattern** defines a method for creating objects but lets the subclasses decide which class to instantiate. The main advantage is that it promotes loose coupling by delegating the responsibility of object creation to a factory class rather than handling it in client code.

## Use Case

The Factory Design Pattern is useful when:
- You have a common interface or abstract class (e.g., `Vehicle`) and you need to create instances of different classes (e.g., `Car`, `Bike`, `Truck`) based on some input or condition.
- You want to centralize object creation to make your code more flexible and scalable.
- You aim to reduce dependencies between client code and the classes it needs to instantiate.

### Benefits:
- **Loose Coupling:** The code that uses the factory doesn’t need to know the details of how the objects are created or which specific class to instantiate.
- **Extensibility:** It’s easier to add new types without modifying existing code (just extend the factory to support the new type).

## Factory Pattern Example

### Problem:
Suppose you are building a vehicle manufacturing system where different types of vehicles need to be produced (e.g., Cars, Bikes, Trucks). Each type of vehicle has a different manufacturing process, but they all share a common interface (i.e., `Vehicle`).

Instead of letting the client code decide which vehicle to instantiate, you can use a **VehicleFactory** to handle this. The factory will create and return the appropriate vehicle object based on the input.

### Structure:
1. **Base Class/Interface** (`Vehicle`): Defines the common interface for all vehicle types.
2. **Concrete Classes** (`Car`, `Bike`, `Truck`): These classes inherit from the `Vehicle` class and implement their own version of the `manufacture` method.
3. **Factory Class** (`VehicleFactory`): This class contains a method that creates instances of `Car`, `Bike`, or `Truck` based on input.

### Code Example:

```python
# check my repository for full code

class Vehicle:
    def manufacture(self):
        pass

class Car(Vehicle):
    def manufacture(self):
        return "Car has been manufactured"

class Bike(Vehicle):
    def manufacture(self):
        return "Bike has been manufactured"

class Truck(Vehicle):
    def manufacture(self):
        return "Truck has been manufactured"

# Factory Class
class VehicleFactory:
    def create_vehicle(vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()
        elif vehicle_type == "truck":
            return Truck()
        else:
            raise ValueError("Unknown vehicle type")
