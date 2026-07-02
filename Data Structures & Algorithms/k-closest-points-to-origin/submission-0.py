
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            distance_squared = x*x + y*y
            heapq.heappush(heap , (-distance_squared , x , y))
            if  len(heap) > k:
                heapq.heappop(heap)

        return [[x,y] for (_ , x , y) in heap]        

        