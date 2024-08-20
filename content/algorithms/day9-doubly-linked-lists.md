---
title: "Day 9: Doubly Linked Lists - Implementation and Comparison"
weight: 9
menu:
  main:
    parent: "Algorithms"
    weight: 9
---

# Doubly Linked Lists - Implementation and Comparison

Welcome to Day 9 of our 60 Days of Coding Algorithm Challenge! Today, we'll explore doubly linked lists, implement one from scratch, and compare it with singly linked lists.

## What is a Doubly Linked List?

A doubly linked list is a type of linked list where each node contains data and two pointers:
1. A pointer to the next node
2. A pointer to the previous node

This bi-directional linking allows for more flexible operations, especially when traversing the list in reverse or deleting nodes.

## Implementing a Doubly Linked List

Let's implement a doubly linked list with basic operations:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                
                return
            current = current.next

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")
```

## Comparing Singly and Doubly Linked Lists

### Advantages of Doubly Linked Lists:

1. **Bi-directional Traversal**: Can be traversed both forward and backward.
2. **Efficient Deletion**: Deleting a node is more efficient as we have direct access to the previous node.
3. **Insert Before Operation**: Inserting a node before a given node is easier.

### Disadvantages of Doubly Linked Lists:

1. **Extra Memory**: Requires extra space for the previous pointer.
2. **Complexity**: Implementation is slightly more complex due to the extra pointer.

## Time Complexity Comparison

| Operation | Singly Linked List | Doubly Linked List |
|-----------|--------------------|--------------------|
| Insertion at beginning | O(1) | O(1) |
| Insertion at end | O(n) | O(1) with tail pointer |
| Deletion at beginning | O(1) | O(1) |
| Deletion at end | O(n) | O(1) with tail pointer |
| Search | O(n) | O(n) |
| Reverse Traversal | O(n) | O(1) |

## Example Usage

```python
dll = DoublyLinkedList()

# Append elements
dll.append(1)
dll.append(2)
dll.append(3)

print("Forward display:")
dll.display_forward()  # Output: 1 <-> 2 <-> 3 <-> None

print("Backward display:")
dll.display_backward()  # Output: 3 <-> 2 <-> 1 <-> None

# Prepend an element
dll.prepend(0)
print("After prepending 0:")
dll.display_forward()  # Output: 0 <-> 1 <-> 2 <-> 3 <-> None

# Delete an element
dll.delete(2)
print("After deleting 2:")
dll.display_forward()  # Output: 0 <-> 1 <-> 3 <-> None
```

## Common Interview Questions

1. **Implement a Palindrome Checker**: Use a doubly linked list to check if a given sequence is a palindrome.
2. **LRU Cache**: Implement a Least Recently Used (LRU) cache using a doubly linked list and a hash map.
3. **Flatten a Multilevel Doubly Linked List**: Given a doubly linked list where each node might have a child list, flatten it into a single level linked list.

## Exercise

1. Implement a method `insert_after(self, target_data, new_data)` that inserts a new node with `new_data` after the first occurrence of a node with `target_data`.
2. Write a method `reverse(self)` that reverses the doubly linked list in-place.
3. Implement a method `is_palindrome(self)` that checks if the doubly linked list is a palindrome.

## Summary

Today, we explored doubly linked lists, their implementation, and how they compare to singly linked lists. Doubly linked lists offer more flexibility in certain operations at the cost of additional memory usage. Understanding the trade-offs between different data structures is crucial for choosing the right tool for specific problems.

Tomorrow, we'll dive into more advanced linked list operations and tackle some common interview problems related to linked lists. Stay tuned!
