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