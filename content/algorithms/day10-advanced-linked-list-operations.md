---
title: "Day 10: Advanced Linked List Operations and Problems"
weight: 10
menu:
  main:
    parent: "Algorithms"
    weight: 10
---

# Advanced Linked List Operations and Problems

Welcome to Day 10 of our 60 Days of Coding Algorithm Challenge! Today, we'll explore advanced operations and tackle common problems related to linked lists. These topics are frequently encountered in coding interviews and real-world applications.

## 1. Reversing a Linked List

Reversing a linked list is a fundamental operation that's often asked in interviews. Here's an implementation for a singly linked list:

```python
def reverse_linked_list(self):
    prev = None
    current = self.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    self.head = prev
```

Time Complexity: O(n), where n is the number of nodes in the list.

## 2. Detecting a Cycle in a Linked List

The Floyd's Cycle-Finding Algorithm, also known as the "tortoise and hare" algorithm, is an efficient method to detect cycles:

```python
def has_cycle(self):
    if not self.head:
        return False
    
    slow = self.head
    fast = self.head.next
    
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    
    return True
```

Time Complexity: O(n), Space Complexity: O(1)

## 3. Finding the Middle Node

Finding the middle node is another common problem. We can solve it efficiently using two pointers:

```python
def find_middle(self):
    if not self.head:
        return None
    
    slow = fast = self.head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow
```

Time Complexity: O(n), Space Complexity: O(1)

## 4. Merging Two Sorted Linked Lists

This operation is useful in many algorithms, including merge sort for linked lists:

```python
def merge_sorted_lists(list1, list2):
    dummy = Node(0)
    current = dummy
    
    while list1 and list2:
        if list1.data <= list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    if list1:
        current.next = list1
    if list2:
        current.next = list2
    
    return dummy.next
```

Time Complexity: O(n + m), where n and m are the lengths of the two lists.

## 5. Removing Nth Node from End

This problem demonstrates the use of two pointers with a specific gap:

```python
def remove_nth_from_end(self, n):
    dummy = Node(0)
    dummy.next = self.head
    first = second = dummy
    
    # Advance first pointer by n+1 steps
    for i in range(n + 1):
        if not first:
            return self.head
        first = first.next
    
    # Move both pointers until first reaches the end
    while first:
        first = first.next
        second = second.next
    
    # Remove the target node
    second.next = second.next.next
    
    return dummy.next
```

Time Complexity: O(L), where L is the length of the list.

## 6. Flattening a Multilevel Doubly Linked List

This problem involves working with a more complex linked list structure:

```python
class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def flatten(head):
    if not head:
        return head
    
    current = head
    while current:
        if current.child:
            next_node = current.next
            child = flatten(current.child)
            current.next = child
            child.prev = current
            current.child = None
            
            while current.next:
                current = current.next
            
            current.next = next_node
            if next_node:
                next_node.prev = current
        
        current = current.next
    
    return head
```

Time Complexity: O(N), where N is the total number of nodes in the multilevel structure.

## Exercise

1. Implement a function to detect and remove a loop in a linked list.
2. Write a method to add two numbers represented by linked lists. The digits are stored in reverse order, and each node contains a single digit.
3. Implement a function to determine if a linked list is a palindrome.

## Summary

Today, we explored advanced linked list operations and problems that are commonly encountered in coding interviews and real-world scenarios. These problems demonstrate various techniques, including two-pointer approaches, dummy nodes, and recursive solutions. Understanding these concepts will significantly improve your problem-solving skills with linked lists.

Tomorrow, we'll shift our focus to a new data structure: stacks. We'll explore their implementation and applications in solving various problems. Stay tuned!