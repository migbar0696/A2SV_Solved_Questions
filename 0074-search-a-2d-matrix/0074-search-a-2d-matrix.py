class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = -1
        right = len(matrix) * len(matrix[0]) 
        n = len(matrix[0])

        while left + 1 < right:
            mid = left + (right - left)//2

            if matrix[mid//n][mid%n] < target:
                left = mid
            elif matrix[mid//n][mid%n] > target:
                right = mid
            else:
                return True
        return False