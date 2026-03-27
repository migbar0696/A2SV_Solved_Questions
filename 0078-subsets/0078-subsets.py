class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        subset = []

        def backtrack(ind):

            if ind == len(nums):
                ans.append(subset.copy())
                return
            
            subset.append(nums[ind])
            backtrack(ind + 1)
            subset.pop()
            backtrack(ind + 1)

            return ans
            
        
        return backtrack(0)

