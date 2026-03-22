# Repo Feedback — Action Items

---

## Code fixes

- `problems/list/three_sum.py` line 31: bounds check should come before array access to avoid index-out-of-bounds
- `problems/trees/invert_binary_tree.py` lines 20-21: use `self.invertTree(...)` instead of `Solution().invertTree(...)` to avoid unnecessary object allocation on every recursive call
- `problems/strings/valid_palindrome.py` line 23: leftover `print()` inside `is_alnum()`
- `data_structures/Linked_List/Linked_List.py`: leftover `print()` calls in `pop_first`, `get_node`, `set_node`

## Notes to fill in

- `problems/strings/valid_palindrome.py`: step 4 in approach notes is blank
- `problems/strings/encode_decode_strings.py`: approach notes never written

## Worth documenting

- `data_structures/Linked_List/Linked_List.py` `Node.__bool__`: always returns True for any Node — add a comment explaining this is intentional
- `data_structures/Linked_List/Linked_List.py` `Node.__len__`: will infinite-loop on cyclic lists — add a docstring warning now that cycle detection exists

## Next problems to solve

Linked list (finish the category first):
- palindrome linked list
- intersection of two linked lists
- add two numbers

Then move to arrays/strings — focus on sliding window and two-pointer patterns.

Skip hard DP, graph algorithms, and advanced tree problems until fundamentals are locked in.

## Repo organization

- Consider renaming `problems/list/` to `problems/arrays/` for clarity
