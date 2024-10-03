class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        highest = 0

        for i in accounts:
            highest = max(highest, sum(i))
        
        return highest