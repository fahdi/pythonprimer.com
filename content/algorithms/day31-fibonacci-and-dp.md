---
title: "Day 31: Fibonacci Sequence and Dynamic Programming"
weight: 31
menu:
  main:
    parent: "Algorithms"
    weight: 31
---

# Fibonacci Sequence and Dynamic Programming

Welcome to Day 31 of our 60 Days of Coding Algorithm Challenge! Today, we'll dive deeper into Dynamic Programming by exploring the Fibonacci sequence, a classic problem that demonstrates the power of DP.

## The Fibonacci Sequence

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. It typically starts with 0 and 1, and the sequence goes as follows:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Mathematically, it can be defined as:

F(n) = F(n-1) + F(n-2), where F(0) = 0 and F(1) = 1

## Naive Recursive Approach

Let's start with a naive recursive implementation:

```python
def fibonacci_naive(n):
    if n <= 1:
        return n
    return fibonacci_naive(n-1) + fibonacci_naive(n-2)

# Example usage
print(fibonacci_naive(10))  # Output: 55
```

While this implementation is simple and intuitive, it has a time complexity of O(2^n), making it extremely inefficient for large values of n.

## Dynamic Programming Approaches

We can significantly improve the efficiency using Dynamic Programming. Let's explore both top-down (memoization) and bottom-up (tabulation) approaches.

### Top-Down Approach (Memoization)

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

Time Complexity: O(n)
Space Complexity: O(n)

### Bottom-Up Approach (Tabulation)

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

Time Complexity: O(n)
Space Complexity: O(n)

### Space-Optimized Bottom-Up Approach

We can further optimize the space complexity:

```python
def fibonacci_optimized(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Example usage
print(fibonacci_optimized(100))  # Efficient in both time and space
```

Time Complexity: O(n)
Space Complexity: O(1)

## Comparison of Approaches

Let's compare the performance of these approaches:

```python
import time

def time_function(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start

n = 30
print(f"Calculating F({n}):")

result, time_naive = time_function(fibonacci_naive, n)
print(f"Naive Recursive: {result} (Time: {time_naive:.6f} seconds)")

result, time_memo = time_function(fibonacci_memo, n)
print(f"Memoization: {result} (Time: {time_memo:.6f} seconds)")

result, time_tab = time_function(fibonacci_tab, n)
print(f"Tabulation: {result} (Time: {time_tab:.6f} seconds)")

result, time_opt = time_function(fibonacci_optimized, n)
print(f"Optimized: {result} (Time: {time_opt:.6f} seconds)")
```

## Advanced: Matrix Exponentiation

For very large n, we can use matrix exponentiation to calculate Fibonacci numbers in O(log n) time:

```python
def fibonacci_matrix(n):
    def matrix_multiply(a, b):
        return [
            [a[0][0]*b[0][0] + a[0][1]*b[1][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]],
            [a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1]]
        ]

    def matrix_power(matrix, power):
        if power == 1:
            return matrix
        if power % 2 == 0:
            half_power = matrix_power(matrix, power // 2)
            return matrix_multiply(half_power, half_power)
        return matrix_multiply(matrix, matrix_power(matrix, power - 1))

    if n <= 1:
        return n
    base_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_power(base_matrix, n - 1)
    return result_matrix[0][0]

# Example usage
print(fibonacci_matrix(1000))  # Can calculate very large Fibonacci numbers
```

Time Complexity: O(log n)
Space Complexity: O(log n) due to the recursive calls in matrix_power

## Exercise

1. Implement a function to find the nth Fibonacci number modulo a given number M. This is useful for handling very large Fibonacci numbers.

2. The Fibonacci sequence can be extended to negative indices. Implement a function that can calculate F(n) for any integer n, positive or negative.

3. Implement a generator function that yields Fibonacci numbers indefinitely. Use this to find the first Fibonacci number greater than a million.

## Summary

Today, we explored the Fibonacci sequence as a classic example of Dynamic Programming. We implemented and compared various approaches, from naive recursion to optimized DP solutions and even matrix exponentiation for very large numbers.

Understanding these different approaches to the Fibonacci sequence provides insights into the power of Dynamic Programming and the trade-offs between time and space complexity.

Tomorrow, we'll explore another classic Dynamic Programming problem: the Longest Common Subsequence. Stay tuned!
