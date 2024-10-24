class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        #since we want to check every 2k character we can use a for loop and increment every 2k
        #look through the 2k and switch the first k chracters
        #before that we need to make s into a list so we can change characters places
        
        s = list(s)
        
        for i in range(0, len(s) - 1, 2*k):
            s[i:i+k] = reversed(s[i:i+k])
            print(s)

        
        return ''.join(s)
            