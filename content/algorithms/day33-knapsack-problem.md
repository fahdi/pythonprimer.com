---
title: "Day 33: The Knapsack Problem"
weight: 33
menu:
  main:
    parent: "Algorithms"
    weight: 33
---

# The Knapsack Problem

Welcome to Day 33 of our 60 Days of Coding Algorithm Challenge! Today, we'll explore the Knapsack Problem, a fundamental problem in combinatorial optimization and a classic example of dynamic programming.

## What is the Knapsack Problem?

The Knapsack Problem is an optimization problem where we need to select items from a set, each with a weight and a value, to maximize the total value while keeping the total weight within a given limit.

There are two main variants of the Knapsack Problem:
1. 0/1 Knapsack Problem: Each item can be included only once or not at all.
2. Unbounded Knapsack Problem: Each item can be included any number of times.

We'll focus on the 0/1 Knapsack Problem in this lesson.

## Problem Statement

Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.

## Naive Recursive Approach

Let's start with a naive recursive implementation:

```python
def knapsack_naive(W, wt, val, n):
    # Base Case
    if n == 0 or W == 0:
        return 0

    # If weight of the nth item is more than Knapsack capacity W,
    # then this item cannot be included in the optimal solution
    if wt[n-1] > W:
        return knapsack_naive(W, wt, val, n-1)

    # Return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(
            val[n-1] + knapsack_naive(W-wt[n-1], wt, val, n-1),
            knapsack_naive(W, wt, val, n-1)
        )

# Example usage
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(f"Maximum value: {knapsack_naive(W, wt, val, n)}")
```

This approach has a time complexity of O(2^n), making it inefficient for larger inputs.

## Dynamic Programming Approach

We can significantly improve the efficiency using Dynamic Programming.

### Top-Down Approach (Memoization)

```python
def knapsack_memo(W, wt, val, n, memo=None):
    if memo is None:
        memo = {}

    # Base Case
    if n == 0 or W == 0:
        return 0

    # Check if already computed
    if (W, n) in memo:
        return memo[(W, n)]

    # If weight of the nth item is more than Knapsack capacity W,
    # then this item cannot be included in the optimal solution
    if wt[n-1] > W:
        result = knapsack_memo(W, wt, val, n-1, memo)
    else:
        # Return the maximum of two cases:
        # (1) nth item included
        # (2) not included
        result = max(
            val[n-1] + knapsack_memo(W-wt[n-1], wt, val, n-1, memo),
            knapsack_memo(W, wt, val, n-1, memo)
        )

    # Save the result in memo
    memo[(W, n)] = result
    return result

# Example usage
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(f"Maximum value: {knapsack_memo(W, wt, val, n)}")
```

### Bottom-Up Approach (Tabulation)

```python
def knapsack_tab(W, wt, val, n):
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[n][W]

# Example usage
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(f"Maximum value: {knapsack_tab(W, wt, val, n)}")
```

Both Dynamic Programming approaches have a time complexity of O(nW) and a space complexity of O(nW).

## Space-Optimized Solution

We can optimize the space complexity to O(W) by only keeping track of the current and previous rows of the DP table:

```python
def knapsack_space_optimized(W, wt, val, n):
    prev = [0] * (W + 1)
    curr = [0] * (W + 1)

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i-1] <= w:
                curr[w] = max(val[i-1] + prev[w-wt[i-1]], prev[w])
            else:
                curr[w] = prev[w]
        prev, curr = curr, prev

    return prev[W]

# Example usage
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(f"Maximum value: {knapsack_space_optimized(W, wt, val, n)}")
```

This optimized version has a space complexity of O(W) while maintaining the time complexity of O(nW).

## Printing the Selected Items

We can modify our solution to also print the items that were selected:

```python
def knapsack_with_items(W, wt, val, n):
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    # Find the selected items
    res = K[n][W]
    w = W
    selected = []
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == K[i-1][w]:
            continue
        else:
            selected.append(i-1)
            res -= val[i-1]
            w -= wt[i-1]

    return K[n][W], selected[::-1]

# Example usage
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
max_value, selected_items = knapsack_with_items(W, wt, val, n)
print(f"Maximum value: {max_value}")
print(f"Selected items (indices): {selected_items}")
```

## Applications of the Knapsack Problem

1. Resource Allocation in Finance
2. Cargo Loading
3. Cutting Stock Problems
4. Cryptography (in creating pseudorandom number generators)
5. Combinatorics and Computational Complexity Theory

## Exercise

1. Implement the Unbounded Knapsack Problem, where you can use items any number of times.

2. Solve the Subset Sum Problem using the Knapsack algorithm. Given a set of integers and a target sum, determine if there's a subset that adds up to the target.

3. Implement a function to solve the Knapsack Problem where items have a volume constraint in addition to weight.

## Summary

Today, we explored the Knapsack Problem, a fundamental problem in combinatorial optimization and a classic example of dynamic programming. We implemented various approaches, from naive recursion to optimized dynamic programming solutions, and even a space-optimized version.

Understanding the Knapsack Problem and its solutions provides valuable insights into dynamic programming techniques and their applications in optimization problems.

Tomorrow, we'll dive into graph algorithms, starting with Breadth-First Search (BFS). Stay tuned!
