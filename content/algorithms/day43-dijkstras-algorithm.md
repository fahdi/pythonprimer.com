---
title: "Day 43: Dijkstra's Algorithm"
weight: 43
menu:
  main:
    parent: "Algorithms"
    weight: 43
---

# Dijkstra's Algorithm

Welcome to Day 43 of our 60 Days of Coding Algorithm Challenge! Today, we'll explore Dijkstra's Algorithm, a fundamental graph algorithm used for finding the shortest paths between nodes in a graph.

## What is Dijkstra's Algorithm?

Dijkstra's Algorithm is a greedy algorithm that solves the single-source shortest path problem for a graph with non-negative edge weights. It was conceived by computer scientist Edsger W. Dijkstra in 1956 and published three years later.

## How Dijkstra's Algorithm Works

1. Initialize distances to all vertices as infinite and distance to the source as 0.
2. Create a set of unvisited vertices.
3. For the current vertex, consider all its unvisited neighbors and calculate their tentative distances.
4. When we are done considering all neighbors of the current vertex, mark it as visited and remove it from the unvisited set.
5. If the destination vertex has been marked visited, we're done.
6. Otherwise, select the unvisited vertex with the smallest tentative distance, and repeat from step 3.

## Implementation

Let's implement Dijkstra's Algorithm in Python:

```python
import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    previous = {vertex: None for vertex in graph}

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        # If we have already found a shorter path, continue
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous

def shortest_path(graph, start, end):
    distances, previous = dijkstra(graph, start)
    path = []
    current_vertex = end
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = previous[current_vertex]
    path.reverse()
    return path, distances[end]

# Example usage
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
    'E': {'C': 10, 'D': 2, 'F': 3},
    'F': {'D': 6, 'E': 3}
}

start = 'A'
end = 'F'
path, distance = shortest_path(graph, start, end)
print(f"Shortest path from {start} to {end}: {' -> '.join(path)}")
print(f"Total distance: {distance}")
```

## Time Complexity

The time complexity of Dijkstra's algorithm depends on the data structure used for the priority queue:

- Using a binary heap: O((V + E) log V), where V is the number of vertices and E is the number of edges.
- Using a Fibonacci heap: O(E + V log V)

## Space Complexity

O(V), where V is the number of vertices in the graph.

## Advantages of Dijkstra's Algorithm

1. Efficiently finds the shortest path in weighted graphs
2. Works well for graphs with non-negative edge weights
3. Can be used to find shortest paths from a single source to all other vertices

## Limitations

1. Does not work with graphs containing negative edge weights
2. May not find the shortest path in graphs with negative cycles

## Applications

1. GPS and navigation systems
2. Network routing protocols
3. Social network analysis
4. Robotics and path planning

## Variations and Optimizations

1. Bidirectional Dijkstra's algorithm: Searches from both the start and end vertices simultaneously
2. A* algorithm: Uses heuristics to guide the search towards the goal
3. Johnson's algorithm: For graphs with negative edge weights but no negative cycles

## Exercise

1. Implement Dijkstra's algorithm using an adjacency matrix instead of an adjacency list.
2. Modify the algorithm to handle directed graphs.
3. Implement a variation of Dijkstra's algorithm that finds the path with the maximum flow capacity between two vertices in a flow network.

## Summary

Today, we explored Dijkstra's Algorithm, a fundamental graph algorithm for finding shortest paths. We implemented the algorithm, discussed its time and space complexity, and looked at its advantages, limitations, and real-world applications.

Understanding Dijkstra's Algorithm is crucial for solving many graph-related problems and has wide-ranging applications in computer science and beyond.
