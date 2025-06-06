class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0
        while l < r:
            width = r - l  
            height_val = min(height[l], height[r])
            area = width * height_val
            max_area = max(area, max_area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area 