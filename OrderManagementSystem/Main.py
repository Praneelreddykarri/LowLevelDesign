from OrderManagementSystem import OrderManagementSystem

if __name__ == "__main__":
    manager = OrderManagementSystem()
    userA = manager.create_user("regular", "Praneel")
    userA_order_items = [("Apple", 1.5), ("Milk", 2.0)]
    manager.process_order(userA, userA_order_items)