class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        #we will use stack for this
        #run push commands and fill the array
        #if the last number on the stack is the popped first number then we can pop
        #if the stack is empty then we will return True
        
        stack = []
        j = 0
        for i in pushed:
            stack.append(i)
            while stack != [] and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        
        return stack == []