class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        minn = 0

        maxn = float("-inf")
        sumn = 0
        for i in range(len(nums)):
            sumn += nums[i]
            
            maxn = max(maxn, sumn - minn)
            minn = min(minn, sumn)
        return maxn 