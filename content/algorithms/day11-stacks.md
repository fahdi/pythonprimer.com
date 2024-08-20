---
title: "Day 11: Introduction to Stacks"
weight: 11
menu:
  main:
    parent: "Algorithms"
    weight: 11
---

# Introduction to Stacks

Welcome to Day 11 of our 60 Days of Coding Algorithm Challenge! Today, we'll explore stacks, a fundamental data structure in computer science that follows the Last-In-First-Out (LIFO) principle.

## What is a Stack?

A stack is a linear data structure that follows a particular order in which operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out). Real-life examples include a stack of plates or a pile of books.

## Basic Operations of a Stack

1. **Push**: Adds an element to the top of the stack
2. **Pop**: Removes the top element from the stack
3. **Peek** or **Top**: Returns the top element of the stack without removing it
4. **isEmpty**: Returns true if the stack is empty, else false

## Implementing a Stack in Python

We can implement a stack using a Python list or create a custom class. Let's implement both:

### Using a Python List

```python
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)
```

### Using a Custom Node Class

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        popped = self.top.data
        self.top = self.top.next
        return popped

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.top.data

    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count
```

## Time Complexity

- Push operation: O(1)
- Pop operation: O(1)
- Peek operation: O(1)
- Search operation: O(n) in the worst case

## Applications of Stacks

1. **Function Call Stack**: Used by compilers to manage function calls
2. **Expression Evaluation**: Used to evaluate prefix, infix, and postfix expressions
3. **Backtracking Algorithms**: Used in backtracking problems like finding maze paths
4. **Undo Mechanism**: Implementing undo functionality in text editors
5. **Balanced Parentheses**: Checking for balanced parentheses in expressions

## Example: Balanced Parentheses

Let's implement a function to check if parentheses in an expression are balanced:

```python
def is_balanced(expression):
    stack = []
    opening = "({["
    closing = ")}]"
    pairs = {")": "(", "}": "{", "]": "["}
    
    for char in expression:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack.pop() != pairs[char]:
                return False
    
    return len(stack) == 0

# Test the function
print(is_balanced("({[]})"))  # True
print(is_balanced("([)]"))    # False
print(is_balanced("(("))      # False
```

## Exercise

1. Implement a function to reverse a string using a stack.
2. Create a `MinStack` class that supports push, pop, top, and retrieving the minimum element in constant time.
3. Implement the `Queue` data structure using two stacks.

## Summary

Today, we explored the stack data structure, its implementation, and a practical application. Stacks are crucial in many algorithms and real-world applications due to their LIFO nature. Understanding stacks will help you solve various problems efficiently and is essential for topics like depth-first search and expression parsing.

Tomorrow, we'll dive into queues, another fundamental data structure that follows the First-In-First-Out (FIFO) principle. Stay tuned!
