class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        left = -1
        right = len(citations)

        while left + 1 < right:

            mid = (left + right)//2

            if citations[mid] >= len(citations) - mid :
                right = mid
            else:
                left = mid
            print(mid)
            print(right)
        return len(citations) - right 