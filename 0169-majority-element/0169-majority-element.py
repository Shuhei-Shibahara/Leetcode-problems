class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        # Return the key with the highest value
        return max(count, key=count.get)