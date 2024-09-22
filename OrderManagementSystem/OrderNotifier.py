from Observer import Observer

class OrderNotifier:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.observers = {}  # Initialize the observers dictionary
        return cls._instance

    def __init__(self):
        self.observers = {}

    def attach(self, user_id, observer):
        if user_id not in self.observers:
            self.observers[user_id] = []
        self.observers[user_id].append(observer)

    def detach(self, user_id, observer):
        if user_id in self.observers:
            self.observers[user_id].remove(observer)

    def notify(self, user_id, message):
        if user_id in self.observers:
            for observer in self.observers[user_id]:
                observer.update(user_id, message)