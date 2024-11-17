class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        check = {}
        res = [-1] * len(nums1)
        for i, num in enumerate(nums1):
            check[num] = i
        
        for i in range(len(nums2)):
            if nums2[i] not in check:
                continue
            
            for j in range(i + 1,len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = check[nums2[i]]
                    res[idx] = nums2[j]
                    break
        
        return res
            
