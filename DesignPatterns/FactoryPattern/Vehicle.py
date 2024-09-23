from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def manufacture(self):
        pass
