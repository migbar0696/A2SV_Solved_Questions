class Solution:
    def singleNumber(self, nums: List[int]) -> int:

#         ans = nums[0]
#         n = len(nums)
#         for i in range(1, n):
#             ans = ans ^ nums[i]
#         return ans

        # or

        ans = nums[0]
        
        for num in nums[1:]:
            ans = ans ^ num
        
        return ans