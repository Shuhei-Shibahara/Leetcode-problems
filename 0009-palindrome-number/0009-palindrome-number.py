class Solution:
    def isPalindrome(self, x: int) -> bool:
        word = str(x)
        l = 0
        r = len(word) - 1
        while l < r:
            if word[l] == word[r]:
                l += 1 
                r -= 1
            else:
                return False
        
        return True