class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        numgoodk = 0
        dictn = Counter()
        l = 0
        for r in range(len(nums)):
            dictn[nums[r]] += 1

            while  len(dictn) > k:
                dictn[nums[l]] -= 1

                if dictn[nums[l]] == 0:
                    del dictn[nums[l]]
                l += 1
            numgoodk += r - l + 1
        

        numgoodk2 = 0
        dictn2 = Counter()
        l2 = 0
        for r2 in range(len(nums)):
            dictn2[nums[r2]] += 1

            while  len(dictn2) > k - 1:
                dictn2[nums[l2]] -= 1

                if dictn2[nums[l2]] == 0:
                    del dictn2[nums[l2]]
                l2 += 1
            numgoodk2 += r2 - l2 + 1
        
        return numgoodk - numgoodk2
