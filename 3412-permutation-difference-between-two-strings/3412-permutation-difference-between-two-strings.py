import string
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        checker = {}

        for i, char_t in enumerate(t):
            checker[char_t] = i
        
        total = 0

        for i, char_s in enumerate(s):
            total += abs(i - checker[char_s])
        
        return total