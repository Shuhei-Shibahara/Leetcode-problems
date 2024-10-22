class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #looking for the k closest point
        #lets find the distance and put them through heap.min
        #and subtract 1 from k every time until k = 0
        minHeap = []
        for x,y in points:
            dist = (x**2)  + (y**2)
            minHeap.append([dist,x,y])
        
        heapq.heapify(minHeap)
        res = []
        while k:
            dist,x,y = heapq.heappop(minHeap)
            res.append([x,y])
            k -= 1
        
        return res