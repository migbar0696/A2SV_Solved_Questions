class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        arr = []

        n  = len(matrix)
        
        for i in range(n):
            heappush(arr, (matrix[i][0], i, 0))

        for _ in range(k):
            if arr:
                num, row, col = heappop(arr)
                print(col, n - 1)
        
            if col < n - 1:
                heappush(arr,(matrix[row][col + 1],row, col + 1))
                
            

        return num