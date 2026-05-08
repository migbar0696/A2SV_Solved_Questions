class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums = [ -x for x in nums]
        heapify(nums)
        self.arr2 = []
        for _ in range(min(self.k ,len(nums))):
            self.num = heappop(nums)
            heappush(self.arr2, -self.num)


    def add(self, val: int) -> int:
        if len(self.arr2) < self.k:
            heappush(self.arr2,val)
        elif val > self.arr2[0] :
            heappush(self.arr2,val)
            heappop(self.arr2)
        

        
        return self.arr2[0]
        

            # BETTER SOLUTION

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
