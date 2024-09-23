# LRU Cache Implementation

## Requirements

The LRU (Least Recently Used) Cache is a data structure that provides a fixed-size cache that evicts the least recently used items when it reaches its capacity. The following requirements define its functionality:

1. **Capacity**: The cache should have a fixed size, defined at the time of its creation.
2. **Get Operation**: 
   - Retrieve a value by its key.
   - If the key exists, return the corresponding value and mark the key as recently used.
   - If the key does not exist, return -1.
3. **Put Operation**: 
   - Add a new key-value pair to the cache.
   - If the key already exists, update its value and mark it as recently used.
   - If adding a new key exceeds the cache's capacity, remove the least recently used item to make space.

## SOLID Principles Followed

1. **Single Responsibility Principle (SRP)**: 
   - Each class has a distinct responsibility. The `Node` class handles the data structure for storing key-value pairs, the `Cache` class manages the linked list for maintaining the order of usage, and the `LRUCache` class implements the caching logic.

2. **Open/Closed Principle (OCP)**: 
   - The design allows for extension without modifying existing code. New caching strategies can be added by creating new classes that inherit from the `CacheStrategy`.

3. **Liskov Substitution Principle (LSP)**: 
   - The `LRUCache` can be used in place of any class that implements the `CacheStrategy` interface, ensuring that derived classes adhere to the base class contract.

4. **Interface Segregation Principle (ISP)**: 
   - The `CacheStrategy` interface defines only the necessary methods for cache operations (`put` and `get`), allowing for a clean and focused interface.

5. **Dependency Inversion Principle (DIP)**: 
   - High-level modules (like `LRUCache`) depends on abstractions (such as the `CacheStrategy` interface) rather than concrete implementations. This design allows for flexibility and the ability to introduce new caching strategies without altering the high-level logic of the cache, promoting easier maintenance and scalability.

## Design Patterns Used

1. **Strategy Pattern**: 
   - The `CacheStrategy` interface allows for defining different caching strategies, enabling the use of various algorithms without modifying the existing codebase. This facilitates easy implementation of alternative caching mechanisms if required.

## Conclusion

This implementation of the LRU Cache meets the specified requirements while adhering to SOLID principles and utilizing design patterns to promote maintainability, scalability, and clarity. This structured approach allows for future enhancements and the ability to adapt to changing requirements with minimal disruption.

---