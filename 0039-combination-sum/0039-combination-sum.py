class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #backtracking here since we are looking for subsets
        #we need to have one including the number that it currently has and one wihtout so that it will remove duplciate answers

        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i >= len(candidates):
                return
            
            cur.append(candidates[i])
            dfs(i,cur, total + candidates[i])
            cur.pop()
            dfs(i+1, cur, total)
        dfs(0,[],0)
        return res