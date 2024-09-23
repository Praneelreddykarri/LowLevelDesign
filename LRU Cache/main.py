from LRUCache import LRUCache

def test_lru_cache():
    """Test cases for LRU Cache."""
    print("Testing LRU Cache:")
    lru_cache = LRUCache(2)
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    print(lru_cache.get(1))  # Expected: 1
    lru_cache.put(3, 3)      # Evicts key 2
    print(lru_cache.get(2))  # Expected: -1 (not found)
    lru_cache.put(4, 4)      # Evicts key 1
    print(lru_cache.get(1))  # Expected: -1 (not found)
    print(lru_cache.get(3))  # Expected: 3
    print(lru_cache.get(4))  # Expected: 4


def main():
    """Main function to run cache tests."""
    test_lru_cache()

if __name__ == "__main__":
    main()
