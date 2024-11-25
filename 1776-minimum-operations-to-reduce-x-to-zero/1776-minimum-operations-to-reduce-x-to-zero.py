class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        cur_sum = 0
        l = 0
        max_window = -1

        for i in range(len(nums)):
            cur_sum += nums[i]
            while l <= i and cur_sum > target:
                cur_sum -= nums[l]
                l += 1
            if cur_sum == target:
                max_window = max(max_window, i - l + 1 )
            
            
        
        return max_window if max_window == -1 else len(nums) - max_window
