---
title: "Day 38: Floyd-Warshall Algorithm"
weight: 38
menu:
  main:
    parent: "Algorithms"
    weight: 38
---

# Floyd-Warshall Algorithm

Welcome to Day 38 of our 60 Days of Coding Algorithm Challenge! Today, we'll explore the Floyd-Warshall algorithm, a powerful algorithm for finding the shortest paths between all pairs of vertices in a weighted graph.

## What is the Floyd-Warshall Algorithm?

The Floyd-Warshall algorithm is an algorithm for finding shortest paths in a weighted graph with positive or negative edge weights (but with no negative cycles). Unlike Dijkstra's algorithm, which finds the shortest path from a single source to all other vertices, Floyd-Warshall finds the shortest paths between all pairs of vertices.

## How Does It Work?

The algorithm works by iteratively improving an estimate on the shortest path between two vertices, until the estimate is optimal. It does this by considering all possible intermediate vertices between each pair of vertices.

## Implementing Floyd-Warshall Algorithm

Here's an implementation of the Floyd-Warshall algorithm:

```python
def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]  # Create a copy of the graph
    
    # Initialize the distance matrix
    for i in range(n):
        for j in range(n):
            if i != j and dist[i][j] == 0:
                dist[i][j] = float('inf')
    
    # Main algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

# Example usage
graph = [
    [0, 5, float('inf'), 10],
    [float('inf'), 0, 3, float('inf')],
    [float('inf'), float('inf'), 0, 1],
    [float('inf'), float('inf'), float('inf'), 0]
]

result = floyd_warshall(graph)
for row in result:
    print(row)
```

## Time and Space Complexity

- Time Complexity: O(V^3), where V is the number of vertices in the graph.
- Space Complexity: O(V^2) to store the distance matrix.

## Detecting Negative Cycles

The Floyd-Warshall algorithm can also be used to detect negative cycles in the graph. If after running the algorithm, any diagonal element in the distance matrix is negative, then there exists a negative cycle in the graph.

```python
def has_negative_cycle(dist):
    n = len(dist)
    for i in range(n):
        if dist[i][i] < 0:
            return True
    return False

# Check for negative cycles
if has_negative_cycle(result):
    print("Graph contains a negative cycle")
else:
    print("No negative cycle detected")
```

## Reconstructing Paths

We can modify the algorithm to not only find the shortest distances but also reconstruct the paths:

```python
def floyd_warshall_with_path(graph):
    n = len(graph)
    dist = [row[:] for row in graph]
    next = [[j if graph[i][j] != float('inf') else None for j in range(n)] for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i != j and dist[i][j] == 0:
                dist[i][j] = float('inf')
                next[i][j] = None
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next[i][j] = next[i][k]
    
    return dist, next

def reconstruct_path(next, u, v):
    if next[u][v] is None:
        return []
    path = [u]
    while u != v:
        u = next[u][v]
        path.append(u)
    return path

# Example usage
dist, next = floyd_warshall_with_path(graph)
print("Shortest path from 0 to 3:", reconstruct_path(next, 0, 3))
```

## Applications of Floyd-Warshall Algorithm

1. Finding the shortest paths in a weighted graph
2. Inversion of real matrices
3. Fast computation of Pathfinder networks
4. Finding the transitive closure of a graph
5. Finding a regular expression denoting the regular language accepted by a finite automaton

## Exercise

1. Implement a version of the Floyd-Warshall algorithm that can handle graphs with no path between some pairs of vertices (represented by infinity).

2. Modify the algorithm to find the maximum flow between all pairs of vertices in a flow network.

3. Use the Floyd-Warshall algorithm to solve the "All-Pairs Shortest Path" problem for a real-world scenario, such as finding the shortest routes between all pairs of cities on a map.

## Summary

Today, we explored the Floyd-Warshall algorithm, a powerful method for finding shortest paths between all pairs of vertices in a weighted graph. We implemented the basic algorithm, added negative cycle detection, and showed how to reconstruct the actual paths.

The Floyd-Warshall algorithm is particularly useful when we need to find shortest paths between all pairs of vertices, or when the graph may contain negative edge weights (but no negative cycles).

Tomorrow, we'll dive into the world of string algorithms, starting with the Knuth-Morris-Pratt (KMP) algorithm for pattern matching. Stay tuned!
