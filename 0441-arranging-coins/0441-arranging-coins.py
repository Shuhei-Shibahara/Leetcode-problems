class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        while n > 0:
            n -= i
            i += 1

        
        return i-1 if n == 0 else i - 2
#n
#i = 1 n = 5
#n = 4 i = 2
#n = 2 i = 3
#n = -1 i = 4