class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l, r, m = [], [], []
        for num in nums:
            if num == pivot:
                m.append(num)
            elif num < pivot:
                l.append(num)
            else:
                r.append(num)
        
        return l + m + r
