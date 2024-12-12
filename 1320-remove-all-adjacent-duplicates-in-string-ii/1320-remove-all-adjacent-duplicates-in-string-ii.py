class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        #we are going to use a staack
        #in the stack we are keeping count of character and count of the letters
        #if the count of letter ever hits k we pop that from our stack

        stack = [] #char count

        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c,1])
            
            
            if stack[-1][1] == k:
                stack.pop()
        res = ""
        for char,count in stack:
            res += char * count
        
        return res