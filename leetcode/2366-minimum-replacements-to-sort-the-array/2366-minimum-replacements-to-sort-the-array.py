class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        minn = nums[-1]

        ans = 0

        for i in range(len(nums) - 1, -1, -1):
            nump = ceil(nums[i] / minn)

            numn = nums[i] // nump

            minn = min(minn, numn)

            ans += nump - 1  
        return ans          
            