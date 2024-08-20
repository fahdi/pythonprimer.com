---
title: "Day 17: Heaps and Priority Queues"
weight: 17
menu:
  main:
    parent: "Algorithms"
    weight: 17
---

# Heaps and Priority Queues

Welcome to Day 17 of our 60 Days of Coding Algorithm Challenge! Today, we'll explore Heaps and Priority Queues, powerful data structures that are essential for many efficient algorithms.

## What is a Heap?

A Heap is a specialized tree-based data structure that satisfies the heap property:

- In a max heap, for any given node C, if P is a parent node of C, then the key (value) of P is greater than or equal to the key of C.
- In a min heap, the key of P is less than or equal to the key of C.

The heap is one maximally efficient implementation of an abstract data type called a priority queue.

## Types of Heaps

1. **Max Heap**: The root node has the largest value, and the property is maintained for all sub-trees.
2. **Min Heap**: The root node has the smallest value, and the property is maintained for all sub-trees.

## Implementing a Binary Heap in Python

We'll implement a min heap using a list in Python:

```python
class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
        parent = self.parent(i)
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.swap(i, parent)
            self._heapify_up(parent)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_val

    def _heapify_down(self, i):
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left
        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right

        if min_index != i:
            self.swap(i, min_index)
            self._heapify_down(min_index)

    def build_heap(self, arr):
        self.heap = arr
        for i in range(len(arr) // 2 - 1, -1, -1):
            self._heapify_down(i)

# Example usage
heap = MinHeap()
heap.insert(3)
heap.insert(2)
heap.insert(1)
heap.insert(15)
heap.insert(5)
heap.insert(4)
heap.insert(45)

print("Extracting elements from the min heap:")
for _ in range(7):
    print(heap.extract_min(), end=" ")
```

## Priority Queue

A priority queue is an abstract data type similar to a regular queue or stack data structure. Each element in a priority queue has an associated priority. Elements with higher priorities are served before elements with lower priorities.

### Implementing Priority Queue using Heap

We can easily implement a priority queue using our MinHeap implementation:

```python
class PriorityQueue:
    def __init__(self):
        self.heap = MinHeap()

    def enqueue(self, item, priority):
        self.heap.insert((priority, item))

    def dequeue(self):
        return self.heap.extract_min()[1]

    def is_empty(self):
        return len(self.heap.heap) == 0

# Example usage
pq = PriorityQueue()
pq.enqueue("Task 1", 3)
pq.enqueue("Task 2", 1)
pq.enqueue("Task 3", 2)

print("Dequeuing tasks:")
while not pq.is_empty():
    print(pq.dequeue())
```

## Time Complexity of Heap Operations

- Insert: O(log n)
- Extract Min/Max: O(log n)
- Peek (getting the min/max element): O(1)
- Build Heap: O(n)

## Applications of Heaps and Priority Queues

1. **Heapsort**: An efficient sorting algorithm with O(n log n) time complexity.
2. **Dijkstra's Algorithm**: For finding the shortest path in a graph.
3. **Prim's Algorithm**: For finding the minimum spanning tree in a graph.
4. **Huffman Coding**: Used in data compression.
5. **Median Maintenance**: Efficiently finding the median in a stream of numbers.
6. **Event-driven Simulation**: Managing events based on their scheduled time.
7. **Task Scheduling**: Prioritizing tasks in operating systems.

## Implementing Heapsort

Here's an implementation of the Heapsort algorithm using our MinHeap:

```python
def heapsort(arr):
    heap = MinHeap()
    heap.build_heap(arr)
    sorted_arr = []
    for _ in range(len(arr)):
        sorted_arr.append(heap.extract_min())
    return sorted_arr

# Example usage
unsorted_array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = heapsort(unsorted_array)
print("Sorted array:", sorted_array)
```

## Advanced Heap Variants

1. **Fibonacci Heap**: Provides better amortized performance for some operations.
2. **Binomial Heap**: A heap similar to a binary heap but also supports quick merging of two heaps.
3. **Leftist Heap**: A variant of binary heap that supports efficient merging.

## Exercise

1. Implement a max heap and use it to find the k-th largest element in an array.
2. Create a method to merge two binary heaps efficiently.
3. Implement a double-ended priority queue that can extract both the minimum and maximum elements efficiently.

## Summary

Today, we explored Heaps and Priority Queues, powerful data structures that are crucial for many efficient algorithms. We implemented a binary min heap and used it to create a priority queue. We also discussed the time complexities of various heap operations and explored some applications of heaps.

Understanding heaps and priority queues is essential for solving a wide range of algorithmic problems, especially those involving sorting, graph algorithms, and optimization problems. As we progress through this challenge, you'll find these data structures invaluable in tackling complex problems efficiently.

Tomorrow, we'll begin our exploration of graph data structures and algorithms, starting with an introduction to graphs and their representations. Stay tuned!
