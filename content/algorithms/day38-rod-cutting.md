---
title: "Day 38 - Extra Work: Rod Cutting Problem"
weight: 38.5
menu:
  main:
    parent: "Algorithms"
    weight: 38.5
---

# Rod Cutting Problem

Welcome to an extra lesson for Day 38 of our 60 Days of Coding Algorithm Challenge! In this additional content, we'll explore the Rod Cutting Problem, another classic example of dynamic programming.

## What is the Rod Cutting Problem?

The Rod Cutting Problem is an optimization problem where we need to cut a rod of length n into smaller pieces to maximize the total value. Each piece has a value associated with its length, and we need to determine the most profitable way to cut the rod.

## Problem Statement

Given a rod of length n inches and a table of prices pi for i = 1, 2, ..., n, determine the maximum revenue rn obtainable by cutting up the rod and selling the pieces.

## Naive Recursive Approach

Let's start with a naive recursive implementation:

```python
def cut_rod_recursive(prices, n):
    if n <= 0:
        return 0
    max_value = float('-inf')
    for i in range(n):
        max_value = max(max_value, prices[i] + cut_rod_recursive(prices, n - i - 1))
    return max_value

# Example usage
prices = [1, 5, 8, 9, 10, 17, 17, 20]
rod_length = 8
print(f"Maximum value: {cut_rod_recursive(prices, rod_length)}")
```

This approach has a time complexity of O(2^n), making it inefficient for larger inputs.

## Dynamic Programming Approach

We can significantly improve the efficiency using Dynamic Programming.

### Top-Down Approach (Memoization)

```python
def cut_rod_memo(prices, n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    max_value = float('-inf')
    for i in range(n):
        max_value = max(max_value, prices[i] + cut_rod_memo(prices, n - i - 1, memo))
    memo[n] = max_value
    return max_value

# Example usage
prices = [1, 5, 8, 9, 10, 17, 17, 20]
rod_length = 8
print(f"Maximum value: {cut_rod_memo(prices, rod_length)}")
```

### Bottom-Up Approach (Tabulation)

```python
def cut_rod_tab(prices, n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        max_value = float('-inf')
        for j in range(i):
            max_value = max(max_value, prices[j] + dp[i - j - 1])
        dp[i] = max_value
    return dp[n]

# Example usage
prices = [1, 5, 8, 9, 10, 17, 17, 20]
rod_length = 8
print(f"Maximum value: {cut_rod_tab(prices, rod_length)}")
```

Both Dynamic Programming approaches have a time complexity of O(n^2) and a space complexity of O(n).

## Printing the Optimal Cuts

We can modify our solution to also print the optimal way to cut the rod:

```python
def cut_rod_with_solution(prices, n):
    dp = [0] * (n + 1)
    cuts = [0] * (n + 1)
    
    for i in range(1, n + 1):
        max_value = float('-inf')
        for j in range(i):
            if prices[j] + dp[i - j - 1] > max_value:
                max_value = prices[j] + dp[i - j - 1]
                cuts[i] = j + 1
        dp[i] = max_value
    
    # Reconstruct the solution
    solution = []
    while n > 0:
        solution.append(cuts[n])
        n -= cuts[n]
    
    return dp[-1], solution

# Example usage
prices = [1, 5, 8, 9, 10, 17, 17, 20]
rod_length = 8
max_value, cuts = cut_rod_with_solution(prices, rod_length)
print(f"Maximum value: {max_value}")
print(f"Optimal cuts: {cuts}")
```

## Applications of the Rod Cutting Problem

1. Resource allocation in economics
2. Cutting stock problems in manufacturing
3. Optimizing revenue in pricing strategies
4. Data compression algorithms

## Exercise

1. Modify the algorithm to handle the case where there's a cost associated with each cut. How does this change the optimal solution?

2. Implement a version of the Rod Cutting Problem where you have a limited number of cuts you can make. How does this constraint affect the solution?

3. Extend the problem to two dimensions, where you need to cut a rectangular sheet to maximize value. This is known as the "2D Cutting Stock Problem".

## Summary

Today, we explored the Rod Cutting Problem, another classic example of dynamic programming. We implemented various approaches, from naive recursion to optimized dynamic programming solutions, and even a version that provides the optimal cutting strategy.

Understanding the Rod Cutting Problem and its solutions provides valuable insights into dynamic programming techniques and their applications in optimization problems, particularly those involving resource allocation and maximizing value.

This problem serves as an excellent complement to our main lesson on the Floyd-Warshall algorithm, further solidifying your understanding of dynamic programming concepts.
