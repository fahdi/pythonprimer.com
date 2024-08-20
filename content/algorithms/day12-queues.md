---
title: "Day 12: Introduction to Queues"
weight: 12
menu:
  main:
    parent: "Algorithms"
    weight: 12
---

# Introduction to Queues

Welcome to Day 12 of our 60 Days of Coding Algorithm Challenge! Today, we'll explore queues, another fundamental data structure that follows the First-In-First-Out (FIFO) principle.

## What is a Queue?

A queue is a linear data structure that follows a particular order in which operations are performed. The order is First In First Out (FIFO). A good example of a queue is any queue of consumers for a resource where the consumer that came first is served first.

## Basic Operations of a Queue

1. **Enqueue**: Adds an element to the rear of the queue
2. **Dequeue**: Removes the element from the front of the queue
3. **Front**: Get the front element from the queue without removing it
4. **Rear**: Get the last element from the queue without removing it
5. **isEmpty**: Check if the queue is empty

## Implementing a Queue in Python

We can implement a queue using a Python list or create a custom class. Let's implement both:

### Using a Python List

```python
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)
```

### Using a Custom Node Class

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        dequeued = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued

    def get_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.data

    def get_rear(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.rear.data

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count
```

## Time Complexity

- Enqueue operation: O(1)
- Dequeue operation: O(1) for linked list implementation, O(n) for array implementation
- Front operation: O(1)
- Rear operation: O(1)

## Applications of Queues

1. **CPU Scheduling**: Manages processes waiting to be executed
2. **Breadth-First Search**: Used in graph algorithms
3. **Handling of requests on a single shared resource**: Printer, CPU task scheduling
4. **Buffering**: In streaming media, routers, etc.
5. **Asynchronous data transfer**: IO Buffers, pipes, file IO, etc.

## Example: Level Order Traversal of a Binary Tree

Let's implement a function to perform level order traversal of a binary tree using a queue:

```python
from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def level_order_traversal(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.value)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result

# Test the function
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(level_order_traversal(root))  # Output: [[1], [2, 3], [4, 5]]
```

## Exercise

1. Implement a circular queue using an array.
2. Create a function to reverse the first K elements of a queue.
3. Implement a stack using two queues.

## Summary

Today, we explored the queue data structure, its implementation, and a practical application in tree traversal. Queues are essential in many algorithms and real-world applications due to their FIFO nature. Understanding queues will help you solve various problems efficiently, especially in scenarios involving ordered processing or breadth-first algorithms.

Tomorrow, we'll begin our exploration of trees, starting with an introduction to tree data structures and their properties. Stay tuned!
