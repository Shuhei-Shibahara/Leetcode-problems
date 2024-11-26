class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #two pointers 
        #we will move the down the nums and look for any non duplicates
        #l will be holding the index of the last non duplicate
        #return l + 1

        l = 0

        for r in range(len(nums)):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
            
        return l + 1