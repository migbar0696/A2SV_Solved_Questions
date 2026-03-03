class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dictn = Counter([0])

        sumn = 0
        cnt = 0
        for i in range(len(nums)):
            sumn += nums[i]

            if sumn - k in dictn:
                cnt += dictn[sumn - k]
            
            dictn[sumn] += 1
        return cnt