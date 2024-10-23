class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        #two pointer
        #first we check if left pointer is even
        #then we can move left pointer over until we find an odd
        #then we move right pointer until we find even and then we swap
        #continue this until right hits end of array

        l = 0
        for r in range(len(nums)):
            if nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums