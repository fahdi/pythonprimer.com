---
title: "Day 39: Palindrome Partitioning"
weight: 39
menu:
  main:
    parent: "Algorithms"
    weight: 39
---

# Palindrome Partitioning

Welcome to Day 39 of our 60 Days of Coding Algorithm Challenge! Today, we'll explore the Palindrome Partitioning problem, which combines string manipulation with dynamic programming concepts.

## What is Palindrome Partitioning?

Palindrome Partitioning is the problem of dividing a string into substrings, where each substring is a palindrome. A palindrome is a string that reads the same backward as forward.

## Problem Statement

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

## Naive Recursive Approach

Let's start with a naive recursive implementation:

```python
def is_palindrome(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

def palindrome_partition_recursive(s):
    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])
            return
        
        for end in range(start, len(s)):
            if is_palindrome(s, start, end):
                path.append(s[start:end+1])
                backtrack(end + 1, path)
                path.pop()
    
    result = []
    backtrack(0, [])
    return result

# Example usage
s = "aab"
print(f"Palindrome partitions of '{s}': {palindrome_partition_recursive(s)}")
```

This approach has a time complexity of O(n * 2^n), where n is the length of the string, making it inefficient for longer strings.

## Dynamic Programming Approach

We can improve the efficiency using Dynamic Programming to precompute palindrome information.

```python
def palindrome_partition_dp(s):
    n = len(s)
    # dp[i][j] is True if s[i:j+1] is a palindrome
    dp = [[False] * n for _ in range(n)]
    
    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True
    
    # Check for substrings of length 2 and more
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if length == 2:
                dp[i][j] = (s[i] == s[j])
            else:
                dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
    
    def backtrack(start, path):
        if start == n:
            result.append(path[:])
            return
        
        for end in range(start, n):
            if dp[start][end]:
                path.append(s[start:end+1])
                backtrack(end + 1, path)
                path.pop()
    
    result = []
    backtrack(0, [])
    return result

# Example usage
s = "aab"
print(f"Palindrome partitions of '{s}': {palindrome_partition_dp(s)}")
```

This approach has a time complexity of O(n * 2^n) in the worst case, but it's generally faster due to the precomputation of palindrome information.

## Optimized Solution: Manacher's Algorithm

For very long strings, we can use Manacher's Algorithm to find all palindromic substrings in O(n) time, which can then be used to optimize our partitioning:

```python
def manacher(s):
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    p = [0] * n
    c = r = 0
    for i in range(1, n-1):
        mirror = 2*c - i
        if i < r:
            p[i] = min(r - i, p[mirror])
        while i + (1 + p[i]) < n and i - (1 + p[i]) >= 0 and t[i + (1 + p[i])] == t[i - (1 + p[i])]:
            p[i] += 1
        if i + p[i] > r:
            c, r = i, i + p[i]
    return p

def palindrome_partition_manacher(s):
    p = manacher(s)
    n = len(s)
    is_palindrome = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            center = i + j + 1
            radius = j - i
            if p[center] >= radius:
                is_palindrome[i][j] = True
    
    def backtrack(start, path):
        if start == n:
            result.append(path[:])
            return
        
        for end in range(start, n):
            if is_palindrome[start][end]:
                path.append(s[start:end+1])
                backtrack(end + 1, path)
                path.pop()
    
    result = []
    backtrack(0, [])
    return result

# Example usage
s = "aab"
print(f"Palindrome partitions of '{s}': {palindrome_partition_manacher(s)}")
```

This approach has a time complexity of O(n) for palindrome precomputation and O(2^n) for partitioning in the worst case.

## Applications of Palindrome Partitioning

1. Text processing and analysis
2. Bioinformatics (DNA sequence analysis)
3. Natural Language Processing
4. Cryptography and steganography

## Exercise

1. Modify the algorithm to find the minimum number of cuts needed to partition a string into palindromes.

2. Implement a function that finds the longest palindromic subsequence in a string using dynamic programming.

3. Create an algorithm that generates all possible palindromes that can be formed by rearranging the characters of a given string.

## Summary

Today, we explored the Palindrome Partitioning problem, which combines string manipulation with dynamic programming concepts. We implemented various approaches, from naive recursion to optimized solutions using Manacher's Algorithm.

Understanding Palindrome Partitioning and its solutions provides valuable insights into string manipulation techniques and their applications in various fields of computer science.

Tomorrow, we'll dive into another interesting problem: the Longest Palindromic Substring. Stay tuned!
