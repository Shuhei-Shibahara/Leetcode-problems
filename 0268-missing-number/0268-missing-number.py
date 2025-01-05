class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        print(count)

        for i in range(len(nums)+1):
            if i not in count:
                return i
        