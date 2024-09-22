from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, user_id, message):
        pass

class UserNotification(Observer):
    def update(self, user_id, message):
        print(f"User {user_id} Notification: {message}")

class AdminNotification(Observer):
    def update(self, user_id, message):
        print(f"Admin Notification for User {user_id}: {message}")
