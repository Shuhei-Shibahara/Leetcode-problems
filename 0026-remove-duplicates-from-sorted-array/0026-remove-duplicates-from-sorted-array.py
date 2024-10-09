class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #were going to iterate through nums to check if the previous value was equal 
        #if we find one that doesnt equal we replace that value with an index checker that we will initailize
        
        j = 1

        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        
        return j