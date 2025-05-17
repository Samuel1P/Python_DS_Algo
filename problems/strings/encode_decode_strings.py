# https://neetcode.io/problems/string-encode-and-decode
# https://leetcode.com/problems/encode-and-decode-strings/description/

"""
Notes:

"""



from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for word in strs:
            output += str(len(word))+"#"+word
        return output

    def decode(self, s: str) -> List[str]:
        
        output = []
        i = 0
        while i < len(s): #1
            j = i #1
            while s[j] != "#":
                j+=1
            word_size = int(s[i:j])
            output.append(s[j+1:j+1+word_size])
            i = j + 1 + word_size
        return output
    
#print(Solution().decode("2#AB3#IJK"))
