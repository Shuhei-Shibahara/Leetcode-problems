class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #we need a stack
        #we keep adding numbers into this stack until we hit a non integer
        #once we hit that we remove the last 2 integers and do the expression and append that back into the stack

        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                a,b = stack.pop(),stack.pop()
                stack.append(b-a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a,b = stack.pop(),stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(c))
        
        return stack[-1]

        
        return stack[-1]