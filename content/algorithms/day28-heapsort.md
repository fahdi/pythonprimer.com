---
title: "Day 28: Heapsort Algorithm"
weight: 28
menu:
  main:
    parent: "Algorithms"
    weight: 28
---

# Heapsort Algorithm

Welcome to Day 28 of our 60 Days of Coding Algorithm Challenge! Today, we'll explore the Heapsort algorithm, an efficient, comparison-based sorting algorithm that leverages the properties of a heap data structure.

## Introduction to Heapsort

Heapsort is a sorting algorithm that uses a binary heap data structure to sort elements. It's an in-place algorithm with an O(n log n) time complexity, making it optimal for large datasets.

## How Heapsort Works

Heapsort works in two main steps:

1. Build a max heap from the input array.
2. Repeatedly extract the maximum element from the heap and place it at the end of the array.

## Implementing Heapsort

Let's implement the Heapsort algorithm:

```python
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    # Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr

# Example usage
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = heapsort(arr)
print(f"Sorted array: {sorted_arr}")
```

## Time Complexity

- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n log n)

Heapsort has a consistent time complexity of O(n log n) for all cases, which is one of its main advantages.

## Space Complexity

- O(1) - Heapsort is an in-place sorting algorithm, requiring only a constant amount of additional memory.

## Advantages of Heapsort

1. Efficient time complexity of O(n log n) for all cases.
2. In-place sorting algorithm, requiring no extra space.
3. Relatively simple to implement compared to other efficient sorting algorithms.

## Disadvantages of Heapsort

1. Not stable: Does not preserve the relative order of equal elements.
2. Poor cache performance: The algorithm's access pattern to memory can lead to many cache misses.
3. Generally slower in practice compared to well-implemented Quicksort on average.

## Optimizations for Heapsort

### 1. Bottom-up Heap Construction

Instead of using top-down heapify for initial heap construction, we can use a bottom-up approach which is more efficient:

```python
def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
```

### 2. Heap Optimization for Small Arrays

For small arrays or subarrays, we can switch to insertion sort:

```python
def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def optimized_heapsort(arr):
    n = len(arr)
    
    # Use insertion sort for small arrays
    if n <= 10:
        insertion_sort(arr, 0, n - 1)
        return arr
    
    # Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr
```

## Applications of Heapsort

1. **External Sorting**: When dealing with large datasets that don't fit into memory.
2. **K-way Merging**: Efficiently merging k sorted arrays.
3. **Finding the k largest/smallest elements**: Heapsort can be modified to find these efficiently.
4. **Priority Queues**: The underlying heap structure is used in priority queue implementations.

## Comparison with Other Sorting Algorithms

| Algorithm | Time Complexity (Average) | Time Complexity (Worst) | Space Complexity | Stable |
|-----------|---------------------------|-------------------------|-------------------|--------|
| Heapsort  | O(n log n)                | O(n log n)              | O(1)              | No     |
| Quicksort | O(n log n)                | O(n^2)                  | O(log n)          | No     |
| Mergesort | O(n log n)                | O(n log n)              | O(n)              | Yes    |

## Exercise

1. Implement a variation of Heapsort that sorts the array in descending order.
2. Modify the Heapsort algorithm to find the k largest elements in an array.
3. Implement an iterative version of Heapsort (without using recursion for the heapify process).

## Summary

Today, we explored the Heapsort algorithm, an efficient comparison-based sorting algorithm that leverages the heap data structure. We implemented the basic algorithm, discussed its time and space complexity, and looked at some optimizations.

Heapsort's consistent O(n log n) time complexity and in-place sorting make it a valuable algorithm to understand and use, especially when dealing with large datasets or in memory-constrained environments.

As we conclude our exploration of comparison-based sorting algorithms, it's important to understand the trade-offs between Heapsort, Quicksort, and Mergesort. Each has its strengths and is suited to different scenarios.

Tomorrow, we'll dive into a comprehensive comparison of sorting algorithms, analyzing their performance in various scenarios and discussing how to choose the right sorting algorithm for specific use cases. Stay tuned!
