class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for n in nums:
            self.add(n)
        
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]

















    # # Time  O(N log k)
    # def __init__(self, k: int, nums: List[int]):
    #     self.heap = []
    #     self.k = k
    #     for n in nums:
    #         self.add(n)

    # def add(self, val: int) -> int:
    #     if len(self.heap) < self.k:
    #         heapq.heappush(self.heap, val)
    #     else:
    #         heapq.heappushpop(self.heap, val)
        
    #     return self.heap[0]



    # # With heapify O(N) time
    # def __init__(self, k: int, nums: List[int]):
    #     self.heap = nums
    #     self.k = k
    #     heapq.heapify(self.heap)
    #     while len(self.heap) > k:
    #         heapq.heappop(self.heap)
        
