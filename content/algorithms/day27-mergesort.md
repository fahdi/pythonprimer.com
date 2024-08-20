---
title: "Day 27: Mergesort Algorithm"
weight: 27
menu:
  main:
    parent: "Algorithms"
    weight: 27
---

# Mergesort Algorithm

Welcome to Day 27 of our 60 Days of Coding Algorithm Challenge! Today, we'll dive deep into the Mergesort algorithm, another efficient and widely used sorting algorithm based on the divide-and-conquer paradigm.

## Introduction to Mergesort

Mergesort is a comparison-based sorting algorithm that follows the divide-and-conquer approach. It divides the input array into two halves, recursively sorts them, and then merges the two sorted halves.

## How Mergesort Works

1. Divide the unsorted list into n sublists, each containing one element (a list of one element is considered sorted).
2. Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.

## Basic Implementation of Mergesort

Here's a basic implementation of the Mergesort algorithm:

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(f"Sorted array: {sorted_arr}")
```

## In-place Mergesort Implementation

While the above implementation is easy to understand, it uses additional space for creating new lists. Here's an in-place implementation:

```python
def merge_sort_inplace(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort_inplace(arr, left, mid)
        merge_sort_inplace(arr, mid + 1, right)
        merge_inplace(arr, left, mid, right)

def merge_inplace(arr, left, mid, right):
    left_arr = arr[left:mid+1]
    right_arr = arr[mid+1:right+1]
    
    i, j, k = 0, 0, left
    
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort_inplace(arr, 0, len(arr) - 1)
print(f"Sorted array: {arr}")
```

## Time Complexity

- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n log n)

Mergesort has a consistent time complexity of O(n log n) for all cases, which is one of its main advantages.

## Space Complexity

- O(n) for the basic implementation
- O(n) for the in-place implementation (due to the temporary arrays in the merge step)

## Advantages of Mergesort

1. Stable: Preserves the relative order of equal elements
2. Guaranteed O(n log n) time complexity for all cases
3. Well-suited for external sorting (sorting large datasets that don't fit in memory)

## Disadvantages of Mergesort

1. Requires extra space O(n) for merging
2. For small datasets, it may be slower than simpler algorithms like insertion sort

## Optimizations for Mergesort

### 1. Using Insertion Sort for Small Subarrays

For small subarrays, it's more efficient to use insertion sort:

```python
def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort_optimized(arr, left, right):
    if right - left <= 10:  # Use insertion sort for small subarrays
        insertion_sort(arr, left, right)
    elif left < right:
        mid = (left + right) // 2
        merge_sort_optimized(arr, left, mid)
        merge_sort_optimized(arr, mid + 1, right)
        merge_inplace(arr, left, mid, right)

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort_optimized(arr, 0, len(arr) - 1)
print(f"Sorted array: {arr}")
```

### 2. Avoiding Unnecessary Copying

We can avoid copying elements in the merge step if the last element of the left subarray is smaller than or equal to the first element of the right subarray:

```python
def merge_optimized(arr, left, mid, right):
    if arr[mid] <= arr[mid + 1]:
        return  # Arrays are already sorted
    
    left_arr = arr[left:mid+1]
    right_arr = arr[mid+1:right+1]
    
    i, j, k = 0, 0, left
    
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
```

## Applications of Mergesort

1. External sorting: Sorting large files that don't fit in memory
2. Sorting linked lists: Mergesort is particularly efficient for linked lists
3. Counting inversions in an array
4. Used in various external sorting algorithms in database systems

## Comparison with Quicksort

| Aspect | Mergesort | Quicksort |
|--------|-----------|-----------|
| Time Complexity | Always O(n log n) | Average: O(n log n), Worst: O(n^2) |
| Space Complexity | O(n) | O(log n) |
| Stability | Stable | Not stable |
| In-place | Not in-place | In-place |
| Adaptivity | Not adaptive | Can be made adaptive |
| Locality of reference | Good | Excellent |

## Exercise

1. Implement a bottom-up (iterative) version of Mergesort.
2. Modify the Mergesort algorithm to count the number of inversions in an array.
3. Implement Mergesort for a linked list.

## Summary

Today, we explored the Mergesort algorithm, an efficient and stable sorting algorithm based on the divide-and-conquer paradigm. We implemented basic and optimized versions of Mergesort, discussed its time and space complexity, and looked at various optimization techniques.

Mergesort's consistent performance and stability make it a crucial algorithm to understand for any programmer, especially when dealing with large datasets or when stability is important.

Tomorrow, we'll dive into heap sort, another efficient comparison-based sorting algorithm. We'll explore its unique characteristics and compare it with Quicksort and Mergesort. Stay tuned!

