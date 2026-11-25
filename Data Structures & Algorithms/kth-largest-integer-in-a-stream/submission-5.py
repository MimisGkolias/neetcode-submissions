class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for n in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap, n)
            else:
                heapq.heappushpop(self.heap, n)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            heapq.heappushpop(self.heap, val)
        
        return self.heap[0]
