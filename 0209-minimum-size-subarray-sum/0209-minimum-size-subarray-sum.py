class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #sliding window method
        #we will go through the list and keep adding more numbers to the right of it
        #check if the number is equal to target
        #if it becomes larger then remove left 

        l = 0
        total = 0
        res = float('inf')
        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
        
        return res if res != float('inf') else 0
            
