class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        beg = 0
        odd = 0
        count = 0
        subarray_count = 0

        for right in range(len(nums)):
            # Check if nums[right] is odd
            if nums[right] % 2 != 0:
                odd += 1

            # When we have exactly k odd numbers
            if odd == k:
                subarray_count = 0
                # Count all subarrays from beg to right that have k odd numbers
                while odd == k:
                    if nums[beg] % 2 != 0:
                        odd -= 1
                    beg += 1
                    subarray_count += 1
                count += subarray_count
            else:
                # If still not k odd numbers, add the previously counted subarrays
                count += subarray_count

        return count

