class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        #were going to use heap to keep track of the highest differential 
        #whenever we use too many bricks we will need to see if their are ladders and if there are then we can pop highest heap and add back bricks
        #if there are no ladders thats the index we are going to return
        #if we go throuhg the whole heights then we will return len of height

        heap = []

        for i in range(len(heights) - 1):
            diff = heights[i+1] - heights[i]
            if diff <= 0:
                continue
            bricks -= diff
            heapq.heappush(heap, -diff)
            if bricks < 0:
                if ladders == 0:
                    return i
                ladders -= 1
                bricks += -heapq.heappop(heap)
        return len(heights) - 1


            