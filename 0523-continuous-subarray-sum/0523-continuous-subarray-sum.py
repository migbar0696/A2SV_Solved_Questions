class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        dictn = Counter()
        dictn[0] = 0
        

        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
        
        for i in range(len(nums)):
            if (nums[i] % k ) not in dictn:
                dictn[nums[i] % k] = i + 1
                
            if (nums[i] % k) in dictn and (i - (dictn[nums[i] % k])) > 0:
                return True
            
        
        return False