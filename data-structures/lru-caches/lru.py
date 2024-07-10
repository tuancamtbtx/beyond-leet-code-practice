from collections import OrderedDict


class LruCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def print_cache(self):
        for key, value in self.cache.items():
            print(f"{key}: {value}")


def main():
    lru = LruCache(3)
    lru.put(1, 1)
    lru.put(2, 2)
    lru.put(3, 3)

    lru.print_cache()

if __name__ == "__main__":
    main()