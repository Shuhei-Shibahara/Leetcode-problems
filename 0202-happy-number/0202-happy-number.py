class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  # To track numbers we've already processed
        
        while n != 1 and n not in seen:
            seen.add(n)  # Add the current number to the set
            digits = [int(digit) for digit in str(n)]  # Split number into digits
            n = sum(digit ** 2 for digit in digits)  # Compute sum of squares of digits
        
        return n == 1  # Return True if n is 1, otherwise False