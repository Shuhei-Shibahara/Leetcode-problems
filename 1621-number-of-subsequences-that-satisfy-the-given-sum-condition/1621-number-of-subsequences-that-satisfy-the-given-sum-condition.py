class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        #2 pointer
        #sort the nums 
        nums.sort()
        res = 0
        mod = (10**9 + 7)
        r = len(nums) - 1

        for i, left in enumerate(nums):

            while (left + nums[r]) > target and r >= i:
                r -= 1
            if r >= i:
                res += (2**(r - i))
                res %= (mod)
        
        return res
