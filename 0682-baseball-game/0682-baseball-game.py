class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for operation in operations:
            if operation.lstrip("-").isdigit():  
                stack.append(int(operation))
            elif operation == "+":
                if len(stack) >= 2:  
                    stack.append(stack[-1] + stack[-2])
            elif operation == "D":
                if stack: 
                    stack.append(2 * stack[-1])
            elif operation == "C":
                if stack:  
                    stack.pop()
        
        return sum(stack)
