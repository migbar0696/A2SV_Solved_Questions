class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(ind, arr):
            if ind > len(nums):
                return
            if arr and len(arr) >= 2 and arr not in ans:
                ans.append(arr[:])
            for i in range(ind, len(nums)):
                if arr:
                    if arr[-1] <= nums[i]:
                        arr.append(nums[i])
                        # print(nums[i])
                        backtrack(i + 1, arr)
                        arr.pop()
                else:
                    arr.append(nums[i])
                    # print(nums[i])
                    backtrack(i + 1, arr)
                    arr.pop()
        
        backtrack(0, [])
        return ans
            
