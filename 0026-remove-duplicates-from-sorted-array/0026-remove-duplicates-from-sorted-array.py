class Solution:
    def removeDuplicates(self, nums: List[int]) -> List[int]:
        #return k elements that they are gonna check
        #use 2 pointer method that way we can keep track of how many indexes to check
        #we must change the array nums

        if not nums:
            return 0

        j = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        
        return j