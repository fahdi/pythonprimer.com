---
title: "Day 16: Tree Traversals"
weight: 16
menu:
  main:
    parent: "Algorithms"
    weight: 16
---

# Tree Traversals

Welcome to Day 16 of our 60 Days of Coding Algorithm Challenge! Today, we'll dive deep into various tree traversal techniques, exploring both recursive and iterative approaches. Tree traversals are fundamental operations for processing tree-based data structures and are crucial for solving many algorithmic problems.

## Types of Tree Traversals

There are two main categories of tree traversals:

1. Depth-First Search (DFS)
   - Inorder Traversal
   - Preorder Traversal
   - Postorder Traversal

2. Breadth-First Search (BFS)
   - Level Order Traversal

Let's explore each of these in detail.

## Depth-First Search (DFS) Traversals

### 1. Inorder Traversal (Left, Root, Right)

Inorder traversal visits the left subtree, then the root, and finally the right subtree.

#### Recursive Approach:

```python
def inorder_recursive(root):
    if root:
        inorder_recursive(root.left)
        print(root.val, end=" ")
        inorder_recursive(root.right)

```

#### Iterative Approach:

```python
def inorder_iterative(root):
    stack = []
    current = root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        print(current.val, end=" ")
        current = current.right
```

### 2. Preorder Traversal (Root, Left, Right)

Preorder traversal visits the root, then the left subtree, and finally the right subtree.

#### Recursive Approach:

```python
def preorder_recursive(root):
    if root:
        print(root.val, end=" ")
        preorder_recursive(root.left)
        preorder_recursive(root.right)
```

#### Iterative Approach:

```python
def preorder_iterative(root):
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val, end=" ")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
```

### 3. Postorder Traversal (Left, Right, Root)

Postorder traversal visits the left subtree, then the right subtree, and finally the root.

#### Recursive Approach:

```python
def postorder_recursive(root):
    if root:
        postorder_recursive(root.left)
        postorder_recursive(root.right)
        print(root.val, end=" ")
```

#### Iterative Approach:

```python
def postorder_iterative(root):
    if not root:
        return
    stack1, stack2 = [root], []
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    while stack2:
        print(stack2.pop().val, end=" ")
```

## Breadth-First Search (BFS) Traversal

### Level Order Traversal

Level order traversal visits nodes level by level from left to right.

```python
from collections import deque

def level_order_traversal(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            print(node.val, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()  # New line for each level
```

## Time and Space Complexity

For all traversals:
- Time Complexity: O(n), where n is the number of nodes in the tree
- Space Complexity: 
  - Recursive: O(h) in the worst case, where h is the height of the tree
  - Iterative: O(n) in the worst case for a skewed tree

## Applications of Tree Traversals

1. **Inorder Traversal**: 
   - Used to get nodes of BST in non-decreasing order
   - Used in expression tree evaluation

2. **Preorder Traversal**:
   - Used to create a copy of the tree
   - Used to get prefix expression on an expression tree

3. **Postorder Traversal**:
   - Used to delete the tree
   - Used to get postfix expression of an expression tree

4. **Level Order Traversal**:
   - Used in level order problems
   - Used in finding the minimum depth of a binary tree

## Advanced Traversal Techniques

### 1. Morris Traversal

Morris Traversal allows us to traverse the tree without using stack or recursion. It has O(1) space complexity.

```python
def morris_inorder(root):
    current = root
    while current:
        if not current.left:
            print(current.val, end=" ")
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right
            
            if not predecessor.right:
                predecessor.right = current
                current = current.left
            else:
                predecessor.right = None
                print(current.val, end=" ")
                current = current.right
```

### 2. Threaded Binary Tree Traversal

A threaded binary tree uses the null pointers in leaf nodes to create threads to other nodes, allowing for more efficient traversal without using a stack or recursion.

## Exercise

1. Implement a function to perform zigzag level order traversal of a binary tree.
2. Create a method to find the vertical order traversal of a binary tree.
3. Implement a function to serialize and deserialize a binary tree.

## Summary

Today, we explored various tree traversal techniques, including depth-first (inorder, preorder, postorder) and breadth-first (level order) approaches. We implemented both recursive and iterative versions of these traversals and discussed their applications and complexities.

Understanding these traversal methods is crucial for solving a wide range of tree-based problems and forms the foundation for more advanced tree algorithms. As we progress through this challenge, you'll find these traversal techniques invaluable in tackling complex tree-related problems.

Tomorrow, we'll dive into heaps and priority queues, building upon our knowledge of trees to explore these specialized data structures. Stay tuned!

