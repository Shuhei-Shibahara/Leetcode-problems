class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        check = defaultdict(int)
        res = 0

        for x, y in dominoes:
            key = tuple(sorted((x, y)))  
            res += check[key] 
            check[key] += 1  

        return res