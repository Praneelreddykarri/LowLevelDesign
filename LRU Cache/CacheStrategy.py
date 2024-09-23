from abc import ABC, abstractmethod

class CacheStrategy(ABC):
    @abstractmethod
    def put(self, key: int, value: int):
        pass

    @abstractmethod
    def get(self, key: int) -> int:
        pass
