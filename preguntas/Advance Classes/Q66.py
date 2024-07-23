# 66. Write a Python class to implement a basic hash table.

class HashTable:
    def __init__(self, size=10):
        """Initialize the hash table with a given size."""
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """Compute the hash value for a given key."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def get(self, key):
        """Retrieve the value associated with a given key."""
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def remove(self, key):
        """Remove the key-value pair associated with a given key."""
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return
        raise KeyError(f"Key '{key}' not found")

    def __str__(self):
        """Return a string representation of the hash table."""
        result = []
        for i, bucket in enumerate(self.table):
            if bucket:
                result.append(f"Index {i}: {bucket}")
        return "\n".join(result)


ht = HashTable()
ht.insert("apple", 1)
ht.insert("banana", 2)
ht.insert("orange", 3)
print("Hash Table:")
print(ht)
print("\nGet value for 'apple':", ht.get("apple"))
print("Get value for 'banana':", ht.get("banana"))
ht.remove("banana")
print("\nHash Table after removing 'banana':")
print(ht)
print("\nTrying to get value for 'banana' after removal:", ht.get("banana"))
