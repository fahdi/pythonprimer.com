---
title: "Day 14: Binary Trees"
weight: 14
menu:
    main:
        parent: "Algorithms"
        weight: 14
---

# Binary Trees

Welcome to Day 14 of our 60 Days of Coding Algorithm Challenge! Today, we'll dive deep into Binary Trees, a fundamental data structure in computer science and a specific type of tree we introduced yesterday.

## What is a Binary Tree?

A Binary Tree is a tree data structure in which each node has at most two children, referred to as the left child and the right child. This restriction on the number of children makes binary trees particularly useful in various applications and algorithms.

## Properties of Binary Trees

1. The maximum number of nodes at level 'l' of a binary tree is 2^l.
2. The maximum number of nodes in a binary tree of height 'h' is 2^(h+1) - 1.
3. In a binary tree with N nodes, the minimum possible height or the minimum number of levels is log2(N+1) - 1.
4. A binary tree with L leaves has at least log2(L) + 1 levels.

## Types of Binary Trees

1. **Full Binary Tree**: Every node has 0 or 2 children.
2. **Complete Binary Tree**: All levels are completely filled except possibly the last level, which is filled from left to right.
3. **Perfect Binary Tree**: All internal nodes have two children and all leaves are at the same level.
4. **Balanced Binary Tree**: The height of the left and right subtrees of every node differs by at most one.
5. **Degenerate (or Pathological) Tree**: Every internal node has only one child.

## Implementing a Binary Tree in Python

Let's implement a basic Binary Tree structure:

```python
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = BinaryTreeNode(root_value)

    def insert_left(self, node, value):
        if node is None:
            return BinaryTreeNode(value)
        node.left = self.insert_left(node.left, value)
        return node

    def insert_right(self, node, value):
        if node is None:
            return BinaryTreeNode(value)
        node.right = self.insert_right(node.right, value)
        return node

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.value)
            self.print_tree(node.left, level + 1)

# Example usage
tree = BinaryTree(1)
tree.root.left = BinaryTreeNode(2)
tree.root.right = BinaryTreeNode(3)
tree.root.left.left = BinaryTreeNode(4)
tree.root.left.right = BinaryTreeNode(5)

print("Binary Tree Structure:")
tree.print_tree(tree.root)
```

## Binary Tree Traversals

There are three main types of depth-first traversals for binary trees:

1. **Inorder Traversal** (Left, Root, Right)
2. **Preorder Traversal** (Root, Left, Right)
3. **Postorder Traversal** (Left, Right, Root)

Let's implement these traversals:

```python
class BinaryTree:
    # ... (previous methods remain the same)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=' ')
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node:
            print(node.value, end=' ')
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.value, end=' ')

# Example usage
tree = BinaryTree(1)
tree.root.left = BinaryTreeNode(2)
tree.root.right = BinaryTreeNode(3)
tree.root.left.left = BinaryTreeNode(4)
tree.root.left.right = BinaryTreeNode(5)

print("Inorder Traversal:")
tree.inorder_traversal(tree.root)
print("\nPreorder Traversal:")
tree.preorder_traversal(tree.root)
print("\nPostorder Traversal:")
tree.postorder_traversal(tree.root)
```

## Level Order Traversal (Breadth-First Search)

We can also perform a level order traversal, which visits nodes level by level from left to right:

```python
from collections import deque

class BinaryTree:
    # ... (previous methods remain the same)

    def level_order_traversal(self):
        if not self.root:
            return
        
        queue = deque([self.root])
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                print(node.value, end=' ')
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print()  # New line for each level

# Example usage
tree = BinaryTree(1)
tree.root.left = BinaryTreeNode(2)
tree.root.right = BinaryTreeNode(3)
tree.root.left.left = BinaryTreeNode(4)
tree.root.left.right = BinaryTreeNode(5)

print("Level Order Traversal:")
tree.level_order_traversal()
```

## Common Binary Tree Operations

1. **Finding the Height of a Binary Tree**:

```python
def height(node):
    if not node:
        return 0
    left_height = height(node.left)
    right_height = height(node.right)
    return max(left_height, right_height) + 1
```

2. **Counting Nodes in a Binary Tree**:

```python
def count_nodes(node):
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)
```

3. **Checking if a Binary Tree is Balanced**:

```python
def is_balanced(node):
    def check_balance(node):
        if not node:
            return 0
        left = check_balance(node.left)
        right = check_balance(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1

    return check_balance(node) != -1
```

## Applications of Binary Trees

1. **Expression Trees**: For representing and evaluating arithmetic expressions.
2. **Huffman Coding Trees**: Used in data compression algorithms.
3. **Binary Search Trees**: For efficient searching and sorting.
4. **Priority Queues**: Heap is a binary tree-based data structure used in priority queues.
5. **Syntax Trees**: In compilers to represent the structure of program code.

## Time Complexity

For a balanced binary tree:
- Insertion: O(log n)
- Deletion: O(log n)
- Search: O(log n)

For an unbalanced binary tree, these operations can degrade to O(n) in the worst case.

## Exercise

1. Implement a function to find the lowest common ancestor of two nodes in a binary tree.
2. Create a method to check if a binary tree is a full binary tree.
3. Implement a function to find the diameter of a binary tree (the longest path between any two nodes).

## Summary

Today, we explored Binary Trees in depth, including their properties, types, implementations, and common operations. Binary Trees are fundamental to many advanced data structures and algorithms, and understanding them thoroughly is crucial for solving complex problems efficiently.

Binary Trees form the basis for more specialized tree structures like Binary Search Trees and Heaps, which we'll explore in the coming days. The traversal techniques and operations we've learned today will be invaluable as we delve deeper into tree-based data structures and algorithms.

Tomorrow, we'll focus on Binary Search Trees, a special type of binary tree that maintains a specific ordering of nodes for efficient searching and sorting operations. Stay tuned!