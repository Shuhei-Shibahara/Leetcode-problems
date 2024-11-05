
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort the array first
        l = 0
        total = 0  # Sum of elements in the current window
        maxCount = 0
        
        for r in range(len(nums)):
            total += nums[r]  # Add the current element to the total
            
            # Calculate the current window size
            while nums[r] * (r - l + 1) - total > k:
                # If the total cost to make all elements in the window equal to nums[r] exceeds k,
                # move the left pointer to reduce the window size
                total -= nums[l]  # Remove the leftmost element
                l += 1  # Move left pointer to the right
            
            # The number of elements in the current window is (r - l + 1)
            maxCount = max(maxCount, r - l + 1)  # Update maxCount
            
        return maxCount