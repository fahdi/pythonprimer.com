---
title: "Day 41: Activity Selection Problem"
weight: 41
menu:
  main:
    parent: "Algorithms"
    weight: 41
---

# Activity Selection Problem

Welcome to Day 41 of our 60 Days of Coding Algorithm Challenge! Today, we'll dive deep into the Activity Selection Problem, a classic example of how greedy algorithms can be used to solve optimization problems efficiently.

## What is the Activity Selection Problem?

The Activity Selection Problem involves selecting the maximum number of non-overlapping activities that can be performed by a single person or machine, given a set of activities with their start and finish times.

## Problem Statement

Given n activities with their start and finish times, select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.

## Greedy Approach

The greedy approach to solve this problem is to always pick the next activity with the earliest finish time. This approach works because choosing the activity with the earliest finish time leaves more room for other activities.

## Implementation

Let's implement the Activity Selection Problem using Python:

```python
def activity_selection(start, finish):
    n = len(start)
    
    # Sort activities by finish time
    activities = sorted(zip(start, finish), key=lambda x: x[1])
    
    selected = [0]  # First activity is always selected
    last_finish = activities[0][1]
    
    for i in range(1, n):
        if activities[i][0] >= last_finish:
            selected.append(i)
            last_finish = activities[i][1]
    
    return selected

# Example usage
start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
selected = activity_selection(start, finish)
print("Selected activities:", selected)

# Print detailed schedule
print("\nDetailed Schedule:")
for i in selected:
    print(f"Activity {i}: Start time = {start[i]}, Finish time = {finish[i]}")
```

## Time Complexity

- Sorting the activities: O(n log n)
- Selecting activities: O(n)

Overall time complexity: O(n log n), where n is the number of activities.

## Space Complexity

O(n) to store the sorted list of activities.

## Proof of Correctness

The greedy choice property holds for this problem because:

1. Choosing the activity with the earliest finish time is always safe.
2. After choosing an activity, the subproblem we're left with is of the same type.

## Variations of the Problem

1. **Weighted Activity Selection**: Each activity has a weight or value, and the goal is to maximize the total value.
2. **Multiple Resource Activity Selection**: Multiple people or machines are available to perform activities.
3. **Activity Selection with Deadlines**: Each activity has a deadline, and the goal is to schedule as many activities as possible before their deadlines.

## Real-world Applications

1. Scheduling classes in a classroom
2. Managing meeting rooms in an office
3. Allocating tasks to a single processor
4. TV program scheduling

## Exercise

1. Modify the algorithm to handle the case where activities are not sorted by finish time initially.
2. Implement the Weighted Activity Selection Problem using dynamic programming.
3. Solve the Activity Selection Problem when activities have deadlines and penalties for missing the deadlines.

## Summary

Today, we explored the Activity Selection Problem, a classic example of how greedy algorithms can efficiently solve certain types of optimization problems. We implemented a solution, discussed its time and space complexity, and looked at variations and real-world applications of the problem.

Understanding the Activity Selection Problem and its solutions provides valuable insights into greedy algorithms and their applications in scheduling and resource allocation problems.

Tomorrow, we'll dive into another fundamental greedy algorithm: Huffman Coding for data compression. Stay tuned!
