class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        flag = False

        while low <= high:
            mid = low + ((high - low ) // 2)

            if nums[mid] == target:
                flag = True
                break
            
            if low == high:
                break

            if nums[mid] > target:
                high = mid - 1
            
            if nums[mid] < target:
                low = mid + 1
        
        if flag:
            return mid
        else:
            return -1
            
            

