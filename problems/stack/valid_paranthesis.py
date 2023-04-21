"""
valid-parentheses
https://leetcode.com/problems/valid-parentheses/
Notes:

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