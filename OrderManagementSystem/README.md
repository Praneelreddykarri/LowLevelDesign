# Order Management System

## Table of Contents
1. [Requirements](#requirements)
   - [User Management](#user-management)
   - [Order Management](#order-management)
   - [Discount Application](#discount-application)
   - [Notifications](#notifications)
   - [State Management](#state-management)
   - [Thread Safety](#thread-safety)
2. [Design Patterns Used](#design-patterns-used)
3. [SOLID Principles Used](#solid-principles-used)
4. [Conclusion](#conclusion)

---

## Requirements

### User Management
- **User Creation**: Ability to create different types of users (Regular and VIP) to cater to varying customer needs.
- **Discount Strategies**: Assign appropriate discount strategies based on user type, enhancing the customer experience and driving sales.

### Order Management
- **Order Creation**: Create and process orders with an auto-incremented order ID for easy tracking and management.
- **Order Lifecycle**: Maintain a record of active orders and allow removal after processing to ensure a tidy and efficient system.

### Discount Application
- **Dynamic Discounts**: Apply discounts based on user type during the order process, incentivizing purchases and increasing customer loyalty.

### Notifications
- **Lifecycle Notifications**: Notify users and admins at various stages of the order lifecycle (creation, confirmation, processing, dispatch, and delivery) to keep all stakeholders informed and engaged.

### State Management
- **State Transitions**: Implement state transitions for orders to accurately reflect their current status, improving clarity and communication throughout the order process.

### Thread Safety
- **Concurrent Handling**: Ensure that the Order Management System can handle concurrent requests safely, preventing data inconsistencies and ensuring a smooth user experience.

---

## Design Patterns Used

1. **Singleton Pattern**
   - The `OrderNotifier` class follows the Singleton design pattern, which ensures that only one instance of the notifier exists throughout the system. This is essential for managing notifications centrally for all orders, preventing duplication and confusion.

2. **Factory Pattern**
   - The Factory pattern is employed in the `UserFactory` class to create different types of users (Regular and VIP) based on the input provided. This pattern adheres to the Open/Closed Principle, allowing easy addition of new user types without modifying existing code, thereby maintaining system stability.

3. **Builder Pattern**
   - The `OrderBuilder` class uses the Builder pattern, which allows for the step-by-step construction of complex Order objects (such as adding items, applying discounts, etc.). This approach separates the construction process from the object representation, resulting in a more flexible and scalable codebase.

4. **State Pattern**
   - The State pattern is implemented through the `OrderState` and its subclasses (`CreatedState`, `ProcessState`, `ConfirmedState`, `DispatchedState`, and `DeliveredState`). This design enables the Order object to transition smoothly between different states, each encapsulating specific behaviors. It aligns with the Single Responsibility Principle by keeping the order state logic distinct from other order-related functionalities.

5. **Observer Pattern**
   - The Observer pattern is utilized in the `OrderNotifier` class, allowing multiple observers (such as `UserNotification` and `AdminNotification`) to receive real-time updates about order status changes. This design promotes a clean separation of concerns, decoupling the notification logic from order processing and supporting the Dependency Inversion Principle.

---

## SOLID Principles Used

1. **Single Responsibility Principle (SRP)**
   - Each class in the system has a distinct responsibility. For instance, the `User` class manages user-related functionality, while the `Order` class handles order management. This separation of concerns enhances maintainability and makes the system easier to understand.

2. **Open/Closed Principle (OCP)**
   - The design allows the system to be extended with new user types or order states without requiring modifications to existing code. By using patterns like Factory and State, we can add new functionality while keeping the existing system intact, reducing the risk of introducing bugs.

3. **Liskov Substitution Principle (LSP)**
   - Subtypes can be used interchangeably where a base type is expected. For example, both `VipUser` and `RegularUser` can be treated as instances of `User`. This ensures that the system behaves consistently regardless of the user type, enhancing code reusability.

4. **Interface Segregation Principle (ISP)**
   - The interfaces are designed to be small and specific to the needs of the clients. This prevents users from being forced to implement methods they don’t need, promoting a cleaner and more efficient codebase.

5. **Dependency Inversion Principle (DIP)**
   - High-level modules (like `OrderManager`) rely on abstractions rather than concrete implementations (such as `User` or `Order`). This promotes loose coupling and allows for easier testing and maintenance of the system.

---

## Conclusion
The Order Management System showcases a robust architecture through the application of various design patterns and adherence to SOLID principles. This not only facilitates efficient order management but also ensures the system is adaptable and maintainable. 
