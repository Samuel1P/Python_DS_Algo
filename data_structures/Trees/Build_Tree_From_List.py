"""
Build Binary Tree from Level-Order List

Utility to convert between LeetCode's level-order array format and actual tree nodes.

LeetCode represents binary trees as level-order arrays:
    [3, 9, 20, None, None, 15, 7]

This corresponds to:
        3
       / \
      9   20
         / \
        15   7

The array is read left-to-right, top-to-bottom (BFS order).
None means "no child at this position".

This module provides:
    - build_tree(level_order_list) → root TreeNode
    - tree_to_list(root)           → level_order_list

Both use BFS (queue-based) since level-order is inherently a BFS concept.
"""

from typing import List, Optional
from collections import deque
from data_structures.Trees.Binary_Tree_Basic import TreeNode


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Build a binary tree from a level-order list (LeetCode format).

    Args:
        values: List like [3, 9, 20, None, None, 15, 7]
                None means "no node at this position".

    Returns:
        Root TreeNode of the constructed tree, or None if input is empty.

    How it works:
        This is BFS construction — the inverse of BFS traversal.
        We process the array left to right. For each node we dequeue,
        the next two values in the array are its left and right children.
        If a value is None, that child doesn't exist (and we don't enqueue it,
        because a non-existent node has no children to process later).

    Example:
        >>> root = build_tree([3, 9, 20, None, None, 15, 7])
        >>> root.val
        3
        >>> root.left.val
        9
        >>> root.right.val
        20
    """
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        parent = queue.popleft()

        # Next value in the array is the left child of this parent
        if i < len(values) and values[i] is not None:
            parent.left = TreeNode(values[i])
            queue.append(parent.left)
        i += 1

        # Next value in the array is the right child of this parent
        if i < len(values) and values[i] is not None:
            parent.right = TreeNode(values[i])
            queue.append(parent.right)
        i += 1

    return root


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """
    Convert a binary tree back to a level-order list (LeetCode format).
    Useful for comparing trees in test assertions.

    Trailing None values are stripped to match LeetCode's convention.
    e.g. [3, 9, 20, None, None, 15, 7] not [3, 9, 20, None, None, 15, 7, None, None, None, None]

    Args:
        root: Root TreeNode of the tree.

    Returns:
        Level-order list like [3, 9, 20, None, None, 15, 7]

    How it works:
        Standard BFS traversal, but we also record None for missing children.
        After traversal, we strip trailing Nones since LeetCode omits them.

    Example:
        >>> root = build_tree([1, 2, 3])
        >>> tree_to_list(root)
        [1, 2, 3]
    """
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node is not None:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Strip trailing Nones — LeetCode doesn't include them
    while result and result[-1] is None:
        result.pop()

    return result
