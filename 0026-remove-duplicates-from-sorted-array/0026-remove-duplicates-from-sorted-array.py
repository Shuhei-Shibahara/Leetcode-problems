class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #were going to have the array have no duplicates
        #2 pointer
        #l keep track of indicies only move when its not a duplicate
        #r pointer will keep checking with the left pointer to see if ther are duplicates

        l = 0
        for r in range(1,len(nums)):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
        
        return l + 1

        
