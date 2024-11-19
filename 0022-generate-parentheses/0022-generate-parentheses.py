class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(open,close,arr):
            if open == close == n:
                res.append("".join(arr.copy()))
                return
            
            if close < open:
                arr.append(')')
                dfs(open,close + 1, arr)
                arr.pop()
            
            if open < n:
                arr.append('(')
                dfs(open+1,close,arr)
                arr.pop()
        
        dfs(0,0,[])
        return res