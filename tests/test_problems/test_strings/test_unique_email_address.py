# https://leetcode.com/problems/unique-email-addresses/description/
"""
Notes:
"""
from problems.strings.unique_email_address import Solution, Solution2

class TestUniqueEmailAddress:
    """
    Test Class
    """
    def test_one(self):
        """
        Test Case 1
        """
        emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
        expected = 2
        output = Solution().numUniqueEmails(emails)
        assert expected == output, f"expected {expected} but got {output}"
        
    def test_two(self):
        """
        Test Case 2
        """
        emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
        expected = 3
        output = Solution().numUniqueEmails(emails)
        assert expected == output, f"expected {expected} but got {output}"
        

    def test_four(self):
            """
            Test Case 4
            """
            emails = [
                "unique.email+test@domain.com",
                "unique.email@domain.com",
                "u.n.i.q.u.e.e.m.a.i.l+test@domain.com",
                "uniqueemail@domain.com",
                "unique.email+spam@anotherdomain.com"
            ]
            expected = 2
            output = Solution().numUniqueEmails(emails)
            assert expected == output, f"expected {expected} but got {output}"
        