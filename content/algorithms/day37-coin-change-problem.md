---
title: "Day 37: Coin Change Problem"
weight: 37
menu:
  main:
    parent: "Algorithms"
    weight: 37
---

# Coin Change Problem

Welcome to Day 37 of our 60 Days of Coding Algorithm Challenge! Today, we'll explore the Coin Change Problem, a classic dynamic programming problem with applications in various fields, including currency systems and algorithmic trading.

## What is the Coin Change Problem?

The Coin Change Problem is about finding the number of ways to make change for a particular amount of money, given a set of coin denominations. There are two common variations of this problem:

1. Finding the total number of ways to make the change.
2. Finding the minimum number of coins needed to make the change.

We'll explore both variations in this lesson.

## Variation 1: Number of Ways to Make Change

### Problem Statement

Given an amount N and a set of coin denominations, find the total number of ways to make change for N.

### Naive Recursive Approach

Let's start with a naive recursive implementation:

```python
def coin_change_recursive(coins, amount):
    def recursive_helper(index, remaining):
        if remaining == 0:
            return 1
        if remaining < 0 or index >= len(coins):
            return 0
        
        # Include the current coin or exclude it
        return (recursive_helper(index, remaining - coins[index]) + 
                recursive_helper(index + 1, remaining))
    
    return recursive_helper(0, amount)

# Example usage
coins = [1, 2, 5]
amount = 5
print(f"Number of ways to make change for {amount}: {coin_change_recursive(coins, amount)}")
```

This approach has a time complexity of O(2^n), where n is the amount, making it inefficient for larger amounts.

### Dynamic Programming Approach

We can significantly improve the efficiency using Dynamic Programming.

```python
def coin_change_dp(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1  # Base case: there's one way to make change for 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    
    return dp[amount]

# Example usage
coins = [1, 2, 5]
amount = 5
print(f"Number of ways to make change for {amount}: {coin_change_dp(coins, amount)}")
```

This approach has a time complexity of O(amount * len(coins)) and a space complexity of O(amount).

## Variation 2: Minimum Number of Coins

### Problem Statement

Given an amount N and a set of coin denominations, find the minimum number of coins needed to make change for N.

### Dynamic Programming Approach

```python
def min_coins_dp(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage
coins = [1, 2, 5]
amount = 11
print(f"Minimum coins needed for {amount}: {min_coins_dp(coins, amount)}")
```

This approach also has a time complexity of O(amount * len(coins)) and a space complexity of O(amount).

## Printing the Coin Combination

We can modify our solution to also print the actual combination of coins used:

```python
def min_coins_with_combination(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin
    
    if dp[amount] == float('inf'):
        return -1, []
    
    # Reconstruct the coin combination
    combination = []
    current = amount
    while current > 0:
        combination.append(coin_used[current])
        current -= coin_used[current]
    
    return dp[amount], combination

# Example usage
coins = [1, 2, 5]
amount = 11
min_coins, combination = min_coins_with_combination(coins, amount)
print(f"Minimum coins needed for {amount}: {min_coins}")
print(f"Coin combination: {combination}")
```

## Applications of the Coin Change Problem

1. Currency systems and cash dispensing machines
2. Financial algorithms for minimizing transaction costs
3. Resource allocation in computer systems
4. Solving scheduling problems with discrete time units

## Exercise

1. Modify the first variation to find the number of unique ways to make change (where the order of coins doesn't matter).

2. Implement a solution for the case where you have a limited supply of each coin denomination.

3. Solve the Coin Change Problem for a system where some coin denominations might not be available (i.e., you're given a set of possible denominations, but not all are guaranteed to be in your coin set).

## Summary

Today, we explored the Coin Change Problem, a classic example of dynamic programming. We implemented solutions for two variations of the problem: finding the number of ways to make change and finding the minimum number of coins needed.

Understanding the Coin Change Problem and its solutions provides valuable insights into dynamic programming techniques and their applications in optimization and counting problems.

Tomorrow, we'll dive into another fundamental algorithm: the Floyd-Warshall algorithm for finding shortest paths in a weighted graph with positive or negative edge weights. Stay tuned!
