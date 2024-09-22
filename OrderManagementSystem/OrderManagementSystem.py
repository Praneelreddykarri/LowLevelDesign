from OrderManager import OrderManager
from UserManager import UserManager
from Observer import UserNotification, AdminNotification
from OrderNotifier import OrderNotifier
import threading

class OrderManagementSystem:
    """Singleton class to manage order processing."""
    _instance=None
    _lock=threading.Lock()

    def __new__(cls):
        if(cls._instance is None):
            cls._lock.acquire()
            if (cls._instance is None):
                cls._instance = super().__new__(cls)
            cls._lock.release()
        return cls._instance


    def __init__(self):
        self.notifier = OrderNotifier()
        self.user_manager = UserManager()
        self.order_manager = OrderManager(self.notifier)


    def setup_observers(self,userID):
        """Attach observers to the notifier."""
        self.notifier.attach(userID, UserNotification())  # Example user ID

    def create_user(self, user_type, name):

        """Create a user using the UserManager."""
        return self.user_manager.create_user(user_type, name)

    def process_order(self, user, items):
        """Process an order using the OrderManager."""
        self.order_manager.create_order(user, items)
        self.setup_observers(user.user_id)




