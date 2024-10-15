class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        #we will need to find the smallest number in nums by doing min(nums)
        #we will also need to find the index of that in nums
        #do a range and go through k
        #return nums

        for _ in range(k):
            idx = nums.index(min(nums))
            nums[idx] *= multiplier
        
        return nums