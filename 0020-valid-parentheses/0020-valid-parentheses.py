class Solution:
    #this can be solved with Stacking
    #create a hash map with open and close of brackets
    #if its an open then we put in stack
    #if its a close then we pop the first one and compare
    #if this doesnt match then False
    #if it does then move on
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {
            ')' : '(',
            ']' : '[',
            '}' : '{',
        }

        for char in s:
            if char in matching.values():
                stack.append(char)
            elif not stack or matching[char] != stack.pop():
                return False
        
        return not stack
