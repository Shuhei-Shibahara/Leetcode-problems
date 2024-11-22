class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #use stack and put in the temperature and index
        #we go through temperature and whenever we find a temperature that is higher than stack thats when we will put the input back in

        res = [0] * len(temperatures)
        stack = [] #[temp,i]

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stackT, stackI = stack.pop()
                res[stackI] = i - stackI
            
            stack.append([t,i])
            
        return res