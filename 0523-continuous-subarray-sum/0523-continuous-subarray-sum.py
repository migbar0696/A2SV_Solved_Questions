class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        dictn = Counter()
        pre_sum = [0]

        for i in range(len(nums)):
            pre_sum.append(pre_sum[-1] + nums[i])
        

        for i in range(len(pre_sum)):
            if pre_sum[i] % k in dictn and (i - dictn[pre_sum[i] % k]) > 1:
                return True
            
            if pre_sum[i] % k not in dictn:
                dictn[pre_sum[i] % k] = i
        
        return False
        
