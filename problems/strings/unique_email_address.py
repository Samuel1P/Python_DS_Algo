# https://leetcode.com/problems/unique-email-addresses/description/
"""
Notes:

Solution1:
1. This is using built-ins
2. Split the email into local and domain parts
3. split the local by the + sign and take the first part
4. Split the local by the . sign and join the parts together
5. Add the local and domain parts together and add to the set
6. Return the length of the set

no built-ins way to do it:
1.

"""
from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ue = set()
        for e in emails:
            u, d = e.split("@")
            u = u.split("+")[0]
            u = "".join(u.split("."))
            ue.add(u+"@"+d)
        return len(ue)
    
class Solution2:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ue = set()
        for e in emails:
            i = 0
            u = ""
            while e[i] not in ["@", "+"]:
                if e[i] != ".":
                    u = u + e[i]
                i += 1
            while e[i] != "@":
                i += 1
            d = e[i+1:]
            ue.add(u+"@"+d)
            
        return len(ue)