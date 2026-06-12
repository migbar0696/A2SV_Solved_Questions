class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        ans = []
        for i in range(len(A)):
            cnt = 0
            for j in range(i + 1):
                if A[j] in B[:i + 1]:
                    cnt += 1
            ans.append(cnt)

        return ans
