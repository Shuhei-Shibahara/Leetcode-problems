class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k:
            ele = nums.pop()
            nums.insert(0,ele)
            k -= 1
