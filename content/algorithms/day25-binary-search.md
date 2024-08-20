---
title: "Day 25: Binary Search and Its Variations"
weight: 25
menu:
  main:
    parent: "Algorithms"
    weight: 25
---

# Binary Search and Its Variations

Welcome to Day 25 of our 60 Days of Coding Algorithm Challenge! Today, we'll explore Binary Search, a fundamental search algorithm, and its various variations. Binary Search is known for its efficiency in searching sorted arrays and forms the basis for many other algorithms.

## Introduction to Binary Search

Binary Search is a divide and conquer algorithm that finds the position of a target value within a sorted array. It compares the target value to the middle element of the array; if they are unequal, the half in which the target cannot lie is eliminated and the search continues on the remaining half until the target value is found.

## Basic Binary Search

Here's an implementation of the basic binary search algorithm:

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Target not found

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
result = binary_search(arr, target)
print(f"Target {target} found at index: {result}")
```

Time Complexity: O(log n)
Space Complexity: O(1)

## Variations of Binary Search

### 1. Recursive Binary Search

A recursive implementation of binary search:

```python
def recursive_binary_search(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, right)
    else:
        return recursive_binary_search(arr, target, left, mid - 1)

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11
result = recursive_binary_search(arr, target, 0, len(arr) - 1)
print(f"Target {target} found at index: {result}")
```

### 2. Finding the First Occurrence

Modified binary search to find the first occurrence of a target value:

```python
def first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching in the left half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

# Example usage
arr = [1, 2, 2, 2, 3, 4, 4, 5]
target = 2
result = first_occurrence(arr, target)
print(f"First occurrence of {target} found at index: {result}")
```

### 3. Finding the Last Occurrence

Modified binary search to find the last occurrence of a target value:

```python
def last_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching in the right half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

# Example usage
arr = [1, 2, 2, 2, 3, 4, 4, 5]
target = 4
result = last_occurrence(arr, target)
print(f"Last occurrence of {target} found at index: {result}")
```

### 4. Finding the Floor and Ceiling

Binary search variations to find the floor (largest element smaller than or equal to target) and ceiling (smallest element larger than or equal to target):

```python
def floor(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
            result = arr[mid]
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def ceiling(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            result = arr[mid]
            right = mid - 1
    
    return result

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 6
floor_result = floor(arr, target)
ceiling_result = ceiling(arr, target)
print(f"Floor of {target}: {floor_result}")
print(f"Ceiling of {target}: {ceiling_result}")
```

### 5. Search in Rotated Sorted Array

A variation of binary search to find an element in a rotated sorted array:

```python
def search_rotated(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        
        # Check if left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1  # Target not found

# Example usage
arr = [4, 5, 6, 7, 0, 1, 2]
target = 0
result = search_rotated(arr, target)
print(f"Target {target} found at index: {result}")
```

## Applications of Binary Search

1. **Database Systems**: For efficient searching in indexed databases.
2. **Version Control Systems**: For finding when a bug was introduced (git bisect).
3. **Machine Learning**: In algorithms like decision trees and gradient descent.
4. **Computer Graphics**: In ray tracing and texture mapping.
5. **Optimization Problems**: For finding minimum or maximum values in unimodal functions.

## Exercise

1. Implement a binary search algorithm to find the square root of a number (up to a given precision).
2. Create a function that uses binary search to find the peak element in a bitonic array (an array that first increases, then decreases).
3. Implement a binary search algorithm to find the minimum element in a sorted and rotated array.

## Summary

Today, we explored Binary Search and its various applications. We implemented the basic binary search algorithm and several variations, including recursive binary search, finding first and last occurrences, floor and ceiling values, and searching in rotated sorted arrays.

Binary Search is a powerful technique that forms the basis for many efficient algorithms. Its logarithmic time complexity makes it invaluable for searching large datasets. As we progress through this challenge, you'll find binary search being used as a building block for more complex algorithms and problem-solving techniques.

Tomorrow, we'll dive into the Quicksort algorithm, one of the most efficient sorting algorithms. Stay tuned!

