"""
valid-parentheses
https://leetcode.com/problems/valid-parentheses/
Notes:
we use stack to solve this. I am using the stack implementation which I wrote earlier.

apart from edge cases, main logic is this..
1. Whenever there is a opener, push it to the stack.
2. Whenever, there is a closer, check if the top of the stack is opener of same kind. if yes, pop the opener from the stack, contiure next iteration, if the top is different kind, then fail.
3. fail if there is items in the stack after all iterations are completed.
"""

from data_structures.Stack.Stack_implementation_using_LinkedList import Stack


class Solution:
    def isValid(self, input_str: str) -> bool:
        stack = Stack()
        close_map = {")": "(",
                     "}": "{",
                     "]": "["}
        if not input_str.strip():
            return True
        for item in input_str:
            if item in close_map.values():
                # if opener
                stack.push(item)
            elif item in close_map:
                # if closer
                if not stack.top or stack.top.value != close_map[item]:
                    return False
                stack.pop() # pop the opener
        return True if stack.top is None else False


class _Solution:
    "Solution for leetcode"
    def isValid(self, input_str: str) -> bool:
        stack = []
        close_map = {")": "(", "}": "{", "]": "["}
        if not input_str.strip():
            return True
        for item in input_str:
            if stack and item in close_map:
                top_v = stack[-1]
                if  top_v == close_map[item]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)
        if stack:
            return False
        return True