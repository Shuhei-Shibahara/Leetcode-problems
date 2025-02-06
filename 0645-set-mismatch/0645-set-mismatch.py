class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = [0] * (n+1)

        for i in nums:
            count[i] += 1

        extra = 0
        none = 0
        for i in range(1, len(count)):
            if count[i] == 2:
                extra = i
            if count[i] == 0:
                none = i
        
        return [extra,none]

