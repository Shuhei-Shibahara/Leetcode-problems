class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #2pointer 
        #l pointer will be moving once if finds a new non duplicate number
        #r pointer will be the one searching for a new number that is non duplicate

        l = 0

        for r in range(1,len(nums)):

            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]

        return l + 1