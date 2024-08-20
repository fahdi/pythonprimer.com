---
title: "Day 15: Binary Search Trees"
weight: 15
menu:
  main:
    parent: "Algorithms"
    weight: 15
---

# Binary Search Trees

Welcome to Day 15 of our 60 Days of Coding Algorithm Challenge! Today, we'll dive into Binary Search Trees (BST), a powerful data structure that combines the efficiency of binary search with the flexibility of a linked data structure.

## What is a Binary Search Tree?

A Binary Search Tree is a binary tree with the following properties:
1. The left subtree of a node contains only nodes with keys less than the node's key.
2. The right subtree of a node contains only nodes with keys greater than the node's key.
3. Both the left and right subtrees must also be binary search trees.

These properties make BSTs efficient for search, insertion, and deletion operations.

## Implementing a Binary Search Tree in Python

Let's implement a basic Binary Search Tree:

```python
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return BSTNode(key)
        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        else:
            root.right = self._insert_recursive(root.right, key)
        return root

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search_recursive(root.left, key)
        return self._search_recursive(root.right, key)

    def inorder_traversal(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, root):
        if root:
            self._inorder_recursive(root.left)
            print(root.key, end=" ")
            self._inorder_recursive(root.right)

# Example usage
bst = BinarySearchTree()
keys = [50, 30, 70, 20, 40, 60, 80]

for key in keys:
    bst.insert(key)

print("Inorder traversal of the BST:")
bst.inorder_traversal()
```

## BST Operations

### 1. Insertion

The insertion operation in a BST maintains the BST property:
- If the tree is empty, create a new node and set it as the root.
- Otherwise, compare the key with the root:
    - If the key is less than the root, insert it into the left subtree.
    - If the key is greater than the root, insert it into the right subtree.
- Repeat this process recursively until you find an empty spot.

Time Complexity: O(h), where h is the height of the tree. In a balanced BST, this is O(log n).

### 2. Search

Searching in a BST is efficient due to its structure:
- Start at the root.
- If the key matches the current node, return the node.
- If the key is less than the current node, search in the left subtree.
- If the key is greater than the current node, search in the right subtree.
- Repeat until you find the key or reach a leaf node.

Time Complexity: O(h), where h is the height of the tree. In a balanced BST, this is O(log n).

### 3. Deletion

Deleting a node from a BST is more complex and involves three cases:
1. Node to be deleted is a leaf: Simply remove it.
2. Node has one child: Replace the node with its child.
3. Node has two children: Find the inorder successor (minimum value in the right subtree), replace the node's value with the successor's value, and delete the successor.

Let's implement the deletion operation:

```python
class BinarySearchTree:
    # ... (previous methods remain the same)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children
            root.key = self._min_value(root.right)
            root.right = self._delete_recursive(root.right, root.key)

        return root

    def _min_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.key

# Example usage
bst = BinarySearchTree()
keys = [50, 30, 70, 20, 40, 60, 80]

for key in keys:
    bst.insert(key)

print("Original BST:")
bst.inorder_traversal()

bst.delete(30)
print("\nBST after deleting 30:")
bst.inorder_traversal()
```

Time Complexity: O(h), where h is the height of the tree. In a balanced BST, this is O(log n).

## Balancing Binary Search Trees

The efficiency of BST operations depends on the height of the tree. In the worst case, when the tree becomes skewed (essentially a linked list), the time complexity degrades to O(n).

To maintain efficiency, we use self-balancing BSTs such as:
1. AVL Trees
2. Red-Black Trees

These structures automatically keep the tree balanced after insertions and deletions, ensuring O(log n) time complexity for basic operations.

## Applications of Binary Search Trees

1. Implementing associative arrays (dictionaries)
2. Database indexing
3. Implementing priority queues
4. Syntax trees in compilers
5. Searching algorithms

## Exercise

1. Implement a function to find the kth smallest element in a BST.
2. Create a method to check if a binary tree is a valid BST.
3. Implement a function to find the lowest common ancestor of two nodes in a BST.

## Summary

Binary Search Trees are powerful data structures that provide efficient searching, insertion, and deletion operations. They form the basis for more advanced self-balancing trees and are crucial in many applications requiring fast look-up, addition, and removal of ordered data.

Understanding BSTs is essential for tackling more complex tree-based problems and is often a prerequisite for advanced algorithms involving balanced trees and tree-based data structures.

Tomorrow, we'll explore tree traversal techniques in more depth, including both recursive and iterative approaches. Stay tuned!