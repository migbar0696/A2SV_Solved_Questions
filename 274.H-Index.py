class Solution:
    def hIndex(self, citations: List[int]) -> int:
        maxcite = float("-inf")

        citations.sort(reverse= True)
        n = len(citations)

        for i in range(n):
            if citations[i] >= i + 1  :
                maxcite = max(maxcite, i + 1)
        
        return maxcite if maxcite != float("-inf") else 0
