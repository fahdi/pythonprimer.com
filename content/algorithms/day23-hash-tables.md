---
title: "Day 23: Hash Tables"
weight: 23
menu:
  main:
    parent: "Algorithms"
    weight: 23
---

# Hash Tables

Welcome to Day 23 of our 60 Days of Coding Algorithm Challenge! Today, we'll dive into Hash Tables, a fundamental data structure that provides efficient insertion, deletion, and lookup operations. Hash tables are widely used in various applications due to their average-case constant time complexity for these operations.

## What is a Hash Table?

A hash table is a data structure that implements an associative array abstract data type, a structure that can map keys to values. It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.

## How Hash Tables Work

1. **Hash Function**: Converts keys into array indices.
2. **Collision Resolution**: Handles cases where two keys hash to the same index.

## Hash Functions

A good hash function should:
1. Be deterministic: same input always produces the same output.
2. Distribute keys uniformly across the array.
3. Be efficient to compute.

Example of a simple hash function:

```python
def simple_hash(key, table_size):
    return sum(ord(char) for char in str(key)) % table_size
```

## Collision Resolution Techniques

### 1. Chaining

In chaining, each bucket is independent, and has some sort of list of entries with the same index. The time for hash table operations is the time to find the bucket (constant) plus the time for the list operation.

### 2. Open Addressing

In open addressing, all entry records are stored in the bucket array itself. When a new entry has to be inserted, the buckets are examined, starting with the hashed-to slot and proceeding in some probe sequence, until an unoccupied slot is found.

## Implementing a Hash Table with Chaining

Let's implement a basic hash table using chaining for collision resolution:

```python
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        raise KeyError(key)

    def remove(self, key):
        index = self._hash(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]
                return
        raise KeyError(key)

    def __str__(self):
        return str(self.table)

# Example usage
ht = HashTable()
ht.insert("apple", 5)
ht.insert("banana", 7)
ht.insert("orange", 3)

print(ht)
print(ht.get("banana"))  # Output: 7

ht.remove("banana")
print(ht)

try:
    ht.get("banana")
except KeyError:
    print("KeyError: 'banana' not found")
```

## Time Complexity

For a good hash function and a reasonable load factor:

- Insert: O(1) average case, O(n) worst case
- Delete: O(1) average case, O(n) worst case
- Search: O(1) average case, O(n) worst case

Where n is the number of key-value pairs in the hash table.

## Load Factor and Resizing

The load factor of a hash table is the ratio of the number of stored elements to the size of the hash table. As the load factor increases, the probability of collisions increases.

To maintain performance, the hash table should be resized when the load factor exceeds a certain threshold (typically 0.7 or 0.75). Resizing involves creating a new, larger array and rehashing all existing elements.

## Applications of Hash Tables

1. **Database Indexing**: For quick data retrieval.
2. **Caches**: To store and retrieve data quickly.
3. **Symbol Tables**: In compilers and interpreters.
4. **Associative Arrays**: Implementation in many programming languages.
5. **Cryptography**: For storing passwords securely.
6. **Blockchain**: For efficient data storage and retrieval.

## Advantages and Disadvantages

### Advantages:
1. Fast lookups: Average time complexity of O(1) for search, insert, and delete.
2. Flexible keys: Can use complex objects as keys.

### Disadvantages:
1. Unordered: Unlike arrays or linked lists, hash tables are inherently unordered.
2. Collisions: Need to handle collisions, which can degrade performance.
3. Space overhead: May require more memory than arrays.

## Exercise

1. Implement a hash table using open addressing with linear probing for collision resolution.
2. Create a function to find the first non-repeating character in a string using a hash table.
3. Implement a method to resize the hash table when the load factor exceeds 0.75.

## Summary

Today, we explored Hash Tables, a powerful data structure that provides efficient key-value pair storage and retrieval. We discussed the core concepts of hash functions and collision resolution techniques, and implemented a basic hash table using chaining.

Understanding hash tables is crucial for solving a wide range of problems efficiently, especially those involving quick lookups or avoiding duplicate values. As we progress through this challenge, you'll find hash tables being used in various algorithms and applications.

Tomorrow, we'll dive into string algorithms, exploring techniques for pattern matching and string manipulation. Stay tuned!

