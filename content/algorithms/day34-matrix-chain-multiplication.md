---
title: "Day 34: Matrix Chain Multiplication"
weight: 34
menu:
  main:
    parent: "Algorithms"
    weight: 34
---

# Matrix Chain Multiplication

Welcome to Day 34 of our 60 Days of Coding Algorithm Challenge! Today, we'll explore Matrix Chain Multiplication, a classic optimization problem that demonstrates the power of dynamic programming.

## What is Matrix Chain Multiplication?

Matrix Chain Multiplication is an optimization problem that seeks to find the most efficient way to multiply a chain of matrices. The problem is not to actually perform the multiplications, but rather to decide the order in which the matrices should be multiplied.

## Problem Statement

Given a sequence of matrices, find the most efficient way to multiply these matrices together. The problem is not actually to perform the multiplications, but merely to decide in which order to perform the multiplications.

## Why is this Important?

The order in which we multiply matrices can significantly affect the total number of operations needed. For example, if we have three matrices A, B, and C with dimensions 10x30, 30x5, and 5x60 respectively:

- (AB)C = (10x30x5) + (10x5x60) = 1500 + 3000 = 4500 operations
- A(BC) = (30x5x60) + (10x30x60) = 9000 + 18000 = 27000 operations

Choosing the right order (AB)C saves us 22,500 operations!

## Naive Recursive Approach

Let's start with a naive recursive implementation:

```python
def matrix_chain_order_naive(p, i, j):
    if i == j:
        return 0

    min_cost = float('inf')

    for k in range(i, j):
        cost = (matrix_chain_order_naive(p, i, k) +
                matrix_chain_order_naive(p, k + 1, j) +
                p[i-1] * p[k] * p[j])

        if cost < min_cost:
            min_cost = cost

    return min_cost

# Example usage
p = [10, 30, 5, 60]
n = len(p)
print(f"Minimum number of multiplications is {matrix_chain_order_naive(p, 1, n-1)}")
```

This approach has a time complexity of O(2^n), making it inefficient for larger inputs.

## Dynamic Programming Approach

We can significantly improve the efficiency using Dynamic Programming.

### Top-Down Approach (Memoization)

```python
def matrix_chain_order_memo(p):
    n = len(p)
    m = [[0 for _ in range(n)] for _ in range(n)]
    
    def matrix_chain_helper(i, j):
        if i == j:
            return 0
        if m[i][j] != 0:
            return m[i][j]
        
        m[i][j] = float('inf')
        for k in range(i, j):
            q = (matrix_chain_helper(i, k) +
                 matrix_chain_helper(k + 1, j) +
                 p[i-1] * p[k] * p[j])
            if q < m[i][j]:
                m[i][j] = q
        return m[i][j]
    
    return matrix_chain_helper(1, n-1)

# Example usage
p = [10, 30, 5, 60]
print(f"Minimum number of multiplications is {matrix_chain_order_memo(p)}")
```

### Bottom-Up Approach (Tabulation)

```python
def matrix_chain_order_tab(p):
    n = len(p)
    m = [[0 for _ in range(n)] for _ in range(n)]
    
    for L in range(2, n):
        for i in range(1, n - L + 1):
            j = i + L - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
    
    return m[1][n-1]

# Example usage
p = [10, 30, 5, 60]
print(f"Minimum number of multiplications is {matrix_chain_order_tab(p)}")
```

Both Dynamic Programming approaches have a time complexity of O(n^3) and a space complexity of O(n^2).

## Printing the Optimal Parenthesization

We can modify our solution to also print the optimal way to parenthesize the product:

```python
def matrix_chain_order_with_parenthesization(p):
    n = len(p)
    m = [[0 for _ in range(n)] for _ in range(n)]
    s = [[0 for _ in range(n)] for _ in range(n)]
    
    for L in range(2, n):
        for i in range(1, n - L + 1):
            j = i + L - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    
    def print_optimal_parens(s, i, j):
        if i == j:
            print(f"A{i}", end="")
        else:
            print("(", end="")
            print_optimal_parens(s, i, s[i][j])
            print_optimal_parens(s, s[i][j] + 1, j)
            print(")", end="")
    
    print("Optimal Parenthesization: ", end="")
    print_optimal_parens(s, 1, n-1)
    print()
    return m[1][n-1]

# Example usage
p = [10, 30, 5, 60]
print(f"Minimum number of multiplications is {matrix_chain_order_with_parenthesization(p)}")
```

## Applications of Matrix Chain Multiplication

1. Optimization in linear algebra computations
2. Parsing in Natural Language Processing
3. Optimizing database query plans
4. RNA secondary structure prediction in bioinformatics

## Exercise

1. Implement a function that returns the actual sequence of matrix multiplications, not just the parenthesization.

2. Modify the algorithm to handle the case where some matrices cannot be multiplied together (i.e., their dimensions are incompatible).

3. Implement a variation of the problem where each matrix multiplication has an associated cost (not just based on dimensions), and find the optimal order to minimize total cost.

## Summary

Today, we explored Matrix Chain Multiplication, a classic optimization problem that demonstrates the power of dynamic programming. We implemented various approaches, from naive recursion to optimized dynamic programming solutions, and even a version that provides the optimal parenthesization.

Understanding Matrix Chain Multiplication and its solutions provides valuable insights into dynamic programming techniques and their applications in optimization problems, particularly those involving sequences of operations.

Tomorrow, we'll dive into another fundamental dynamic programming problem: the Longest Increasing Subsequence. Stay tuned!
