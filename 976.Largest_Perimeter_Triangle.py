class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        maxa = float("-inf")

        for i in range(n - 2):
            if nums[i] + nums[i + 1] > nums[i + 2]:
                maxa = max(maxa,nums[i] + nums[i + 1] + nums[i + 2] )
        
        return maxa if maxa != float("-inf") else 0
