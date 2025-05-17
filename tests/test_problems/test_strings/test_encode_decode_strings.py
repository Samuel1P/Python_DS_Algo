# https://neetcode.io/problems/string-encode-and-decode
# https://leetcode.com/problems/encode-and-decode-strings/description/

from problems.strings.encode_decode_strings import Solution

class TestEncodeDecodeStrings:
    """
    Test Class
    """
    def test_one(self):
        inp = ["neet","code","love","you"]
        encoded_string = Solution().encode(inp)
        print(f"encoded_string: {encoded_string}")
        decoded_string = Solution().decode(encoded_string)
        print(f"decoded_string: {decoded_string}")
        assert decoded_string == inp, f"expected {inp} but got {decoded_string}"
        
    def test_two(self):
        inp = ["a","b","c"]
        encoded_string = Solution().encode(inp)
        decoded_string = Solution().decode(encoded_string)
        assert decoded_string == inp, f"expected {inp} but got {decoded_string}"
        
    def test_three(self):
        inp = ["#1he4llo","2wo3#rl42d#"]
        encoded_string = Solution().encode(inp)
        decoded_string = Solution().decode(encoded_string)
        assert decoded_string == inp, f"expected {inp} but got {decoded_string}"
        
    def test_four(self):
        inp = ["test", "case", "example"]
        encoded_string = Solution().encode(inp)
        decoded_string = Solution().decode(encoded_string)
        assert decoded_string == inp, f"expected {inp} but got {decoded_string}"

    def test_five(self):
        inp = ["", " ", "   ", "a"*1000, "b"*5000, "c"*10000]
        encoded_string = Solution().encode(inp)
        decoded_string = Solution().decode(encoded_string)
        assert decoded_string == inp, f"expected {inp} but got {decoded_string}"

    def test_six(self):
        inp = ["special!@#$%^&*()_+-=[]{}|;:',.<>?/`~", "1234567890", "multi\nline\nstring", "tab\tseparated\tvalues"]
        encoded_string = Solution().encode(inp)
        decoded_string = Solution().decode(encoded_string)
        assert decoded_string == inp, f"expected {inp} but got {decoded_string}"

    def test_seven(self):
        inp = ["", "a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh", "abcdefghi", "abcdefghij"]
        encoded_string = Solution().encode(inp)
        decoded_string = Solution().decode(encoded_string)
        assert decoded_string == inp, f"expected {inp} but got {decoded_string}"
        