---
title: "Day 21: Shortest Path Algorithms"
weight: 21
menu:
  main:
    parent: "Algorithms"
    weight: 21
---

# Shortest Path Algorithms

Welcome to Day 21 of our 60 Days of Coding Algorithm Challenge! Today, we'll dive into shortest path algorithms, focusing on two fundamental algorithms: Dijkstra's Algorithm and the Bellman-Ford Algorithm. These algorithms are crucial for solving problems involving finding the most efficient path between nodes in a graph.

## Introduction to Shortest Path Problems

The shortest path problem is about finding a path between two vertices in a graph such that the sum of the weights of its constituent edges is minimized. This problem has numerous real-world applications, including:

1. GPS Navigation systems
2. Network routing protocols
3. Flight itinerary planning
4. Robot motion planning

## Dijkstra's Algorithm

Dijkstra's algorithm finds the shortest path from a single source vertex to all other vertices in a weighted graph with non-negative edge weights.

### Algorithm:

1. Initialize distances to all vertices as infinite and distance to the source as 0.
2. Create a set of unvisited vertices.
3. For the current vertex, consider all its unvisited neighbors and calculate their tentative distances.
4. When we are done considering all neighbors of the current vertex, mark it as visited and remove it from the unvisited set.
5. If the destination vertex has been marked visited, we're done.
6. Otherwise, select the unvisited vertex with the smallest tentative distance, and repeat from step 3.

### Implementation:

```python
import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Example usage
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
    'E': {'C': 10, 'D': 2, 'F': 3},
    'F': {'D': 6, 'E': 3}
}

start_vertex = 'A'
shortest_distances = dijkstra(graph, start_vertex)
print(f"Shortest distances from {start_vertex}: {shortest_distances}")
```

### Time Complexity:
- O((V + E) log V) with a binary heap implementation
- O(V^2) with a naive implementation

### Space Complexity:
- O(V)

## Bellman-Ford Algorithm

The Bellman-Ford algorithm also finds the shortest path from a single source vertex to all other vertices, but it can handle graphs with negative edge weights and detect negative cycles.

### Algorithm:

1. Initialize distances to all vertices as infinite and distance to the source as 0.
2. Repeat V-1 times (where V is the number of vertices):
   - For each edge (u, v) with weight w:
     - If distance[u] + w < distance[v], update distance[v] to distance[u] + w
3. Check for negative-weight cycles:
   - For each edge (u, v) with weight w:
     - If distance[u] + w < distance[v], a negative-weight cycle exists

### Implementation:

```python
def bellman_ford(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex].items():
                if distances[vertex] + weight < distances[neighbor]:
                    distances[neighbor] = distances[vertex] + weight
    
    # Check for negative-weight cycles
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            if distances[vertex] + weight < distances[neighbor]:
                print("Graph contains a negative-weight cycle")
                return None
    
    return distances

# Example usage
graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}

start_vertex = 'A'
shortest_distances = bellman_ford(graph, start_vertex)
if shortest_distances:
    print(f"Shortest distances from {start_vertex}: {shortest_distances}")
```

### Time Complexity:
- O(VE), where V is the number of vertices and E is the number of edges

### Space Complexity:
- O(V)

## Comparison of Dijkstra's and Bellman-Ford Algorithms

| Aspect | Dijkstra's Algorithm | Bellman-Ford Algorithm |
|--------|----------------------|------------------------|
| Edge Weights | Non-negative only | Can handle negative weights |
| Negative Cycles | Cannot detect | Can detect |
| Time Complexity | O((V + E) log V) with binary heap | O(VE) |
| Use Case | Faster for graphs with non-negative weights | Necessary for graphs with negative weights |

## Applications

1. **Network Routing**: Both algorithms are used in routing protocols to find the most efficient path for data packets.
2. **GPS Systems**: Dijkstra's algorithm is commonly used in GPS navigation to find the shortest route.
3. **Social Networks**: Finding the shortest connection between two people.
4. **Currency Exchange**: Bellman-Ford can be used to detect arbitrage opportunities in currency exchange.

## Exercise

1. Implement a function to find the shortest path (not just the distance) between two vertices using Dijkstra's algorithm.
2. Modify the Bellman-Ford algorithm to print the negative cycle if one exists.
3. Implement Floyd-Warshall algorithm for finding shortest paths between all pairs of vertices in a weighted graph.

## Summary

Today, we explored two fundamental shortest path algorithms: Dijkstra's Algorithm and the Bellman-Ford Algorithm. We implemented both algorithms and discussed their characteristics, time and space complexities, and applications.

Understanding these algorithms is crucial for solving a wide range of graph problems, especially those involving optimization of paths or routes. As we progress through this challenge, you'll find these algorithms being used as building blocks for solving more complex graph-related problems.

Tomorrow, we'll dive into minimum spanning tree algorithms, including Kruskal's and Prim's algorithms. Stay tuned!

