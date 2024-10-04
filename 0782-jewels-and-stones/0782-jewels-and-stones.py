class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        check = {}
        total = 0
        for i in jewels:
            check[i] = 0
        
        for i in stones:
            if i in check:
                total += 1
        
        return total