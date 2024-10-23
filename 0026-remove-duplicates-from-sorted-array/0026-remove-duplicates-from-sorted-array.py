class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # two pointer method
        # we are going to iterate through the array 
        # while checking with left pointer we will move the right one checking if it is a duplicate
        #if it is a duplicate we will keep moving right 
        #else we will move left pointer 1 and change that to the new number that we have
        #at the end we will return l since that indicates k elemnts that are unique

        l = 0
        r = 1

        while r < len(nums):

            if nums[l] == nums[r]:
                r += 1
            else:
                l += 1
                nums[l] = nums[r]


        return l + 1