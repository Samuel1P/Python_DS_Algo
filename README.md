# Python DS & Algo Learning

Personal learning repository for mastering Data Structures and algorithms.

## Quick Stats
- **Data Structures**: 16 implementations
- **Algorithms**: 10 implementations  
- **Problems Solved**: 23
- **Test Coverage**: 29 test cases

## Structure

```
data_structures/    → Linked lists, Trees, Stack, Queue, Graph, Hash tables
algorithms/         → Sorting, Recursion, Tree traversal
problems/           → String, Array, LinkedList, Tree, HashMap, Stack, Bit ops solutions
tests/              → Comprehensive test suite
```

## Topics Covered

### Data Structures
- Linked List (Singly, Doubly)
- Binary Trees & BST
- Stacks & Queues
- Graphs & Hash Tables

### Algorithms
- **Sorting**: Bubble, Selection, Insertion, Merge, Quick
- **Recursion**: Factorial, recursive problems
- **Traversal**: BFS, DFS

### Problems by Category
- **Strings**: palindrome, substring, encoding, roman numerals
- **Arrays**: two sum, three sum, max subarray, stock trading
 - **LinkedLists**: middle of linked list, remove elements, reverse, rotate, detect cycle
- **Trees**: invert, merge trees
- **HashMaps**: anagrams, top K frequent
- **Stack**: valid parentheses
- **Bit Ops**: reverse bits

## Testing

```bash
pytest                          # Run all tests
pytest -v                       # Verbose output
pytest tests/test_dsa/         # Test data structures
pytest tests/test_problems/    # Test problems
```

## Quick Reference: Time Complexities

| Sorting | Best | Average | Worst | Space |
|---------|------|---------|-------|-------|
| Bubble | O(n) | O(n²) | O(n²) | O(1) |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) |

## Setup

```bash
pip install -r requirements.txt
```
