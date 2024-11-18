class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #bucket sort
        #since there are only 3 integers we can look to count all 3 integers in nums and reassingn them in nums

        count = Counter(nums)
        print(count)
        num = 0
        i = 0
        while num < 3:
            
            while count[num] > 0:
                nums[i] = num
                count[num] -= 1
                i += 1
            num += 1
        
        return nums
        