class Solution:
    def validPalindrome(self, s: str) -> bool:
        #we use 2 pointers
        #l will be the start and r will be the end
        #we go down the list, if we find one that doesnt match
        #we can do an if statement checking if the one next to it is a possible match
        #we can delete that one 

        #[a,b,b,d,a]
        #l = 0 r = 4 
        #l = 1 r = 3
        #
        s = list(s)
        l = 0
        r = len(s)-1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return self.is_palindrome(s,l+1,r) or self.is_palindrome(s,l,r-1)
        
        return True

    def is_palindrome(self,s,l,r):

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        
        return True


