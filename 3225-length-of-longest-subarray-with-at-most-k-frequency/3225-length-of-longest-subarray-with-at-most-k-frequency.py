class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l = 0
        counter = defaultdict(int)
        result = 0

        for r in range(len(nums)):
            counter[nums[r]] += 1

            while counter[nums[r]] > k:
                counter[nums[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
        
        return result