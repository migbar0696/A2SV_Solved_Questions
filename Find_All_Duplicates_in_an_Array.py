class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []

        for ele in nums:
            if nums[abs(ele) - 1] > 0:
                nums[abs(ele) - 1] *= -1
            else:
                ans.append(abs(ele))
        return ans
