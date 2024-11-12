class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        smallest = float('inf')
        total = 0
        l = 0

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                # smallest = min(smallest, r - l + 1)
                if r - l + 1 < smallest:
                    smallest = r - l + 1
                total -= nums[l]
                l += 1
        
        return smallest
