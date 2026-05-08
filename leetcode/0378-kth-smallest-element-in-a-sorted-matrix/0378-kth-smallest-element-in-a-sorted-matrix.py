class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        arr = []

        for each in matrix:
            arr.extend(each)

        heapify(arr)
        
        for _ in range(k - 1):
            heappop(arr)
        return arr[0]