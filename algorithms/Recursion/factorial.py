"""
Factorail of an integer using recursion
"""

def factorial(n):
    if n == 1: # base case or exit case - we start popping funcs from call stack after this
        return n
    return n * factorial(n-1)

print(factorial(4)) # 24
