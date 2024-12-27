class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        total = 0
        for i in range(len(nums)):
            nums[i].sort()
        for i in range(len(nums[0])):
            x = 0
            for j in range(len(nums)):
                x = max(x,nums[j][i])
            total += x
        
        return total  