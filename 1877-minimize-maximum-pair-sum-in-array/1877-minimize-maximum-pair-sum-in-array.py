class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxn = 0
        n = len(nums)

        for i in range(n):
            maxn = max(maxn, nums[i] + nums[n - 1 - i])

        return maxn