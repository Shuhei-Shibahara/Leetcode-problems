class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)
        res = 0

        def dfs(word):
            nonlocal res 
            if word:
                res += 1
            
            for i in count:
                if count[i] != 0:
                    count[i] -= 1
                    dfs(word + i)
                    count[i] += 1
        
        dfs('')
        return res