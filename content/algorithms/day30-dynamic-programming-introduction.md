---
title: "Day 30: Introduction to Dynamic Programming"
weight: 30
menu:
  main:
    parent: "Algorithms"
    weight: 30
---

# Day 30: Introduction to Dynamic Programming

Welcome to Day 30 of our 60 Days of Coding Algorithm Challenge! Today, we'll dive into Dynamic Programming (DP), a powerful algorithmic technique used to solve complex problems by breaking them down into simpler subproblems.

## What is Dynamic Programming?

Dynamic Programming is a method for solving complex problems by breaking them down into simpler subproblems. It is applicable when the subproblems are not independent, i.e., when subproblems share subsubproblems. A dynamic programming algorithm solves each subsubproblem only once and then saves its answer in a table, thereby avoiding the work of recomputing the answer every time the subsubproblem is encountered.

## Key Characteristics of Dynamic Programming Problems

1. Optimal Substructure: An optimal solution to the problem contains optimal solutions to subproblems.
2. Overlapping Subproblems: The problem can be broken down into subproblems which are reused several times.

## Approaches to Dynamic Programming

1. Top-down (Memoization): We solve the bigger problem by recursively finding the solution to smaller subproblems. Whenever we solve a subproblem, we cache its result.

2. Bottom-up (Tabulation): We solve the subproblems first and use their solutions to build-on and arrive at solutions to bigger subproblems.

## Example: Fibonacci Sequence

Let's implement the Fibonacci sequence using both approaches:

### Top-down (Memoization)

```python
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

# Example usage
print(fibonacci_memo(100))  # Fast, even for large n
```

### Bottom-up (Tabulation)

```python
def fibonacci_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# Example usage
print(fibonacci_tab(100))  # Also fast for large n
```

## Classic DP Problem: Longest Common Subsequence (LCS)

The Longest Common Subsequence problem is finding the longest subsequence common to all sequences in a set of sequences. Let's implement it:

```python
def lcs(X, Y):
    m, n = len(X), len(Y)
    L = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    # Backtracking to find the LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs.append(X[i-1])
            i -= 1
            j -= 1
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs))

# Example usage
X = "ABCDGH"
Y = "AEDFHR"
print(f"LCS of {X} and {Y} is {lcs(X, Y)}")
```

## When to Use Dynamic Programming

1. Counting Problems: How many ways are there to do something?
2. Optimization Problems: What is the minimum or maximum of something?
3. Yes/No Problems: Can something be done or not?

## Advantages of Dynamic Programming

1. Efficiency: Solves complex problems efficiently by avoiding redundant calculations.
2. Optimization: Finds the optimal solution for problems with multiple possible solutions.
3. Versatility: Applicable to a wide range of problems in various fields.

## Disadvantages of Dynamic Programming

1. Memory Usage: Can require a lot of memory for storing subproblem solutions.
2. Complexity: Sometimes difficult to identify the correct subproblems and recurrence relation.

## Exercise

1. Implement the "Coin Change" problem using dynamic programming. Given a set of coin denominations and a target amount, find the minimum number of coins needed to make up that amount.

2. Solve the "Knapsack Problem" using dynamic programming. Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.

3. Implement the "Edit Distance" problem. Given two strings, find the minimum number of operations (insert, delete, replace) required to convert one string into the other.

## Summary

Today, we introduced Dynamic Programming, a powerful technique for solving complex optimization problems. We explored the key characteristics of DP problems, implemented solutions using both top-down and bottom-up approaches, and solved the classic Longest Common Subsequence problem.

Understanding Dynamic Programming is crucial for solving a wide range of algorithmic problems efficiently. As we progress through this challenge, you'll encounter more advanced DP problems and techniques.

Tomorrow, we'll dive into graph algorithms, starting with Depth-First Search (DFS) and its applications. Stay tuned!
