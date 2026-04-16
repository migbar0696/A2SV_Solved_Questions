class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1
            else:
                ans.append(abs(num))
        
        return ans