---
title: "Day 42: Huffman Coding"
weight: 42
menu:
  main:
    parent: "Algorithms"
    weight: 42
---

# Huffman Coding

Welcome to Day 42 of our 60 Days of Coding Algorithm Challenge! Today, we'll explore Huffman Coding, a greedy algorithm used for lossless data compression.

## What is Huffman Coding?

Huffman Coding is an efficient method for data compression. It assigns variable-length codes to characters based on their frequencies. More frequent characters get shorter codes, while less frequent characters get longer codes.

## How Huffman Coding Works

1. Calculate the frequency of each character in the input.
2. Create a leaf node for each character and add it to a priority queue.
3. While there's more than one node in the queue:
   - Remove the two nodes with the lowest frequency.
   - Create a new internal node with these two nodes as children.
   - Add the new node to the queue.
4. The remaining node is the root of the Huffman tree.
5. Traverse the tree to assign codes to characters.

## Implementation

Let's implement Huffman Coding in Python:

```python
import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    # Count frequency of characters
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1
    
    # Create a priority queue of nodes
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)
    
    # Build the Huffman tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        internal = Node(None, left.freq + right.freq)
        internal.left = left
        internal.right = right
        heapq.heappush(heap, internal)
    
    return heap[0]

def generate_codes(root):
    def traverse(node, code):
        if node.char:
            codes[node.char] = code
            return
        traverse(node.left, code + '0')
        traverse(node.right, code + '1')
    
    codes = {}
    traverse(root, '')
    return codes

def huffman_encoding(text):
    root = build_huffman_tree(text)
    codes = generate_codes(root)
    encoded_text = ''.join(codes[char] for char in text)
    return encoded_text, root

def huffman_decoding(encoded_text, root):
    decoded_text = []
    current = root
    for bit in encoded_text:
        if bit == '0':
            current = current.left
        else:
            current = current.right
        if current.char:
            decoded_text.append(current.char)
            current = root
    return ''.join(decoded_text)

# Example usage
text = "this is an example for huffman encoding"
encoded, tree = huffman_encoding(text)
print(f"Encoded text: {encoded}")
decoded = huffman_decoding(encoded, tree)
print(f"Decoded text: {decoded}")
```

## Time Complexity

- Building the frequency table: O(n)
- Creating and building the Huffman tree: O(k log k), where k is the number of unique characters
- Generating codes: O(k)
- Encoding: O(n)
- Decoding: O(n)

Overall time complexity: O(n + k log k), where n is the length of the text and k is the number of unique characters.

## Space Complexity

O(k) for the Huffman tree and codes table, where k is the number of unique characters.

## Advantages of Huffman Coding

1. Lossless compression
2. Variable-length codes for efficient compression
3. Optimal prefix codes (no code is a prefix of another)

## Disadvantages

1. Requires knowledge of character frequencies in advance
2. Two passes over the data (one for counting frequencies, one for encoding)
3. Compressed data size depends on the accuracy of frequency statistics

## Applications

1. Data compression in file archiving tools (e.g., zip)
2. Image compression (used in JPEG and PNG)
3. Implementation of data structures like succinct trees

## Exercise

1. Modify the Huffman Coding algorithm to work with bytes instead of characters for more general data compression.
2. Implement a function to calculate the compression ratio achieved by Huffman Coding for a given input.
3. Create a variant of Huffman Coding that uses a predefined frequency table for English text, eliminating the need for the first pass over the data.

## Summary

Today, we explored Huffman Coding, a fundamental algorithm in data compression. We implemented the algorithm, discussed its time and space complexity, and looked at its advantages, disadvantages, and real-world applications.

Understanding Huffman Coding provides insights into how efficient data compression works and demonstrates another powerful application of greedy algorithms and priority queues.

Tomorrow, we'll study the Dijkstra’s Algorithm. Stay tuned!
