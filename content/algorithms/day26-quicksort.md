---
title: "Day 26: Quicksort Algorithm"
weight: 26
menu:
  main:
    parent: "Algorithms"
    weight: 26
---

# Quicksort Algorithm

Welcome to Day 26 of our 60 Days of Coding Algorithm Challenge! Today, we'll dive deep into the Quicksort algorithm, one of the most efficient and widely used sorting algorithms in practice.

## Introduction to Quicksort

Quicksort is a divide-and-conquer algorithm that works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

## How Quicksort Works

1. Choose a pivot element from the array.
2. Partition the array around the pivot, such that:
   - All elements less than the pivot are moved to its left.
   - All elements greater than the pivot are moved to its right.
3. Recursively apply steps 1-2 to the sub-array of elements with smaller values and the sub-array of elements with greater values.

## Basic Implementation of Quicksort

Here's a basic implementation of the Quicksort algorithm:

```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quicksort(arr)
print(f"Sorted array: {sorted_arr}")
```

## In-place Quicksort Implementation

While the above implementation is easy to understand, it's not the most efficient as it creates new lists. Here's an in-place implementation:

```python
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort_inplace(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort_inplace(arr, low, pi - 1)
        quicksort_inplace(arr, pi + 1, high)

# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
quicksort_inplace(arr, 0, len(arr) - 1)
print(f"Sorted array: {arr}")
```

## Time Complexity

- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n^2) - This occurs when the pivot is always the smallest or largest element.

## Space Complexity

- O(log n) - Due to the recursive calls on the call stack.

## Optimizations for Quicksort

### 1. Choosing the Pivot

The choice of pivot can significantly affect the performance of Quicksort. Some common strategies include:

1. Choose the first element as pivot
2. Choose the last element as pivot
3. Choose the middle element as pivot
4. Choose a random element as pivot
5. Median-of-three (choose the median of the first, middle, and last elements)

Here's an implementation using the median-of-three strategy:

```python
def median_of_three(arr, low, high):
    mid = (low + high) // 2
    if arr[low] <= arr[mid] <= arr[high] or arr[high] <= arr[mid] <= arr[low]:
        return mid
    elif arr[mid] <= arr[low] <= arr[high] or arr[high] <= arr[low] <= arr[mid]:
        return low
    else:
        return high

def partition_median(arr, low, high):
    pivot_index = median_of_three(arr, low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return partition(arr, low, high)

def quicksort_optimized(arr, low, high):
    if low < high:
        pi = partition_median(arr, low, high)
        quicksort_optimized(arr, low, pi - 1)
        quicksort_optimized(arr, pi + 1, high)

# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
quicksort_optimized(arr, 0, len(arr) - 1)
print(f"Sorted array: {arr}")
```

### 2. Handling Small Subarrays

For small subarrays, it's often more efficient to use a simpler sorting algorithm like insertion sort:

```python
def insertion_sort(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def quicksort_hybrid(arr, low, high):
    while low < high:
        if high - low + 1 < 10:
            insertion_sort(arr, low, high)
            break
        else:
            pi = partition_median(arr, low, high)
            if pi - low < high - pi:
                quicksort_hybrid(arr, low, pi - 1)
                low = pi + 1
            else:
                quicksort_hybrid(arr, pi + 1, high)
                high = pi - 1

# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
quicksort_hybrid(arr, 0, len(arr) - 1)
print(f"Sorted array: {arr}")
```

## Advantages and Disadvantages of Quicksort

### Advantages:
1. Efficient on average: O(n log n)
2. In-place sorting: Requires little additional memory
3. Cache-friendly: Good locality of reference

### Disadvantages:
1. Worst-case time complexity of O(n^2)
2. Not stable: Does not preserve the relative order of equal elements
3. Vulnerable to pathological data sets that can trigger worst-case behavior

## Applications of Quicksort

1. General-purpose sorting: Used in many standard library sort functions
2. Numerical computations: Efficiently sorting large datasets
3. Information retrieval: Sorting search results
4. Database systems: Indexing and sorting records

## Exercise

1. Implement a three-way partitioning Quicksort that handles duplicate elements efficiently.
2. Create a version of Quicksort that uses two pivots instead of one.
3. Implement an iterative version of Quicksort using a stack to manage the recursive calls.

## Summary

Today, we explored the Quicksort algorithm, one of the most efficient and widely used sorting algorithms. We implemented basic and optimized versions of Quicksort, discussed its time and space complexity, and looked at various optimization techniques.

Quicksort's efficiency and adaptability make it a crucial algorithm to understand for any programmer. Its divide-and-conquer approach is a powerful paradigm that can be applied to many other problems.

Tomorrow, we'll dive into another efficient sorting algorithm: Mergesort. We'll compare it with Quicksort and explore its unique characteristics. Stay tuned!

