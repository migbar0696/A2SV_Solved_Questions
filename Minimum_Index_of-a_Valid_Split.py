class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        from collections import Counter

        freqn = Counter(nums)

        dominant = max(freqn, key = freqn.get)
        n = len(nums)
        cnt = 0
        
        for i in range(n):
            if nums[i] == dominant:
                cnt += 1
            
            if cnt > ((i + 1) // 2) and (freqn[dominant] - cnt) > (n - (i + 1)) //2:

                return i
        
        return - 1
