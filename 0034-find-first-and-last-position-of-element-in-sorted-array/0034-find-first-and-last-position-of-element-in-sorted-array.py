class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            return [-1, -1]
        left = -1
        right = len(nums) - 1
        flag = False
        ans = []

        while left + 1 <right:
            mid = (left + right)//2

            if nums[mid] >= target:
                right = mid 
            if nums[mid] < target:
                left = mid 

        print(left, right)
            
        if nums[right] == target:
            ans.append(right)
        else:
            ans.append(-1)

        
            
        left = 0
        right = len(nums) 
        flag = False

        while left + 1 <right:
            mid = (left + right)//2

            if nums[mid] <= target:
                left = mid 

            if nums[mid] > target:
                right = mid 
            
        if nums[left] == target:
            ans.append(left)
        else:
            ans.append(-1)

        return ans