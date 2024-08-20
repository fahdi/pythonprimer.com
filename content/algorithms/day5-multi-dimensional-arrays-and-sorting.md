---
title: "Day 5: Multi-Dimensional Arrays and Sorting Algorithms"
weight: 5
menu:
  main:
    parent: "Algorithms"
    weight: 5
---

# Day 5: Multi-Dimensional Arrays and Sorting Algorithms

Welcome to Day 5 of our 60 Days of Coding Algorithm Challenge! Today, we’ll delve into the world of multi-dimensional arrays (such as matrices) and learn about some fundamental sorting algorithms. These are essential concepts in computer science that will provide you with the tools to solve more complex problems.

## Multi-Dimensional Arrays

A multi-dimensional array is essentially an array of arrays. The most common example is a two-dimensional array, often referred to as a matrix. Multi-dimensional arrays are used in a wide range of applications, from representing grids in games to storing data in scientific computing.

### Example: 2D Array (Matrix)

Let’s explore how to create and manipulate a 2D array:

```python
# Initializing a 2D array (3x3 matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing an element at row 1, column 2
print(matrix[1][2])  # Output: 6

# Traversing the matrix and printing all elements
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # Newline after each row
```

### Common Operations on 2D Arrays

Here are two fundamental operations you can perform on matrices:

1. **Matrix Addition**:
    - Adding two matrices involves adding the corresponding elements from each matrix.

    ```python
    def add_matrices(matrix1, matrix2):
        result = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix1[0])):
                row.append(matrix1[i][j] + matrix2[i][j])
            result.append(row)
        return result
    ```

    - **Explanation**: This function iterates over each element of the matrices, adds them together, and stores the result in a new matrix.

2. **Matrix Transposition**:
    - Transposing a matrix involves swapping its rows and columns.

    ```python
    def transpose_matrix(matrix):
        transposed = []
        for i in range(len(matrix[0])):
            row = []
            for j in range(len(matrix)):
                row.append(matrix[j][i])
            transposed.append(row)
        return transposed
    ```

    - **Explanation**: This function creates a new matrix where the rows and columns of the original matrix are flipped.

## Introduction to Sorting Algorithms

Sorting is one of the most common operations on arrays. Sorting algorithms are used to arrange the elements of an array in a specific order, typically ascending or descending. Understanding how sorting algorithms work is crucial for optimizing performance in many applications.

### Bubble Sort

Bubble Sort is a simple but inefficient sorting algorithm that repeatedly steps through the array, compares adjacent elements, and swaps them if they are in the wrong order.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to detect if any swapping occurred
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no swapping happened, array is already sorted
        if not swapped:
            break
    return arr
```

- **Explanation**: Bubble Sort checks each pair of adjacent elements and swaps them if they are in the wrong order. The algorithm repeats this process until no swaps are needed, indicating that the array is sorted.

### Selection Sort

Selection Sort divides the array into a sorted and unsorted region. It repeatedly selects the smallest element from the unsorted region and moves it to the end of the sorted region.

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the current index is the minimum
        min_index = i
        # Check the rest of the array to find the actual minimum
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
```

- **Explanation**: Selection Sort works by selecting the smallest element from the unsorted portion of the array and swapping it with the first unsorted element. This process is repeated, gradually growing the sorted portion of the array.

## Exercise

1. Write a function to multiply two matrices. Ensure that the number of columns in the first matrix equals the number of rows in the second matrix.
2. Implement an optimized version of Bubble Sort that stops early if the array is already sorted (as shown above).
3. Compare the time complexity and efficiency of Bubble Sort and Selection Sort when applied to large datasets. Analyze their performance and discuss which scenarios each algorithm might be best suited for.

## Summary

Multi-dimensional arrays and sorting algorithms are foundational concepts in programming. Mastering these topics will not only improve your problem-solving skills but also prepare you for tackling more advanced algorithms. Tomorrow, we’ll continue our journey by diving into more sophisticated sorting techniques and their practical applications.

Stay tuned!
