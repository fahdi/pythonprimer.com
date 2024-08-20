---
title: "Day 35: Longest Increasing Subsequence"
weight: 35
menu:
  main:
    parent: "Algorithms"
    weight: 35
---

# Longest Increasing Subsequence (LIS)

Welcome to Day 35 of our 60 Days of Coding Algorithm Challenge! Today, we'll explore the Longest Increasing Subsequence (LIS) problem, a classic dynamic programming problem with applications in various fields.

## What is the Longest Increasing Subsequence?

The Longest Increasing Subsequence problem is to find a subsequence of a given sequence in which the subsequence's elements are in sorted order, lowest to highest, and in which the subsequence is as long as possible. This subsequence is not necessarily contiguous or unique.

For example, the LIS of [10, 22, 9, 33, 21, 50, 41, 60, 80] is [10, 22, 33, 50, 60, 80] of length 6.

## Naive Recursive Approach

Let's start with a naive recursive implementation:

```python
def lis_naive(arr):
    n = len(arr)
    
    def lis_helper(i, prev):
        if i == n:
            return 0
        
        include = 0
        if arr[i] > prev:
            include = 1 + lis_helper(i + 1, arr[i])
        
        exclude = lis_helper(i + 1, prev)
        
        return max(include, exclude)
    
    return lis_helper(0, float('-inf'))

# Example usage
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(f"Length of LIS is {lis_naive(arr)}")
```

This approach has a time complexity of O(2^n), making it inefficient for larger inputs.

## Dynamic Programming Approach

We can significantly improve the efficiency using Dynamic Programming.

### Top-Down Approach (Memoization)

```python
def lis_memo(arr):
    n = len(arr)
    memo = {}
    
    def lis_helper(i, prev_index):
        if i == n:
            return 0
        
        if (i, prev_index) in memo:
            return memo[(i, prev_index)]
        
        include = 0
        if prev_index == -1 or arr[i] > arr[prev_index]:
            include = 1 + lis_helper(i + 1, i)
        
        exclude = lis_helper(i + 1, prev_index)
        
        memo[(i, prev_index)] = max(include, exclude)
        return memo[(i, prev_index)]
    
    return lis_helper(0, -1)

# Example usage
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(f"Length of LIS is {lis_memo(arr)}")
```

### Bottom-Up Approach (Tabulation)

```python
def lis_tab(arr):
    n = len(arr)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Example usage
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(f"Length of LIS is {lis_tab(arr)}")
```

The Dynamic Programming approaches have a time complexity of O(n^2) and a space complexity of O(n).

## Optimized Solution using Binary Search

We can further optimize the solution to achieve O(n log n) time complexity:

```python
def lis_optimized(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    tail = [0] * n
    length = 1
    tail[0] = arr[0]
    
    for i in range(1, n):
        if arr[i] < tail[0]:
            tail[0] = arr[i]
        elif arr[i] > tail[length-1]:
            tail[length] = arr[i]
            length += 1
        else:
            tail[binary_search(tail, 0, length-1, arr[i])] = arr[i]
    
    return length

def binary_search(tail, low, high, key):
    while high > low:
        mid = (low + high) // 2
        if tail[mid] >= key:
            high = mid
        else:
            low = mid + 1
    return high

# Example usage
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(f"Length of LIS is {lis_optimized(arr)}")
```

This optimized version has a time complexity of O(n log n) and a space complexity of O(n).

## Printing the Longest Increasing Subsequence

We can modify our solution to also print the LIS:

```python
def lis_with_sequence(arr):
    n = len(arr)
    dp = [1] * n
    prev = [-1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
    
    # Find the index of the maximum value in dp
    max_length = max(dp)
    max_index = dp.index(max_length)
    
    # Reconstruct the sequence
    sequence = []
    while max_index != -1:
        sequence.append(arr[max_index])
        max_index = prev[max_index]
    
    return max_length, sequence[::-1]

# Example usage
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
length, sequence = lis_with_sequence(arr)
print(f"Length of LIS is {length}")
print(f"LIS is {sequence}")
```

## Applications of LIS

1. Analyzing sequence data in bioinformatics
2. Predicting stock market trends
3. Text compression algorithms
4. Optimization in computer graphics (e.g., optimal triangulation)
5. Finding the longest chain of pairs in array of pairs

## Exercise

1. Implement a function to find the Longest Decreasing Subsequence.

2. Modify the LIS algorithm to find the Longest Bitonic Subsequence (a subsequence that first increases, then decreases).

3. Implement a function to find the Longest Common Increasing Subsequence of two arrays.

## Summary

Today, we explored the Longest Increasing Subsequence problem, a classic example of dynamic programming. We implemented various approaches, from naive recursion to optimized dynamic programming solutions, and even a version that provides the actual subsequence.

Understanding the LIS problem and its solutions provides valuable insights into dynamic programming techniques and their applications in sequence analysis and optimization problems.

Tomorrow, we'll dive into another fundamental algorithm: Dijkstra's Shortest Path Algorithm. Stay tuned!
