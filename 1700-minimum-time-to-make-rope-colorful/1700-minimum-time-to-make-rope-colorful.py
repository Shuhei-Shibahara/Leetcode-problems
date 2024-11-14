class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        l,total = 0,0

        for r in range(1,len(colors)):
            
            if colors[l] == colors[r]:
                if neededTime[l] < neededTime[r]:
                    total += neededTime[l]
                    l = r
                else:
                    total += neededTime[r]
            else:
                l = r
        return total
