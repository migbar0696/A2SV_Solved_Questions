class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        maxl = float("-inf")
        l = 0
        dictb  = Counter()
        n = len(nums)
        res = []
        for r in range(n):
            dictb[nums[r]] += 1

            while (r - l + 1 ) - dictb[1] > 1:
                dictb[nums[l]] -= 1
                res.append(dictb[l])
                l += 1

            maxl = max(maxl, r - l )
        print(res)
        return maxl