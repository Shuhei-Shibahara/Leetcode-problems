class Solution:
    def addDigits(self, num: int) -> int:
        # Continue summing digits until a single-digit number is obtained
        while num >= 10:
            num = sum(int(digit) for digit in str(num))
        
        return num
