---
title: "Day 8: Singly Linked Lists - Implementation and Basic Operations"
weight: 8
menu:
  main:
    parent: "Algorithms"
    weight: 8
---

# Singly Linked Lists - Implementation and Basic Operations

Welcome to Day 8 of our 60 Days of Coding Algorithm Challenge! Today, we'll dive deeper into singly linked lists, implementing a more comprehensive version and exploring various operations.

## Singly Linked List Structure

A singly linked list consists of nodes where each node contains data and a pointer to the next node. The last node points to None, indicating the end of the list.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

## Implementing a Singly Linked List

Let's implement a singly linked list with several basic operations:

```python
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.is_empty():
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next:
            current.next = current.next.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))
```

## Basic Operations Explained

1. **is_empty()**: Checks if the list is empty.
2. **append(data)**: Adds a new node with the given data to the end of the list.
3. **prepend(data)**: Adds a new node with the given data to the beginning of the list.
4. **delete(data)**: Removes the first occurrence of a node with the given data.
5. **search(data)**: Searches for a node with the given data and returns True if found.
6. **display()**: Prints all elements in the list.

## Time Complexity Analysis

- **Append**: O(n) - We need to traverse to the end of the list.
- **Prepend**: O(1) - We simply add to the head.
- **Delete**: O(n) - In the worst case, we need to traverse the entire list.
- **Search**: O(n) - We may need to traverse the entire list to find an element.

## Example Usage

Let's see how to use our SinglyLinkedList class:

```python
# Create a new linked list
my_list = SinglyLinkedList()

# Append elements
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.display()  # Output: 1 -> 2 -> 3

# Prepend an element
my_list.prepend(0)
my_list.display()  # Output: 0 -> 1 -> 2 -> 3

# Search for elements
print(my_list.search(2))  # Output: True
print(my_list.search(4))  # Output: False

# Delete an element
my_list.delete(2)
my_list.display()  # Output: 0 -> 1 -> 3
```

## Common Interview Questions

1. **Reverse a Linked List**: Can you implement a method to reverse the linked list in-place?
2. **Detect a Cycle**: How would you detect if a linked list has a cycle?
3. **Find the Middle Node**: Can you find the middle node of the linked list in one pass?

## Exercise

1. Implement a method `insert_after(self, target_data, new_data)` that inserts a new node with `new_data` after the first occurrence of a node with `target_data`.
2. Write a method `length(self)` that returns the number of nodes in the linked list.
3. Implement a method `remove_duplicates(self)` that removes all duplicate nodes from the linked list.

## Summary

Today, we've implemented a more comprehensive singly linked list and explored its basic operations. Understanding these operations and their time complexities is crucial for using linked lists effectively in various algorithms.

Tomorrow, we'll dive into doubly linked lists and compare them with singly linked lists. We'll also explore some more advanced linked list problems. Stay tuned!
