from Node import Node

class Cache:
    def __init__(self):
        self.head = None  # Most recently used node
        self.tail = None  # Least recently used node
        self.size = 0

    def add_node(self, node: Node):
        """Add a node at the front (most recently used)."""
        if not self.head:
            # If the cache is empty, initialize head and tail
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        self.size += 1

    def remove_node(self, node: Node):
        """Remove an existing node from the linked list."""
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        self.size -= 1

    def move_to_head(self, node: Node):
        """Move a given node to the front (most recently used)."""
        self.remove_node(node)
        self.add_node(node)

    def remove_tail(self) -> Node:
        """Remove and return the least recently used node."""
        if self.size == 0:
            return None
        lru_node = self.tail
        self.remove_node(lru_node)
        return lru_node
