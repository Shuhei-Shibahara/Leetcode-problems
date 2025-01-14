class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        #have a way to check how many zeroes to replace
        #need to have the sum of both arrays to equal each other
        #if it doesn then it should be -1
        #since we want the minimum sum while replacing the zero we can add onto the sum by 1
        #we can take the larger of the sum and return that only if there are 0s 
        zero1, zero2 = 0, 0
        sum1, sum2 = 0, 0

        for num in nums1:
            if num == 0:
                zero1 += 1
            sum1 += num

        for num in nums2:
            if num == 0:
                zero2 += 1
            sum2 += num
        
        sum1 += 1 * zero1
        sum2 += 1 * zero2

        if sum1 > sum2:
            return sum1 if zero2 else -1
        elif sum2 > sum1:
            return sum2 if zero1 else -1
        
        return sum1

