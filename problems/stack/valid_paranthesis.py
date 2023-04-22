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

stack = Stack()

class Solution:
    def isValid(self, input_str: str) -> bool:
        close_map = {")": "(", "}": "{", "]": "["}
        if not input_str.strip():
            return True
        for item in input_str:
            if item in close_map.values():
                stack.push(item)
            else:
                top_v = stack.top.value
                if  top_v == close_map[item]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 1:
            return False
        return True


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