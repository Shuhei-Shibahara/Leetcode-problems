class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #two pointer 
        #left start at index 0 and right start at the last index 
        #replace the characters and the increment left and decrement right by 1

        l = 0
        r = len(s) - 1

        while l < r:
            s[l],s[r] = s[r],s[l]
            l += 1
            r -= 1
        
        return s