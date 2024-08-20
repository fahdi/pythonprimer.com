---
title: "Day 32: Longest Common Subsequence"
weight: 32
menu:
  main:
    parent: "Algorithms"
    weight: 32
---

# Longest Common Subsequence (LCS)

Welcome to Day 32 of our 60 Days of Coding Algorithm Challenge! Today, we'll explore the Longest Common Subsequence (LCS) problem, a classic example of dynamic programming.

## What is the Longest Common Subsequence?

The Longest Common Subsequence problem is to find the longest subsequence common to all sequences in a set of sequences. Unlike substrings, subsequences are not required to occupy consecutive positions within the original sequences.

For example, the LCS of "ABCDGH" and "AEDFHR" is "ADH" of length 3.

## Naive Recursive Approach

Let's start with a naive recursive implementation:

```python
def lcs_naive(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 + lcs_naive(X, Y, m-1, n-1)
    else:
        return max(lcs_naive(X, Y, m, n-1), lcs_naive(X, Y, m-1, n))

# Example usage
X = "ABCDGH"
Y = "AEDFHR"
print(f"Length of LCS is {lcs_naive(X, Y, len(X), len(Y))}")
```

This approach has a time complexity of O(2^n) in the worst case, making it inefficient for longer sequences.

## Dynamic Programming Approach

We can significantly improve the efficiency using Dynamic Programming. Let's implement both top-down (memoization) and bottom-up (tabulation) approaches.

### Top-Down Approach (Memoization)

```python
def lcs_memo(X, Y):
    def lcs_helper(m, n, memo):
        if m == 0 or n == 0:
            return 0
        if (m, n) in memo:
            return memo[(m, n)]
        if X[m-1] == Y[n-1]:
            memo[(m, n)] = 1 + lcs_helper(m-1, n-1, memo)
        else:
            memo[(m, n)] = max(lcs_helper(m, n-1, memo), lcs_helper(m-1, n, memo))
        return memo[(m, n)]
    
    return lcs_helper(len(X), len(Y), {})

# Example usage
X = "ABCDGH"
Y = "AEDFHR"
print(f"Length of LCS is {lcs_memo(X, Y)}")
```

### Bottom-Up Approach (Tabulation)

```python
def lcs_tab(X, Y):
    m, n = len(X), len(Y)
    L = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    
    return L[m][n]

# Example usage
X = "ABCDGH"
Y = "AEDFHR"
print(f"Length of LCS is {lcs_tab(X, Y)}")
```

Both of these Dynamic Programming approaches have a time complexity of O(mn) and a space complexity of O(mn), where m and n are the lengths of the input sequences.

## Printing the Longest Common Subsequence

We can modify our bottom-up approach to not only find the length of the LCS but also print the LCS itself:

```python
def print_lcs(X, Y):
    m, n = len(X), len(Y)
    L = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill L[][] in bottom up fashion
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    
    # Following steps build LCS string from L[][]
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
print(f"LCS of {X} and {Y} is {print_lcs(X, Y)}")
```

## Space-Optimized Solution

We can optimize the space complexity to O(min(m,n)) by only keeping track of the current and previous rows of the DP table:

```python
def lcs_space_optimized(X, Y):
    m, n = len(X), len(Y)
    
    # Make sure X is the shorter string
    if m > n:
        return lcs_space_optimized(Y, X)
    
    # Previous and current row of the DP table
    prev = [0] * (m + 1)
    curr = [0] * (m + 1)
    
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if X[i-1] == Y[j-1]:
                curr[i] = prev[i-1] + 1
            else:
                curr[i] = max(curr[i-1], prev[i])
        prev, curr = curr, prev
    
    return prev[m]

# Example usage
X = "ABCDGH"
Y = "AEDFHR"
print(f"Length of LCS is {lcs_space_optimized(X, Y)}")
```

This optimized version has a space complexity of O(min(m,n)) while maintaining the time complexity of O(mn).

## Applications of LCS

1. DNA sequence alignment in bioinformatics
2. File comparison (diff utility)
3. Plagiarism detection
4. Version control systems

## Exercise

1. Implement a function to find the Longest Common Substring (contiguous) of two strings using dynamic programming.

2. Modify the LCS algorithm to find the Longest Palindromic Subsequence of a given string.

3. Implement a function to find the Shortest Common Supersequence of two strings using the LCS algorithm.

## Summary

Today, we explored the Longest Common Subsequence problem, a classic example of dynamic programming. We implemented various approaches, from naive recursion to optimized dynamic programming solutions, and even a space-optimized version.

Understanding the LCS problem and its solutions provides valuable insights into dynamic programming techniques and their applications in string manipulation and comparison problems.

Tomorrow, we'll dive into another fundamental dynamic programming problem: the Knapsack Problem. Stay tuned!
