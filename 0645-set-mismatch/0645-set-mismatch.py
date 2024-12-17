class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        v = [0] * (n+1)
        mis, dup = 0,0

        for num in nums:
            v[num] += 1
        
        for i in range(1,len(v)):
            if v[i] == 2:
                dup = i
            if v[i] == 0:
                mis = i
        
        return [dup,mis]