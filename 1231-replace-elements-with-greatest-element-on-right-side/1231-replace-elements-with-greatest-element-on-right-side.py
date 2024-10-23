class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #reverse iterate
        #looking from the right, replace it with the previous max, and update the previous max with the max between the current index

        prevMax = -1

        for i in range(len(arr)-1, -1, -1):
            currNum = arr[i]
            arr[i] = prevMax
            prevMax = max(currNum, prevMax)
        
        return arr