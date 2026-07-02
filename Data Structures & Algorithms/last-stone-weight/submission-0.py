import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [ -s for s in stones]
        heapq.heapify(heap)

        while len(heap) >= 2 :
            largest = - heapq.heappop(heap)
            second_largest = - heapq.heappop(heap)

            if largest != second_largest:
                heapq.heappush(heap , - (largest - second_largest))
        return -heap[0] if heap else 0      



        