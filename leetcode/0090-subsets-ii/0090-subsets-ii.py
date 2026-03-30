class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(ind, arr):

            if len(arr) > len(nums):
                return
            if sorted(arr) not in ans:
                ans.append(sorted(arr[:]))

            for i in range(ind, len(nums)):
                arr.append(nums[i])
                backtrack(i + 1, arr)
                arr.pop()
            
            return ans
        
        return backtrack(0, [])