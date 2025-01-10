class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = len(num) - 1

        while i >= 0:
            if int(num[i]) % 2 != 0:  # Check if the digit at index `i` is odd
                return num[0:i + 1]
            i -= 1
        
        return ""