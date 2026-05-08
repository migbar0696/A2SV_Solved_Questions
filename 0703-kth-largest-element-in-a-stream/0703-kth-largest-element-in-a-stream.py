class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums

        heapify(self.minHeap)
        while(len(self.minHeap) > k):
            heappop(self.minHeap)

    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k:
            heappush(self.minHeap,val)
        elif val > self.minHeap[0] :
            heappush(self.minHeap,val)
            heappop(self.minHeap)
        

        
        return self.minHeap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)