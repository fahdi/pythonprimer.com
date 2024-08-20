---
title: "Day 4: Introduction to Arrays"
weight: 4
menu:
  main:
    parent: "Algorithms"
    weight: 4
---

# Day 4: Introduction to Arrays

Welcome to Day 4 of our 60 Days of Coding Algorithm Challenge! Today, we'll explore one of the most fundamental data structures in computer science: arrays.

## What is an Array?

An array is a collection of elements, each identified by an index or key. Arrays are used to store multiple values in a single variable and are a crucial part of many algorithms and data structures.

## Properties of Arrays

1. **Fixed Size**: Arrays have a fixed size, which means you need to define the number of elements it can hold during its declaration.
2. **Homogeneous Elements**: All elements in an array are of the same data type.
3. **Indexed Access**: Each element in an array can be accessed using its index, starting from 0.

## Basic Operations

1. **Initialization**:
    ```python
    arr = [1, 2, 3, 4, 5]
    ```

2. **Accessing Elements**:
    ```python
    first_element = arr[0]
    ```

3. **Updating Elements**:
    ```python
    arr[1] = 10
    ```

4. **Traversing**:
    ```python
    for element in arr:
        print(element)
    ```

5. **Inserting Elements** (requires shifting elements):
    ```python
    arr.insert(2, 20)  # Insert 20 at index 2
    ```

6. **Deleting Elements** (requires shifting elements):
    ```python
    arr.pop(2)  # Remove element at index 2
    ```

## Example: Implementing Basic Array Operations

Let's implement a few basic array operations in Python:

```python
# Initialize an array
arr = [1, 2, 3, 4, 5]

# Access elements
print("First element:", arr[0])
print("Third element:", arr[2])

# Update an element
arr[1] = 10
print("Updated array:", arr)

# Traverse the array
for element in arr:
    print(element)

# Insert an element
arr.insert(2, 20)
print("Array after insertion:", arr)

# Delete an element
arr.pop(2)
print("Array after deletion:", arr)
```

## Exercise

1. Write a function to find the minimum and maximum elements in an array.
2. Implement a function to reverse an array.
3. Create a function to find the sum of all elements in an array.

## Summary

Arrays are a fundamental data structure that you'll use frequently in your coding journey. Understanding their properties and operations is crucial for solving more complex problems. Tomorrow, we'll dive deeper into more advanced array operations and their applications.

Stay tuned!
