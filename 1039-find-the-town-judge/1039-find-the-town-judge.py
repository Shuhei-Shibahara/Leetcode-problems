class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        for x,y in trust:
            incoming[y] += 1
            outgoing[x] += 1
        
        for i in range(1, n+1):
            if outgoing[i] == 0 and incoming[i] == n-1:
                return i
        return -1