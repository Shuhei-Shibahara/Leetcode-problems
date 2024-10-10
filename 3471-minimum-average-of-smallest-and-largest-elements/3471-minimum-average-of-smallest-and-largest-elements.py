class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        avg = float(inf)
        l = 0
        r = len(nums) - 1
        nums.sort()

        while l < r:
            cur_avg = (nums[l] + nums[r] )/ 2
            avg = min(avg, cur_avg)
            l += 1
            r -= 1
        
        return avg