class Solution:
    def addDigits(self, num: int) -> int:
        # If the number is 0, return 0
        if num == 0:
            return 0
        
        # Digital root calculation
        return 1 + (num - 1) % 9
