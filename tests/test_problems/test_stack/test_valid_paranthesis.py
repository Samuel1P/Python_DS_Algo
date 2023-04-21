
"""
Test Suite for the valid paranthesis problem
"""

from problems.stack.valid_paranthesis import Solution


class TestValidParanthesis:
    """
    Test Class
    """
        
    def test_one(self):
        test_str = "{{}}"
        actual_result = Solution().isValid(test_str)
        assert actual_result == True
        
    def test_two(self):
        test_str = ""
        actual_result = Solution().isValid(test_str)
        assert actual_result == True

    def test_three(self):
        test_str = "([{}])"
        actual_result = Solution().isValid(test_str)
        assert actual_result == True
        
    def test_four(self):
        test_str = "[{{]}}"
        actual_result = Solution().isValid(test_str)
        assert actual_result == False
        
    def test_five(self):
        test_str = "[][][][][]["
        actual_result = Solution().isValid(test_str)
        assert actual_result == False
    
    def test_six(self):
        test_str = "["
        actual_result = Solution().isValid(test_str)
        assert actual_result == False
        
    def test_seven(self):
        test_str = "]"
        actual_result = Solution().isValid(test_str)
        assert actual_result == False