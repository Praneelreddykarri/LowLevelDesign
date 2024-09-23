from Cache import Cache
from Node import Node
from CacheStrategy import CacheStrategy

class LRUCache(CacheStrategy):
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.cache_list = Cache()

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.cache_list.move_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.cache_list.move_to_head(node)
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.cache_list.add_node(new_node)

            if self.cache_list.size > self.capacity:
                lru_node = self.cache_list.remove_tail()
                if lru_node:
                    del self.cache[lru_node.key]
