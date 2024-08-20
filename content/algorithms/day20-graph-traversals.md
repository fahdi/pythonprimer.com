---
title: "Day 20: Graph Traversals - BFS and DFS"
weight: 20
menu:
  main:
    parent: "Algorithms"
    weight: 20
---

# Graph Traversals - BFS and DFS

Welcome to Day 20 of our 60 Days of Coding Algorithm Challenge! Today, we'll dive into two fundamental graph traversal algorithms: Breadth-First Search (BFS) and Depth-First Search (DFS). These algorithms form the basis for many more complex graph algorithms and are essential for solving a wide range of problems.

## Introduction to Graph Traversals

Graph traversal refers to the process of visiting (checking and/or updating) each vertex in a graph. The order in which the vertices are visited defines the traversal algorithm. The two most common traversal algorithms are:

1. Breadth-First Search (BFS)
2. Depth-First Search (DFS)

## Breadth-First Search (BFS)

BFS explores a graph level by level. It visits all the neighbors of a vertex before moving to the next level neighbors.

### Algorithm:
1. Start from a chosen source vertex and add it to a queue.
2. Visit the vertex at the front of the queue and remove it.
3. Add all unvisited neighbors of this vertex to the queue.
4. Repeat steps 2-3 until the queue is empty.

### Implementation:

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example usage
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 4],
    3: [1, 4],
    4: [2, 3]
}

print("BFS starting from vertex 0:")
bfs(graph, 0)
```

### Time Complexity:
- O(V + E), where V is the number of vertices and E is the number of edges.

### Space Complexity:
- O(V) for the queue and visited set.

### Applications of BFS:
1. Finding the shortest path in an unweighted graph
2. Web crawlers
3. Social networking features (e.g., finding friends within a certain degree of connection)
4. GPS Navigation systems
5. Puzzle solving (e.g., solving a Rubik's cube in the least number of moves)

## Depth-First Search (DFS)

DFS explores a graph by going as deep as possible along each branch before backtracking.

### Algorithm:
1. Start from a chosen source vertex.
2. Explore one of its unvisited neighbors.
3. Repeat step 2 for the newly visited vertex.
4. If all neighbors are visited, backtrack to the previous vertex.
5. Repeat steps 2-4 until all vertices are visited.

### Implementation:

```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Iterative DFS
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=" ")
            stack.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

# Example usage
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 4],
    3: [1, 4],
    4: [2, 3]
}

print("Recursive DFS starting from vertex 0:")
dfs(graph, 0)

print("\nIterative DFS starting from vertex 0:")
dfs_iterative(graph, 0)
```

### Time Complexity:
- O(V + E), where V is the number of vertices and E is the number of edges.

### Space Complexity:
- O(V) for the recursive call stack or the stack in iterative implementation.

### Applications of DFS:
1. Topological Sorting
2. Detecting cycles in a graph
3. Path finding (e.g., maze solving)
4. Finding strongly connected components
5. Generating mazes

## Comparison of BFS and DFS

| Aspect | BFS | DFS |
|--------|-----|-----|
| Data Structure | Queue | Stack (or Recursion) |
| Space Complexity | O(V) - can be high for wide graphs | O(h) where h is the height of the tree - can be high for deep graphs |
| Completeness | Complete (finds solution if it exists) | Not complete (can get stuck in infinite path) |
| Path Optimality | Optimal for unweighted graphs | Not guaranteed to be optimal |
| Use Case | Shortest path, closer nodes | Path exists, topological ordering |

## Exercise

1. Implement a function to find the shortest path between two vertices in an unweighted graph using BFS.
2. Create a method to detect a cycle in a directed graph using DFS.
3. Implement a function to find all connected components in an undirected graph using either BFS or DFS.

## Summary

Today, we explored two fundamental graph traversal algorithms: Breadth-First Search (BFS) and Depth-First Search (DFS). We implemented both algorithms and discussed their characteristics, time and space complexities, and applications.

Understanding these traversal techniques is crucial for solving a wide range of graph problems and forms the foundation for more advanced graph algorithms. As we progress through this challenge, you'll find BFS and DFS being used as building blocks for solving complex graph-related problems.

Tomorrow, we'll dive into shortest path algorithms, starting with Dijkstra's algorithm. Stay tuned!

