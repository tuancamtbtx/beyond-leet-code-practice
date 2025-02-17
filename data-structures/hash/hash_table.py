class HashTable():
    def __init__(self,size):
        self.size = size
        self.hash_table = self.create_buckets()
    
    def create_buckets(self):
        return [ [] for _ in range(self.size)]
    
    def set_value(self, key, value):
        hashed_key =  hash(key) % self.size

        bucket = self.hash_table[hashed_key]
        found_key = False

        for index, record in enumerate(bucket):
            record_key , record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key == True:
            bucket[index] = (key, value)
        else:
            bucket.append((key, value))
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

def main():
    hash_table = HashTable(10)
    hash_table.set_value("a", 1)
    hash_table.set_value("a", 2)
    hash_table.set_value("tua", "quanma")

    print(hash_table)
if __name__ == "__main__":
    main()

class HashTable:
    def __init__(self, size=10):
        # Initialize hash table with empty buckets
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        """Compute the hash value for a given key."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash_function(key)
        # Check if the key already exists and update it
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # If key does not exist, append the new key-value pair
        self.table[index].append([key, value])

    def retrieve(self, key):
        """Retrieve the value associated with a given key."""
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # Key not found

    def remove(self, key):
        """Remove the key-value pair from the hash table."""
        index = self._hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False  # Key not found

# Example usage:
hash_table = HashTable()
hash_table.insert("name", "Alice")
hash_table.insert("age", 30)
hash_table.insert("city", "New York")

print("Retrieve 'name':", hash_table.retrieve("name"))  # Output: Alice
print("Retrieve 'age':", hash_table.retrieve("age"))    # Output: 30
print("Retrieve 'city':", hash_table.retrieve("city"))  # Output: New York

hash_table.remove("age")
print("Retrieve 'age' after removal:", hash_table.retrieve("age"))  # Output: None