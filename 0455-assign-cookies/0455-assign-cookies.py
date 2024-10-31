class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        l,r = 0,0
        count = 0
        while l < len(g) and r < len(s):

            if g[l] <= s[r]:
                l += 1
                r += 1
                count += 1
            else:
                r += 1
        
        return count