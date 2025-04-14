class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ROWS,COLS = len(matrix), len(matrix[0])
        res = 0
        prev_height = [0] * COLS

        for r in range(ROWS):
            heights = matrix[r][:]
            for c in range(COLS):
                if heights[c] > 0:
                    heights[c] += prev_height[c]
                
            sorted_height = sorted(heights, reverse=True)
            for i in range(COLS):
                res = max(res, (i+1)*sorted_height[i])
            prev_height = heights
        
        return res
