class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        check = {}
        for num in nums:
            if num not in check:
                check[num] = 1
        
        res = []

        for i in range(1, len(nums) + 1):
            if i not in check:
                res.append(i)
        
        return res