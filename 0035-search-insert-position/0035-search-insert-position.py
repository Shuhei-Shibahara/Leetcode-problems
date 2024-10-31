class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #binary search to find target
        #if we do not find it, we return the index in place which would be the current smaller number
        
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return l

