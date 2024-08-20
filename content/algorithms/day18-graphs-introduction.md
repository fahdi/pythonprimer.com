---
title: "Day 18: Introduction to Graphs"
weight: 18
menu:
  main:
    parent: "Algorithms"
    weight: 18
---

# Introduction to Graphs

Welcome to Day 18 of our 60 Days of Coding Algorithm Challenge! Today, we'll dive into the world of graphs, a versatile and powerful data structure used to represent relationships between entities.

## What is a Graph?

A graph is a non-linear data structure consisting of nodes (or vertices) and edges. The nodes are the entities we want to represent, and the edges are the relationships or connections between these entities.

Formally, a graph G is an ordered pair of a set V of vertices and a set E of edges, written as G = (V, E).

## Basic Graph Terminology

1. **Vertex (Node)**: A fundamental unit of which graphs are formed.
2. **Edge**: A connection between two vertices in a graph.
3. **Adjacent Vertices**: Two vertices are said to be adjacent if there's an edge connecting them.
4. **Degree of a Vertex**: The number of edges connected to a vertex.
5. **Path**: A sequence of vertices where each adjacent pair is connected by an edge.
6. **Cycle**: A path that starts and ends at the same vertex.

## Types of Graphs

1. **Undirected Graph**: Edges have no direction.
2. **Directed Graph (Digraph)**: Edges have directions.
3. **Weighted Graph**: Edges have weights or costs associated with them.
4. **Unweighted Graph**: All edges are considered to have equal weight.
5. **Connected Graph**: There is a path between every pair of vertices.
6. **Disconnected Graph**: There are some vertices without a path between them.
7. **Cyclic Graph**: The graph has at least one cycle.
8. **Acyclic Graph**: The graph has no cycles.

## Graph Representations

There are two primary ways to represent a graph in code:

1. **Adjacency Matrix**: A 2D array where matrix[i][j] represents an edge from vertex i to vertex j.
2. **Adjacency List**: An array of lists, where each list describes the set of neighbors of a particular vertex.

Let's implement both representations:

```python
class Graph:
    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed
        self.matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
        self.list = {i: [] for i in range(num_vertices)}

    def add_edge(self, v1, v2, weight=1):
        self.matrix[v1][v2] = weight
        self.list[v1].append(v2)
        if not self.directed:
            self.matrix[v2][v1] = weight
            self.list[v2].append(v1)

    def remove_edge(self, v1, v2):
        self.matrix[v1][v2] = 0
        self.list[v1].remove(v2)
        if not self.directed:
            self.matrix[v2][v1] = 0
            self.list[v2].remove(v1)

    def print_matrix(self):
        for row in self.matrix:
            print(row)

    def print_list(self):
        for vertex in self.list:
            print(f"{vertex}: {self.list[vertex]}")

# Example usage
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

print("Adjacency Matrix:")
g.print_matrix()
print("\nAdjacency List:")
g.print_list()
```

## Basic Graph Operations

1. **Adding a vertex**: Create a new entry in the adjacency list or expand the adjacency matrix.
2. **Adding an edge**: Update the adjacency list or matrix to reflect the new connection.
3. **Removing a vertex**: Remove the vertex's entry and all references to it.
4. **Removing an edge**: Update the adjacency list or matrix to remove the connection.
5. **Checking if two vertices are adjacent**: Check the corresponding entry in the list or matrix.

## Graph Traversal Algorithms

The two fundamental algorithms for traversing a graph are:

1. **Depth-First Search (DFS)**: Explores as far as possible along each branch before backtracking.
2. **Breadth-First Search (BFS)**: Explores all the neighboring vertices at the present depth before moving to vertices at the next depth level.

We'll cover these in detail in the coming days.

## Applications of Graphs

1. **Social Networks**: Representing relationships between people.
2. **Map/GPS Navigation**: Finding shortest paths between locations.
3. **Computer Networks**: Modeling network topology and routing.
4. **Recommendation Systems**: Suggesting products or content based on user relationships.
5. **Search Engine Indexing**: Web crawling and pagerank algorithms.
6. **Dependency Resolution**: Managing dependencies in software projects.

## Time Complexity

The time complexity of graph operations depends on the representation:

For Adjacency Matrix:
- Adding/Removing an edge: O(1)
- Checking if two vertices are adjacent: O(1)
- Finding all adjacent vertices: O(V)

For Adjacency List:
- Adding an edge: O(1)
- Removing an edge: O(E)
- Checking if two vertices are adjacent: O(E)
- Finding all adjacent vertices: O(1)

Where V is the number of vertices and E is the number of edges.

## Exercise

1. Implement a function to check if a given graph is connected.
2. Create a method to find the degree of a vertex in both directed and undirected graphs.
3. Implement a function to detect if a cycle exists in a directed graph.

## Summary

Today, we introduced graphs, a powerful and versatile data structure used to represent relationships between entities. We covered basic graph terminology, types of graphs, and different ways to represent graphs in code. We also discussed basic graph operations and briefly touched on traversal algorithms.

Understanding graphs is crucial for solving a wide range of problems in computer science and real-world applications. As we progress through this challenge, we'll explore more advanced graph algorithms and their applications.

Tomorrow, we'll dive deeper into graph representations and discuss the pros and cons of different approaches. Stay tuned!
