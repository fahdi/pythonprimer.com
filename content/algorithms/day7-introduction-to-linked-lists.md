---
title: "Day 7: Introduction to Linked Lists"
weight: 7
menu:
  main:
    parent: "Algorithms"
    weight: 7
---

# Introduction to Linked Lists

Welcome to Day 7 of our 60 Days of Coding Algorithm Challenge! Today, we'll dive into the world of linked lists, a fundamental data structure in computer science.

## What is a Linked List?

A linked list is a linear data structure where elements are stored in nodes. Each node contains a data field and a reference (or link) to the next node in the sequence.

Unlike arrays, linked lists do not store elements in contiguous memory locations. Instead, the elements are linked using pointers.

## Basic Structure of a Linked List

A typical node in a linked list consists of two components:
1. **Data**: The value or payload of the node
2. **Next**: A reference to the next node in the sequence

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

## Types of Linked Lists

1. **Singly Linked List**: Each node points to the next node in the sequence.
2. **Doubly Linked List**: Each node has pointers to both the next and previous nodes.
3. **Circular Linked List**: The last node points back to the first node, forming a circle.

## Basic Operations on a Linked List

1. **Insertion**: Adding a new node to the list
2. **Deletion**: Removing a node from the list
3. **Traversal**: Visiting each node in the list
4. **Search**: Finding a node with a specific value

## Example: Simple Singly Linked List Implementation

Let's implement a basic singly linked list in Python:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Usage
my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.display()  # Output: 1 -> 2 -> 3 -> None
```

## Advantages of Linked Lists

1. **Dynamic Size**: Linked lists can grow or shrink in size during runtime.
2. **Efficient Insertion and Deletion**: Adding or removing elements at the beginning is O(1).
3. **Flexible Memory Allocation**: Nodes can be stored anywhere in memory.

## Disadvantages of Linked Lists

1. **No Random Access**: Accessing an element by index is O(n).
2. **Extra Memory**: Each node requires additional memory for the pointer.
3. **Not Cache-Friendly**: Nodes may be scattered in memory, reducing cache efficiency.

## Exercise

1. Implement a `prepend` method that adds a new node to the beginning of the linked list.
2. Write a `search` method that returns `True` if a given value exists in the linked list, and `False` otherwise.
3. Implement a `delete` method that removes the first occurrence of a given value from the linked list.

## Summary

Linked lists are versatile data structures that offer efficient insertion and deletion operations. Understanding linked lists is crucial for many advanced algorithms and data structures. In the coming days, we'll explore more complex operations and variations of linked lists.

Tomorrow, we'll dive deeper into singly linked lists and implement more advanced operations. Stay tuned!