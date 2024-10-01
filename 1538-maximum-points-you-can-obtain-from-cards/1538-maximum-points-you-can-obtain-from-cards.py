class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        if k >= len(cardPoints):
            return total
        
        total_max = 0
        state = 0
        start = 0

        for end in range(len(cardPoints)):
            state += cardPoints[end]

            if end - start + 1 == len(cardPoints) - k:
                total_max = max(total_max, total - state)
                state -= cardPoints[start]
                start += 1
        
        return total_max