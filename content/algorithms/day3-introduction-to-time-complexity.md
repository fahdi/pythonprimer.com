---
title: "Day 3: Introduction to Time Complexity"
weight: 3
menu:
  main:
    parent: "Algorithms"
    weight: 3
---

# Day 3: Introduction to Time Complexity

Welcome to Day 3 of our 60 Days of Coding Algorithm Challenge! Today, we'll explore the concept of time complexity, a fundamental aspect of algorithm analysis that is crucial for writing efficient code.

## What is Time Complexity?

Time complexity is a measure of the amount of time an algorithm takes to complete as a function of the size of the input. It provides insight into how the runtime of an algorithm grows as the input size increases, helping us evaluate its efficiency and scalability.

### Key Points:
- **Input Size**: Often denoted as \( n \), it represents the number of elements or data points the algorithm processes.
- **Growth Rate**: Describes how the algorithm's runtime increases relative to the input size.

## Why is Time Complexity Important?

1. **Efficiency**: Allows us to compare different algorithms and choose the most efficient one for a given problem, especially as input sizes grow.
2. **Scalability**: Helps predict the behavior of an algorithm when handling large datasets, ensuring it can scale effectively.
3. **Optimization**: Guides us in identifying bottlenecks and optimizing our code for better performance, which is essential in resource-constrained environments.

## Big O Notation

Big O notation is the standard way to express time complexity. It describes the upper bound of the algorithm's growth rate, focusing on the worst-case scenario to provide a guarantee on the algorithm's performance.

### Common Big O Notations:

1. **O(1) - Constant Time**: The runtime is constant, regardless of input size.
2. **O(log n) - Logarithmic Time**: The runtime grows logarithmically, making it very efficient for large inputs.
3. **O(n) - Linear Time**: The runtime grows linearly with the input size.
4. **O(n log n) - Linearithmic Time**: A common complexity for efficient sorting algorithms.
5. **O(n^2) - Quadratic Time**: The runtime grows quadratically, making the algorithm inefficient for large inputs.
6. **O(2^n) - Exponential Time**: The runtime doubles with each additional element, leading to very poor scalability.

## Examples of Time Complexities

### 1. O(1) - Constant Time

```python
def get_first_element(arr):
    return arr[0]
```

- **Explanation**: This function retrieves the first element of the array, which requires a single operation regardless of the array's size.

### 2. O(n) - Linear Time

```python
def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val
```

- **Explanation**: This function iterates through the array to find the maximum value. The number of operations grows linearly with the input size.

### 3. O(n^2) - Quadratic Time

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

- **Explanation**: Bubble Sort involves nested loops, where each element is compared multiple times. The number of operations grows quadratically with the input size.

## How to Analyze Time Complexity

Analyzing time complexity involves understanding the key operations that drive the algorithm's runtime. Here's a step-by-step approach:

1. **Identify Basic Operations**: Determine the most significant operations that influence the runtime, such as comparisons or iterations.
2. **Count Executions**: Calculate how many times these operations are performed based on the input size.
3. **Express in Terms of Input Size**: Represent the total number of operations as a function of the input size \( n \).
4. **Simplify Using Big O**: Focus on the highest order term (the most significant growth rate) and ignore constants, as Big O notation captures the overall trend.

## Exercise

Let's analyze the time complexity of the following function:

```python
def find_pair_with_sum(arr, target_sum):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                return (arr[i], arr[j])
    return None
```

### Questions to Consider:
1. **What are the basic operations?**: Identify the key operations within the loops.
2. **How many times are they executed in relation to the input size?**: Determine the number of iterations for each loop.
3. **What is the Big O notation for this function?**: Combine the results to express the overall time complexity.

### Hints:
- **Nested Loops**: The inner loop runs multiple times for each iteration of the outer loop, leading to a potentially higher time complexity.
- **Total Operations**: Consider the sum of operations across all iterations to determine the overall time complexity.

## Summary

Understanding time complexity is essential for evaluating and comparing algorithms. It provides a theoretical framework for predicting how an algorithm will perform, especially with large inputs. As we continue, we'll see how different data structures and algorithmic techniques can help us optimize for better time complexity.

Tomorrow, we'll begin our exploration of fundamental data structures, starting with arrays. We'll learn about their properties, basic operations, and how they interact with time complexity.

Stay tuned!
