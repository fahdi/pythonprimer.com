---
title: "Day 19: Graph Representations"
weight: 19
menu:
  main:
    parent: "Algorithms"
    weight: 19
---

# Graph Representations

Welcome to Day 19 of our 60 Days of Coding Algorithm Challenge! Today, we'll dive deeper into various ways of representing graphs in code, exploring their pros and cons, and discussing when to use each representation.

## Overview of Graph Representations

There are several ways to represent a graph in computer memory. The choice of representation depends on the type of graph and the algorithms you plan to use. The most common representations are:

1. Adjacency Matrix
2. Adjacency List
3. Edge List
4. Incidence Matrix

Let's explore each of these in detail.

## 1. Adjacency Matrix

An adjacency matrix is a 2D array of size V x V where V is the number of vertices in the graph. The entry matrix[i][j] is 1 (or the edge weight for weighted graphs) if there is an edge from vertex i to vertex j, and 0 otherwise.

### Implementation:

```python
class GraphMatrix:
    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed
        self.matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    def add_edge(self, v1, v2, weight=1):
        self.matrix[v1][v2] = weight
        if not self.directed:
            self.matrix[v2][v1] = weight

    def remove_edge(self, v1, v2):
        self.matrix[v1][v2] = 0
        if not self.directed:
            self.matrix[v2][v1] = 0

    def print_matrix(self):
        for row in self.matrix:
            print(row)

# Example usage
g = GraphMatrix(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.print_matrix()
```

### Pros:
- Constant time O(1) to check if there is an edge between two vertices
- Simple for undirected graphs
- Efficient for dense graphs

### Cons:
- Uses O(V^2) space, which can be wasteful for sparse graphs
- O(V^2) time to add or remove a vertex

## 2. Adjacency List

An adjacency list represents a graph as an array of lists. The array index corresponds to a vertex, and each element in its list represents the vertices that form an edge with it.

### Implementation:

```python
from collections import defaultdict

class GraphList:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def add_edge(self, v1, v2):
        self.graph[v1].append(v2)
        if not self.directed:
            self.graph[v2].append(v1)

    def remove_edge(self, v1, v2):
        self.graph[v1].remove(v2)
        if not self.directed:
            self.graph[v2].remove(v1)

    def print_list(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")

# Example usage
g = GraphList()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.print_list()
```

### Pros:
- Space-efficient for sparse graphs
- Faster to iterate over all edges
- Efficient addition and removal of edges

### Cons:
- Slower to check if there is an edge between two vertices (O(E) in the worst case)
- More complex to implement compared to adjacency matrix

## 3. Edge List

An edge list is a representation where we store the graph simply as an unordered list of edges. Each edge is a pair of vertices.

### Implementation:

```python
class GraphEdgeList:
    def __init__(self, directed=False):
        self.edges = []
        self.directed = directed

    def add_edge(self, v1, v2):
        self.edges.append((v1, v2))
        if not self.directed:
            self.edges.append((v2, v1))

    def remove_edge(self, v1, v2):
        self.edges.remove((v1, v2))
        if not self.directed:
            self.edges.remove((v2, v1))

    def print_edges(self):
        print(self.edges)

# Example usage
g = GraphEdgeList()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.print_edges()
```

### Pros:
- Simple and intuitive
- Space-efficient for sparse graphs
- Efficient for algorithms that work directly with edges

### Cons:
- Inefficient for checking if there's an edge between two vertices or finding adjacent vertices

## 4. Incidence Matrix

An incidence matrix is a 2D array of size V x E where V is the number of vertices and E is the number of edges. For each column representing an edge, we mark the vertices it connects with 1 (or -1 and 1 for directed graphs).

### Implementation:

```python
class GraphIncidenceMatrix:
    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed
        self.matrix = []
        self.edge_count = 0

    def add_edge(self, v1, v2):
        column = [0] * self.num_vertices
        column[v1] = 1
        column[v2] = -1 if self.directed else 1
        self.matrix.append(column)
        self.edge_count += 1

    def print_matrix(self):
        for i in range(self.num_vertices):
            row = [self.matrix[j][i] for j in range(self.edge_count)]
            print(row)

# Example usage
g = GraphIncidenceMatrix(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.print_matrix()
```

### Pros:
- Can represent multigraphs (graphs with multiple edges between the same vertices)
- Useful for some graph algorithms and in certain mathematical treatments of graphs

### Cons:
- Not as commonly used as adjacency matrix or adjacency list
- Can be space-inefficient, especially for sparse graphs

## Choosing the Right Representation

The choice of graph representation depends on several factors:

1. **Density of the graph**: For dense graphs, adjacency matrix might be preferred. For sparse graphs, adjacency list or edge list are more space-efficient.

2. **Types of operations**: If you need to quickly check if there's an edge between two vertices, adjacency matrix is better. If you need to iterate over all edges quickly, adjacency list or edge list might be preferable.

3. **Type of graph**: For weighted graphs, adjacency matrix or a modified adjacency list can be used. For multigraphs, incidence matrix or a modified adjacency list might be suitable.

4. **Memory constraints**: If memory is a concern, consider using adjacency list for sparse graphs.

5. **Algorithmic requirements**: Some algorithms work better with certain representations. For example, Kruskal's algorithm for minimum spanning trees works well with an edge list.

## Exercise

1. Implement a function to convert between adjacency matrix and adjacency list representations.
2. Create a method to find all isolated vertices (vertices with no incoming or outgoing edges) in a graph, using each of the representations we've discussed.
3. Implement a function to check if a graph is bipartite, using both adjacency matrix and adjacency list representations. Compare the time complexity of your implementations.

## Summary

Today, we explored various ways to represent graphs in code, including adjacency matrices, adjacency lists, edge lists, and incidence matrices. We discussed the pros and cons of each representation and provided guidelines for choosing the right representation based on the specific requirements of your problem.

Understanding these different representations is crucial for implementing graph algorithms efficiently and solving graph-related problems effectively. As we progress through this challenge, we'll use these representations to implement various graph algorithms.

Tomorrow, we'll dive into graph traversal algorithms, starting with Depth-First Search (DFS) and Breadth-First Search (BFS). Stay tuned!
