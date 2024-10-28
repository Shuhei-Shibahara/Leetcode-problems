class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.backspaced(s) == self.backspaced(t)

    def backspaced(self, s):
        stack = []
        s = list(s)
        while s:
            cur = s.pop(0)
            if cur != '#':
                stack.append(cur)
            else:
                if stack:
                    stack.pop()
        
        return ''.join(stack)