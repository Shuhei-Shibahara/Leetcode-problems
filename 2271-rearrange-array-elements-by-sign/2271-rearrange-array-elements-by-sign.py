class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        l,r = 0,1
        for i in nums:
            if i >= 0:
                res[l] = i
                l += 2
            else:
                res[r] = i
                r += 2
        
        nums = res
        return nums
