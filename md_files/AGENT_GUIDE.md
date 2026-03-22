# Agent Guide — Python DS & Algo Repo

This document is the single source of truth for any agent working in this repo.
Read this fully before creating or modifying any file.

---

## CRITICAL — Read This First

**This is a personal learning repository. Not a production codebase. Not a library. Not for others.**

---

### What the agent is allowed to do

- Create new files with the correct name and location
- Add the URL comment at the top
- Add a placeholder module-level docstring at the top (do not write approach notes)
- Add the `Solution` class shell with the correct method signature and a `pass` placeholder
- Add the test file with the correct class name, import, and empty test method stubs
- Write complete test cases (test logic is fine — the agent can write tests)
- Fix syntax errors or broken imports if asked

### What the agent must NEVER do

- **Write the actual solution logic inside any `Solution` method**
- **Fill in the body of any algorithm or data structure method**
- The user writes all real logic themselves — this is the entire point of the repo
- **Write approach notes / reasoning in problem files**

The user learns by solving problems with their own hands.
If the agent writes the solution, the learning is lost.
When in doubt: create the file, set up the structure, leave a `pass`, and stop.

---

### What "boilerplate" means in this repo

Boilerplate the agent CAN create:
```python
# https://leetcode.com/problems/some-problem/
"""
This section is a placeholder.
Fill approach notes here after implementation.
Keep it readable and beginner-friendly.
Time: O(?)
Space: O(?)
"""
from typing import List

class Solution:
    def someMethod(self, nums: List[int]) -> int:
        pass  # user implements this
```

And the matching test file:
```python
"""
Test Suite for some-problem
"""
from problems.list.some_problem import Solution


class TestSomeProblem:
    """
    Test Class
    """
    def test_one(self):
        pass  # user fills in or agent fills in test cases

    def test_two(self):
        pass
```

---

The single most important value here is **readability and revisability**.
The owner must be able to come back to any file after months or years and immediately understand:
- What the problem is
- What the approach is
- Why the code is written the way it is

**Clever, compact, or "smart" code is actively unwanted.**
If there is a choice between a shorter solution and a more readable one — always choose readable.
If there is a choice between an optimized solution and a clearly explained one — always choose clarity first, then note the optimization in the docstring.

Write code and comments as if explaining to yourself after a long break.

---

## 1. What This Repo Is

A personal Python learning repo for Data Structures, Algorithms, and LeetCode-style problem solving.
Every file is written by one person for self-study. Keep that tone — clean, readable, and informal in comments.
The goal is not to impress. The goal is to learn and remember.

---

## 2. Repo Layout

```
root/
├── data_structures/        # DS implementations from scratch
│   ├── Linked_List/
│   ├── Trees/
│   ├── Stack/
│   ├── Queue/
│   ├── Graph/
│   ├── Hash_Tables/
│   └── List/
├── algorithms/             # Algorithm implementations
│   ├── Sorting/
│   ├── Recursion/
│   └── Tree_Traversal/
├── problems/               # LeetCode-style solutions
│   ├── strings/
│   ├── list/
│   ├── linkedlist/
│   ├── trees/
│   ├── hashmaps/
│   ├── stack/
│   └── bit_operations/
├── tests/
│   ├── test_dsa/           # Tests for data_structures/ and algorithms/
│   └── test_problems/      # Tests for problems/ — mirrors problems/ folder structure
│       ├── test_strings/
│       ├── test_lists/
│       ├── test_linkedlist/
│       ├── test_trees/
│       ├── test_hashmaps/
│       ├── test_stack/
│       └── test_bit_operations/
├── archive/                # Old scratch files — do NOT add new files here
├── md_files/               # Documentation only
├── .agent_config           # Agent config pointer file
├── requirements.txt        # pytest only
└── README.md
```

---

## 3. Naming Conventions

| Type | Convention | Example |
|------|-----------|---------|
| Problem files | `snake_case.py` | `valid_palindrome.py` |
| Data structure files | `Title_Case.py` | `Linked_List.py`, `Binary_Search_Tree.py` |
| Algorithm files | `Title_Case.py` | `Merge_Sort.py`, `Bubble_Sort_Loop.py` |
| Test files | `test_snake_case.py` | `test_valid_palindrome.py` |
| Classes | `PascalCase` | `Solution`, `LinkedList`, `BinarySearchTree` |
| Methods/functions | `camelCase` (LeetCode style for solutions) | `twoSum`, `reverseList`, `maxSubArray` |
| Helper methods | `snake_case` | `is_alnum`, `traversed_data_list` |

---

## 4. Problem File Template

Every file in `problems/` must follow this exact structure:

```python
# https://leetcode.com/problems/<problem-slug>/
"""
This section is a placeholder.
Explain the approach in simple, plain English after you implement.
Keep the steps short and clear for revisiting later.

Time: O(?)
Space: O(?)  (include if relevant)
"""
from typing import List  # import only what is needed

class Solution:
    def methodName(self, param: type) -> type:
        # implementation
        pass
```

**Rules:**
- The LeetCode URL goes on line 1 as a comment.
- The module-level docstring contains the approach notes and complexity.
- There is exactly one `Solution` class per file.
- Method name matches the LeetCode method name exactly (camelCase).
- Use `from typing import List / Optional` as needed.
- No `if __name__ == "__main__"` block in problem files.
- Do NOT add a function-level docstring inside the method — the module docstring covers it.

**Real example** (`problems/list/maximum_subarray.py`):
```python
"""
maximum-subarray
https://leetcode.com/problems/maximum-subarray/

Notes:
This is called as the Kadane Algorithm.
1. Initalise two counters, max sum and curr sum. max sum will be the first element and curr sum will be zero.
2. Loop through the list
...

Time: O(n)
"""
from typing import List

class Solution:
    def maxSubArray(self, num_list: List[int]) -> int:
        max_sum = num_list[0]
        curr_sum = 0
        for num in num_list:
            ...
        return max_sum
```

---

## 5. Test File Template

Every test file in `tests/test_problems/` must follow this structure:

```python
# https://leetcode.com/problems/<problem-slug>/   (optional but preferred for problems)
"""
Test Suite for the <problem name>
"""
from problems.<category>.<filename> import Solution


class Test<ProblemName>:
    """
    Test Class
    """
    def test_one(self):
        inp = <input>
        outp = Solution().<methodName>(inp)
        assert outp == <expected>

    def test_two(self):
        ...
```

**Rules:**
- Import path mirrors the `problems/` folder: `from problems.<subfolder>.<filename> import Solution`
- Class name is `Test` + PascalCase problem name.
- Test methods are named `test_one`, `test_two`, `test_three`, etc. (not `test_case_1`).
- Use `actual` / `expected` variable names when the test is more complex (see below).
- No pytest fixtures unless the test needs shared state (use `setup_class` in that case).
- Minimum 3 test cases per problem. Include at least one edge case.

**When inputs are complex** (e.g. linked lists, trees), use `actual` / `expected` pattern:
```python
def test_one(self):
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    expected = 6
    actual = Solution().maxSubArray(nums)
    assert actual == expected
```

**When test needs shared setup** (linked list / tree tests):
```python
class TestSomething:
    def setup_class(self):
        self.LL = LinkedList(1)
        self.LL.append(2)
        self.LL.append(3)

    def test_one(self):
        result = Solution().someMethod(self.LL.head)
        assert result == expected
```

---

## 6. Linked List Problem — Import Pattern

When a problem works with linked lists, import the `Node` from the existing data structure:

```python
from typing import Optional
from data_structures.Linked_List.Linked_List import Node

# Definition for singly-linked list.
# class Node:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def someMethod(self, head: Optional[Node]) -> Optional[Node]:
        ...
```

The commented-out class definition is kept as a reference (LeetCode convention). Keep it.

In the test file, import both `Solution` and `LinkedList`:
```python
from problems.linkedlist.<filename> import Solution
from data_structures.Linked_List.Linked_List import LinkedList
```

---

## 7. Tree Problem — Import Pattern

```python
from data_structures.Trees.Binary_Search_Tree import Node

class Solution:
    def someTreeMethod(self, curr_node: Node) -> Node:
        ...
```

In the test file:
```python
from problems.trees.<filename> import Solution
from data_structures.Trees.Binary_Search_Tree import BinarySearchTree, Node
```

Use `BinarySearchTree` to build the tree in tests, then pass `.root` or individual nodes to `Solution`.

---

## 8. Algorithm File Template

Files in `algorithms/` are more script-like — they are not wrapped in a class.

```python
"""
<Algorithm Name>
Time Big O: O(?)
Space: O(?)
"""

sample_data = [...]

print("input: ", sample_data)

def helper_function(...):
    ...

def main_algorithm(...):
    ...

output_data = main_algorithm(sample_data)
print("output: ", output_data)
```

**Rules:**
- Module docstring with time/space complexity at the top.
- `sample_data` at module level for quick manual testing.
- `print` statements for input/output are fine and expected.
- No `Solution` class — just plain functions.

---

## 9. Data Structure File Template

Files in `data_structures/` implement the structure from scratch.

```python
"""
<Data Structure Name> implementation
"""

class Node:
    """
    Node Class
    """
    def __init__(self, value=None, next=None):
        """
        Constructor for Node
        """
        self.val = value
        self.next = next

    def __repr__(self):
        return f"Node('{self.val}')"


class <DataStructureName>:
    """
    <DataStructureName> Class
    """
    def __init__(self, value=None):
        """
        constructor
        """
        ...
```

**Rules:**
- Module-level docstring.
- Class-level docstring on every class.
- Method-level docstring on `__init__` and dunder methods.
- Regular methods do not need docstrings if the name is self-explanatory.
- Commented-out usage examples at the bottom of the file are fine (existing pattern).

---

## 10. Where to Place New Files

| What you're adding | File goes in | Test goes in |
|--------------------|-------------|--------------|
| New LeetCode string problem | `problems/strings/` | `tests/test_problems/test_strings/` |
| New LeetCode array/list problem | `problems/list/` | `tests/test_problems/test_lists/` |
| New LeetCode linked list problem | `problems/linkedlist/` | `tests/test_problems/test_linkedlist/` |
| New LeetCode tree problem | `problems/trees/` | `tests/test_problems/test_trees/` |
| New LeetCode hashmap problem | `problems/hashmaps/` | `tests/test_problems/test_hashmaps/` |
| New LeetCode stack problem | `problems/stack/` | `tests/test_problems/test_stack/` |
| New LeetCode bit ops problem | `problems/bit_operations/` | `tests/test_problems/test_bit_operations/` |
| New sorting algorithm | `algorithms/Sorting/` | `tests/test_dsa/` |
| New data structure | `data_structures/<Name>/` | `tests/test_dsa/` |

---

## 11. Existing Data Structures Available for Import

| Class | Import path | Key attributes |
|-------|------------|----------------|
| `Node` (linked list) | `data_structures.Linked_List.Linked_List` | `.val`, `.next` |
| `LinkedList` | `data_structures.Linked_List.Linked_List` | `.head`, `.tail`, `.length`, `.append()`, `.traversed_data_list()`, `.traversed_data_list_from_head(head)` |
| `Node` (doubly) | `data_structures.Linked_List.Doubly_Linked_List` | `.val`, `.next`, `.prev` |
| `Node` (tree) | `data_structures.Trees.Binary_Search_Tree` | `.val`, `.left`, `.right` |
| `BinarySearchTree` | `data_structures.Trees.Binary_Search_Tree` | `.root`, `.insert_node(val)`, `.bfs()`, `.bfs_from_node(node)` |
| `BinaryTree` | `data_structures.Trees.Binary_Tree_Basic` | basic tree ops |

---

## 12. Key Patterns to Follow

**Readability over everything.**
This repo is revisited after long gaps — weeks, months, sometimes years.
Every file must be self-explanatory to someone who has completely forgotten the problem.
Do not write terse one-liners when a few clear lines communicate better.
Do not omit steps in the approach notes just because the logic "seems obvious".

**Always use `Solution` class** for problems (not standalone functions).

**Complexity must be in the module docstring**, not inline comments:
```python
# WRONG
def maxSubArray(...):
    # Time: O(n)

# RIGHT — in the module docstring at the top
"""
Time: O(n)
"""
```

**Approach notes go in the module docstring**, written as numbered steps in plain English. They can be slightly informal — this is a personal learning repo.

**Test assertions**: prefer `assert actual == expected` over `assert Solution().method() == value` for readability when the setup is more than one line.

**Do not use pytest fixtures** (`@pytest.fixture`) unless absolutely necessary. The existing pattern uses `setup_class` for shared state.

---

## 13. Running Tests

```bash
pytest                                  # all tests
pytest tests/test_problems/            # all problem tests
pytest tests/test_dsa/                 # all dsa tests
pytest tests/test_problems/test_strings/test_valid_palindrome.py  # single file
pytest -v                              # verbose
```

No `pytest.ini` or `pyproject.toml` exists — pytest runs with default settings from the repo root.

---

## 14. Before Submitting — Quality Checklist

Run through this before considering any file complete:

- [ ] **Could you re-read this file cold, after 6 months, and understand it immediately?** (most important)
- [ ] Approach notes explain the thinking in plain English, step by step — not just what the code does
- [ ] Variable names are descriptive — no single-letter names except well-known loop counters (`i`, `j`) or pointer pairs (`left`, `right`)
- [ ] Code follows PEP 8
- [ ] Functions/classes have docstrings (where required by the templates above)
- [ ] Type hints are included
- [ ] Tests are comprehensive (minimum 3 cases, at least one edge case)
- [ ] Edge cases are handled in the implementation
- [ ] Time complexity is documented in the module docstring
- [ ] No clever tricks that sacrifice clarity — if a trick is used, it must be explained in a comment

### Problem-Solving Approach (for new problems)

1. Understand the problem thoroughly — read the constraints
2. Plan the approach and write it out as numbered notes in the module docstring
3. Consider time and space complexity before coding
4. Implement the solution inside the `Solution` class
5. Write test cases covering normal inputs, edge cases, and boundary conditions
6. Verify all tests pass with `pytest`
7. Optimize if a better time/space complexity is achievable

---

## 15. What NOT to Do

- Do NOT add files to `archive/` — it is for old scratch work only.
- Do NOT create a new top-level folder without a clear reason.
- Do NOT use `@pytest.mark` decorators unless asked.
- Do NOT add `__init__.py` files to `problems/` subfolders — they don't have them.
- Do NOT wrap algorithm files in a `Solution` class — they use plain functions.
- Do NOT add a `requirements.txt` dependency unless asked — the only dependency is `pytest`.
- Do NOT delete commented-out usage examples at the bottom of data structure files.

### 16. Cursor / IDE behavior (learning-mode rule)

- Keep AI completion disabled for this repository by using the workspace `.vscode/settings.json` settings.
- Restrict this behavior to this workspace/repo only (do not apply globally).
