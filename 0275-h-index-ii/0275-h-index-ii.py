class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        left = 0
        right = len(citations)

        while left + 1 < right:

            mid = (left + right)//2

            if citations[mid] <= mid + 1:
                left = mid
            else:
                right = mid
        return citations[left]