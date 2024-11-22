class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l, r = 0, sum(nums)

        for i, ele in enumerate(nums):
            r -= ele
            if l == r:
                return i
            
            l += ele
        
        return -1
