class Solution:
    def scoreOfString(self, s: str) -> int:
        #what is a ASCII value?
        #would it be okay if I looked that up?

        total = 0
        for i in range(len(s)-1):
            total += abs(ord(s[i]) - ord(s[i+1]))
        return total