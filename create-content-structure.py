import os

# Define the structure
structure = {
    'content': {
        '_index.md': '',
        'algorithms': {
            '_index.md': '# Algorithms',
            'day1-introduction.md': '# Day 1: Introduction to Algorithms',
            'day2-algorithmic-thinking-and-pseudocode.md': '# Day 2: Algorithmic Thinking and Pseudocode',
            'day3-introduction-to-time-complexity.md': '# Day 3: Introduction to Time Complexity',
            'day4-introduction-to-arrays.md': '# Day 4: Introduction to Arrays',
            'day5-multi-dimensional-arrays-and-sorting.md': '# Day 5: Multi-Dimensional Arrays and Sorting Algorithms',
            'day6-advanced-sorting-insertion-merge.md': '# Day 6: Advanced Sorting Algorithms - Insertion Sort and Merge Sort',
            'day7-introduction-to-linked-lists.md': '# Day 7: Introduction to Linked Lists',
            'day8-singly-linked-lists.md': '# Day 8: Singly Linked Lists - Implementation and Basic Operations',
            'day9-doubly-linked-lists.md': '# Day 9: Doubly Linked Lists - Implementation and Comparison',
            'day10-advanced-linked-list-operations.md': '# Day 10: Advanced Linked List Operations and Problems',
            'day11-stacks.md': '# Day 11: Introduction to Stacks',
            'day12-queues.md': '# Day 12: Introduction to Queues',
            'day13-trees-introduction.md': '# Day 13: Introduction to Trees',
            'day14-binary-trees.md': '# Day 14: Binary Trees',
            'day15-binary-search-trees.md': '# Day 15: Binary Search Trees',
            'day16-tree-traversals.md': '# Day 16: Tree Traversals',
            'day17-heaps.md': '# Day 17: Heaps and Priority Queues',
            'day18-graphs-introduction.md': '# Day 18: Introduction to Graphs',
            'day19-graph-representations.md': '# Day 19: Graph Representations',
            'day20-graph-traversals.md': '# Day 20: Graph Traversals - BFS and DFS',
            'day21-shortest-path-algorithms.md': '# Day 21: Shortest Path Algorithms',
            'day22-minimum-spanning-trees.md': '# Day 22: Minimum Spanning Trees',
            'day23-hash-tables.md': '# Day 23: Hash Tables',
            'day24-sets.md': '# Day 24: Sets and Their Applications',
            'day25-binary-search.md': '# Day 25: Binary Search and Its Variations',
            'day26-quicksort.md': '# Day 26: Quicksort Algorithm',
            'day27-mergesort.md': '# Day 27: Mergesort Algorithm',
            'day28-heapsort.md': '# Day 28: Heapsort Algorithm',
            'day29-sorting-algorithm-comparison.md': '# Day 29: Comparison of Sorting Algorithms',
            'day30-dynamic-programming-introduction.md': '# Day 30: Introduction to Dynamic Programming',
            'day31-fibonacci-and-dp.md': '# Day 31: Fibonacci Sequence and Dynamic Programming',
            'day32-longest-common-subsequence.md': '# Day 32: Longest Common Subsequence',
            'day33-knapsack-problem.md': '# Day 33: The Knapsack Problem',
            'day34-matrix-chain-multiplication.md': '# Day 34: Matrix Chain Multiplication',
            'day35-longest-increasing-subsequence.md': '# Day 35: Longest Increasing Subsequence',
            'day36-edit-distance.md': '# Day 36: Edit Distance Problem',
            'day37-coin-change-problem.md': '# Day 37: Coin Change Problem',
            'day38-rod-cutting.md': '# Day 38: Rod Cutting Problem',
            'day39-palindrome-partitioning.md': '# Day 39: Palindrome Partitioning',
            'day40-greedy-algorithms-introduction.md': '# Day 40: Introduction to Greedy Algorithms',
            'day41-activity-selection.md': '# Day 41: Activity Selection Problem',
            'day42-huffman-coding.md': '# Day 42: Huffman Coding',
            'day43-dijkstras-algorithm.md': '# Day 43: Dijkstra\'s Algorithm',
            'day44-prims-algorithm.md': '# Day 44: Prim\'s Algorithm',
            'day45-kruskals-algorithm.md': '# Day 45: Kruskal\'s Algorithm',
            'day46-floyd-warshall-algorithm.md': '# Day 46: Floyd-Warshall Algorithm',
            'day47-bellman-ford-algorithm.md': '# Day 47: Bellman-Ford Algorithm',
            'day48-backtracking-introduction.md': '# Day 48: Introduction to Backtracking',
            'day49-n-queens-problem.md': '# Day 49: N-Queens Problem',
            'day50-sudoku-solver.md': '# Day 50: Sudoku Solver',
            'day51-hamiltonian-cycle.md': '# Day 51: Hamiltonian Cycle',
            'day52-graph-coloring.md': '# Day 52: Graph Coloring Problem',
            'day53-bit-manipulation-techniques.md': '# Day 53: Bit Manipulation Techniques',
            'day54-power-set.md': '# Day 54: Generating Power Set using Bit Manipulation',
            'day55-counting-bits.md': '# Day 55: Counting Bits and Bit Hacks',
            'day56-string-algorithms-kmp.md': '# Day 56: String Algorithms - KMP Algorithm',
            'day57-rabin-karp-algorithm.md': '# Day 57: Rabin-Karp Algorithm',
            'day58-tries.md': '# Day 58: Tries and Their Applications',
            'day59-advanced-tree-structures.md': '# Day 59: Advanced Tree Structures (AVL, Red-Black Trees)',
            'day60-competitive-programming-techniques.md': '# Day 60: Competitive Programming Techniques and Wrap-up'
        },
        'about.md': '# About',
        'resources.md': '# Resources'
    }
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            if not os.path.exists(path):
                with open(path, 'w') as f:
                    f.write(content)
                print(f"Created: {path}")
            else:
                print(f"Skipped existing file: {path}")

# Create the structure
create_structure('.', structure)

print("Content structure for all 60 days updated successfully!")