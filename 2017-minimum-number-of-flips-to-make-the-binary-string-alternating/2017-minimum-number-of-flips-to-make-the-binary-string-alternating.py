class Solution:
    def minFlips(self, s: str) -> int:
        #since we know we want to have the end goal be the alternating string we can compare the s with a alternated string and look for differences
        #lets first combine s with itself to extend it, this will show every possible version of type-1
        #keep compaing that with the alternated string and see what the min difference is
        n = len(s)
        s = s + s
        alt1, alt2 = "",""

        for i in range(len(s)):
            alt1 += "0" if i % 2 else "1"
            alt2 += "1" if i % 2 else "0"
        
        res = len(s)
        diff1,diff2 = 0,0
        l = 0
        for r in range(len(s)):
            if s[r] != alt1[r]:
                diff1 += 1
            if s[r] != alt2[r]:
                diff2 += 1
            
            if (r - l + 1) > n:
                if s[l] != alt1[l]:
                    diff1 -= 1
                if s[l] != alt2[l]:
                    diff2 -= 1
                l += 1
                
            if (r - l + 1) == n:
                res = min(res, diff1, diff2)
        
        return res
            
            
