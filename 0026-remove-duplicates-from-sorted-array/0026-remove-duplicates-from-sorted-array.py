class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #were going to use 2 pointer here
        #we keep moving right pointer until we find one that is not identical to l pointer
        #then we move left pointer 1 and then change that with the value of right pointer
        #do this til end of the list

        l = 0

        for r in range(len(nums)):

            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
        
        return l + 1

