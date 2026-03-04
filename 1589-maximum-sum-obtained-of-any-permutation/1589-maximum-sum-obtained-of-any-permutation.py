class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        maxn = 0
        sumn = 0

        for start, end in requests:
            maxn = max(maxn, end)
        
        pre_sum = [0] * (maxn + 2)

        for start, end in requests:
            pre_sum[start] += 1
            pre_sum[end + 1] -= 1
        
        for i in range(1, len(pre_sum)):
            pre_sum[i] = pre_sum[i] + pre_sum[i - 1]
        
        pre_sum.sort(reverse=True)
        nums.sort(reverse=True)
        
        lenn = min(len(pre_sum), len(nums))
        for i in range(lenn):
            sumn += (pre_sum[i] * nums[i])

        print(10 ^ 9)         
        return sumn % (pow(10, 9) + 7)

