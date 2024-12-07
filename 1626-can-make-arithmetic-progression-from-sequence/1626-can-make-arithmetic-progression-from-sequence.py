class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) < 2:
            return True  # Edge case: arrays with less than 2 elements
        
        arr.sort()  # Sort the array
        
        diff = arr[1] - arr[0]  # Expected difference
        
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False
        
        return True
        