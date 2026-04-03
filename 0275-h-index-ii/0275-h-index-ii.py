class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        left = -1
        right = len(citations)

        while left + 1 < right:

            mid = (left + right)//2

            if citations[mid] >= mid + 1 and mid + 1 <= len(citations) - mid:
                left = mid
            else:
                right = mid
            print(mid)
        return left + 1