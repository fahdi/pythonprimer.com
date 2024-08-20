---
title: "Day 22: Minimum Spanning Trees"
weight: 22
menu:
  main:
    parent: "Algorithms"
    weight: 22
---

# Minimum Spanning Trees

Welcome to Day 22 of our 60 Days of Coding Algorithm Challenge! Today, we'll explore Minimum Spanning Trees (MST) and two fundamental algorithms for finding them: Kruskal's Algorithm and Prim's Algorithm. These algorithms are crucial for solving problems involving network design, clustering, and other optimization tasks.

## Introduction to Minimum Spanning Trees

A Minimum Spanning Tree of an undirected, connected, weighted graph is a tree that spans all vertices of the graph with the minimum total edge weight. In other words, it's a subset of the edges that forms a tree including every vertex, where the total weight of all the edges in the tree is minimized.

Key properties of a Minimum Spanning Tree:
1. It includes all vertices of the graph.
2. It forms a tree (no cycles).
3. Among all possible spanning trees, it has the minimum total edge weight.

## Kruskal's Algorithm

Kruskal's algorithm builds the minimum spanning tree by adding edges one by one, always choosing the edge with the lowest weight that doesn't create a cycle.

### Algorithm:

1. Sort all edges in non-decreasing order of their weight.
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If not, include this edge. Otherwise, discard it.
3. Repeat step 2 until there are (V-1) edges in the spanning tree, where V is the number of vertices.

### Implementation:

```python
class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

def kruskal_mst(graph):
    edges = [(w, u, v) for u in graph for v, w in graph[u].items()]
    edges.sort()
    vertices = list(graph.keys())
    ds = DisjointSet(vertices)
    mst = []

    for w, u, v in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, w))

    return mst

# Example usage
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
    'E': {'C': 10, 'D': 2, 'F': 3},
    'F': {'D': 6, 'E': 3}
}

mst = kruskal_mst(graph)
print("Minimum Spanning Tree edges:")
for edge in mst:
    print(f"{edge[0]} -- {edge[1]} : {edge[2]}")
```

### Time Complexity:
- O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices.

### Space Complexity:
- O(E + V)

## Prim's Algorithm

Prim's algorithm builds the minimum spanning tree by adding vertices one by one to the growing spanning tree.

### Algorithm:

1. Initialize a tree with a single vertex, chosen arbitrarily from the graph.
2. Grow the tree by one edge: of the edges that connect the tree to vertices not yet in the tree, find the minimum-weight edge, and transfer it to the tree.
3. Repeat step 2 until all vertices are in the tree.

### Implementation:

```python
import heapq

def prim_mst(graph):
    start_vertex = next(iter(graph))
    mst = []
    visited = set([start_vertex])
    edges = [(w, start_vertex, v) for v, w in graph[start_vertex].items()]
    heapq.heapify(edges)

    while edges:
        w, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, w))
            for next_v, next_w in graph[v].items():
                if next_v not in visited:
                    heapq.heappush(edges, (next_w, v, next_v))

    return mst

# Example usage
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
    'E': {'C': 10, 'D': 2, 'F': 3},
    'F': {'D': 6, 'E': 3}
}

mst = prim_mst(graph)
print("Minimum Spanning Tree edges:")
for edge in mst:
    print(f"{edge[0]} -- {edge[1]} : {edge[2]}")
```

### Time Complexity:
- O((V + E) log V) with a binary heap implementation
- O(V^2) with a naive implementation

### Space Complexity:
- O(V)

## Comparison of Kruskal's and Prim's Algorithms

| Aspect | Kruskal's Algorithm | Prim's Algorithm |
|--------|---------------------|-------------------|
| Approach | Edge-based | Vertex-based |
| Best for | Sparse graphs | Dense graphs |
| Time Complexity | O(E log E) | O((V + E) log V) with binary heap |
| Space Complexity | O(E + V) | O(V) |
| Implementation | Simpler with sorting | Requires priority queue |

## Applications of Minimum Spanning Trees

1. **Network Design**: Designing low-cost computer or telecommunications networks.
2. **Approximation Algorithms**: For NP-hard problems like the traveling salesman problem.
3. **Cluster Analysis**: In data mining and machine learning.
4. **Image Segmentation**: In computer vision and image processing.
5. **Taxonomy Creation**: In biology for creating evolutionary trees.

## Exercise

1. Implement a function to find the maximum spanning tree of a graph using either Kruskal's or Prim's algorithm.
2. Modify Kruskal's algorithm to handle graphs where some edges have equal weights.
3. Implement a variation of Prim's algorithm that finds the minimum spanning forest in a disconnected graph.

## Summary

Today, we explored Minimum Spanning Trees and two fundamental algorithms for finding them: Kruskal's Algorithm and Prim's Algorithm. We implemented both algorithms and discussed their characteristics, time and space complexities, and applications.

Understanding these algorithms is crucial for solving a wide range of optimization problems, especially those involving network design and clustering. As we progress through this challenge, you'll find these algorithms being used as building blocks for solving more complex graph-related problems.

Tomorrow, we'll dive into hash tables, a fundamental data structure that provides efficient insertion, deletion, and lookup operations. Stay tuned!

