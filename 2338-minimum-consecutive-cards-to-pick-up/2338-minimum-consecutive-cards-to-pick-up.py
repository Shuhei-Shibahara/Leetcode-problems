class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        graph = {}
        ans = float('inf')
        for i,card in enumerate(cards):
            if card not in graph:
                graph[card] = i
            else:
                ans = min(ans, i - graph[card] + 1)
                graph[card] = i 

        return -1 if ans == float('inf') else ans
