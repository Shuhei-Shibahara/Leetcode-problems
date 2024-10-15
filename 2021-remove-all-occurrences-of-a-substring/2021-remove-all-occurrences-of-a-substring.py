class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        #go through s and find occurenses of part
        #when we find one and remove we need to start over and look through again
        #once this is completed then we return s

        idx = s.find(part)
        length = len(part) - 1
        while idx != -1:
            s = s[:idx] + s[idx + len(part):]
            idx = s.find(part)
        
        return s
