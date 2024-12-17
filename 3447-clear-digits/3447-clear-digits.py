class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for i in s:
            if '0' <= i <= '9' and stack:
                stack.pop()
            else:
                stack.append(i)
        
        s = ''.join(stack)
        return s