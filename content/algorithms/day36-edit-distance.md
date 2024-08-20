---
title: "Day 36: Edit Distance Problem"
weight: 36
menu:
  main:
    parent: "Algorithms"
    weight: 36
---

# Edit Distance Problem

Welcome to Day 36 of our 60 Days of Coding Algorithm Challenge! Today, we'll explore the Edit Distance Problem, a classic dynamic programming problem with applications in natural language processing, bioinformatics, and more.

## What is the Edit Distance Problem?

The Edit Distance Problem, also known as the Levenshtein Distance Problem, is about finding the minimum number of operations required to transform one string into another. The allowed operations are:

1. Insert a character
2. Delete a character
3. Replace a character

For example, the edit distance between "kitten" and "sitting" is 3, as we need to:
1. Replace 'k' with 's'
2. Replace 'e' with 'i'
3. Insert 'g' at the end

## Naive Recursive Approach

Let's start with a naive recursive implementation:

```python
def edit_distance_naive(str1, str2, m, n):
    # If first string is empty, insert all characters of second string
    if m == 0:
        return n

    # If second string is empty, remove all characters of first string
    if n == 0:
        return m

    # If last characters are same, ignore last char and recur for remaining string
    if str1[m-1] == str2[n-1]:
        return edit_distance_naive(str1, str2, m-1, n-1)

    # If last characters are different, consider all possibilities and find minimum
    return 1 + min(edit_distance_naive(str1, str2, m, n-1),    # Insert
                   edit_distance_naive(str1, str2, m-1, n),    # Remove
                   edit_distance_naive(str1, str2, m-1, n-1))  # Replace

# Example usage
str1 = "kitten"
str2 = "sitting"
print(f"Edit Distance between '{str1}' and '{str2}': {edit_distance_naive(str1, str2, len(str1), len(str2))}")
```

This approach has a time complexity of O(3^(m+n)), making it inefficient for longer strings.

## Dynamic Programming Approach

We can significantly improve the efficiency using Dynamic Programming.

### Top-Down Approach (Memoization)

```python
def edit_distance_memo(str1, str2):
    m, n = len(str1), len(str2)
    memo = {}

    def dp(i, j):
        if i == 0:
            return j
        if j == 0:
            return i

        if (i, j) in memo:
            return memo[(i, j)]

        if str1[i-1] == str2[j-1]:
            memo[(i, j)] = dp(i-1, j-1)
        else:
            memo[(i, j)] = 1 + min(dp(i, j-1),    # Insert
                                   dp(i-1, j),    # Remove
                                   dp(i-1, j-1))  # Replace
        return memo[(i, j)]

    return dp(m, n)

# Example usage
str1 = "kitten"
str2 = "sitting"
print(f"Edit Distance between '{str1}' and '{str2}': {edit_distance_memo(str1, str2)}")
```

### Bottom-Up Approach (Tabulation)

```python
def edit_distance_tab(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Fill d[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):
            # If first string is empty, only option is to insert all characters of second string
            if i == 0:
                dp[i][j] = j

            # If second string is empty, only option is to remove all characters of first string
            elif j == 0:
                dp[i][j] = i

            # If last characters are same, ignore last char and recur for remaining string
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            # If last characters are different, consider all possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j-1],      # Insert
                                   dp[i-1][j],      # Remove
                                   dp[i-1][j-1])    # Replace

    return dp[m][n]

# Example usage
str1 = "kitten"
str2 = "sitting"
print(f"Edit Distance between '{str1}' and '{str2}': {edit_distance_tab(str1, str2)}")
```

Both Dynamic Programming approaches have a time complexity of O(mn) and a space complexity of O(mn), where m and n are the lengths of the input strings.

## Printing the Edits

We can modify our solution to also print the actual edits needed:

```python
def edit_distance_with_path(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Fill dp[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

    # Backtrack to find the edits
    edits = []
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i-1][j-1] + 1:
            edits.append(f"Replace '{str1[i-1]}' with '{str2[j-1]}'")
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i-1][j] + 1:
            edits.append(f"Delete '{str1[i-1]}'")
            i -= 1
        elif dp[i][j] == dp[i][j-1] + 1:
            edits.append(f"Insert '{str2[j-1]}'")
            j -= 1

    while i > 0:
        edits.append(f"Delete '{str1[i-1]}'")
        i -= 1
    while j > 0:
        edits.append(f"Insert '{str2[j-1]}'")
        j -= 1

    return dp[m][n], reversed(edits)

# Example usage
str1 = "kitten"
str2 = "sitting"
distance, edits = edit_distance_with_path(str1, str2)
print(f"Edit Distance between '{str1}' and '{str2}': {distance}")
print("Edits:")
for edit in edits:
    print(edit)
```

## Applications of Edit Distance

1. Spell checking and correction
2. DNA sequence alignment in bioinformatics
3. Plagiarism detection
4. Machine translation and natural language processing
5. Fuzzy string searching

## Exercise

1. Implement a version of the Edit Distance algorithm where the costs of insertion, deletion, and replacement are different.

2. Modify the algorithm to find the longest common subsequence of two strings.

3. Implement a function that uses Edit Distance to find similar words in a dictionary (like a simple spell checker).

## Summary

Today, we explored the Edit Distance Problem, a classic example of dynamic programming. We implemented various approaches, from naive recursion to optimized dynamic programming solutions, and even a version that provides the actual sequence of edits.

Understanding the Edit Distance problem and its solutions provides valuable insights into dynamic programming techniques and their applications in string manipulation and comparison problems.

Tomorrow, we'll dive into another fundamental algorithm: the Bellman-Ford algorithm for finding shortest paths in a graph with negative edge weights. Stay tuned!
