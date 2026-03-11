class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from collections import deque
        moni = deque()
        mond = deque()
        
        l = 0
        maxl = 0
        for r in range(len(nums)):
            
            while moni and nums[r] < moni[-1]:
                moni.pop()
            
            while mond and nums[r] > mond[-1]:
                mond.pop()
            
            moni.append(nums[r])
            mond.append(nums[r])

            while moni and mond and abs(moni[0] - mond[0]) > limit:
                if nums[l] == moni[0]:
                    moni.popleft()
                
                if nums[l] == mond[0]:
                    mond.popleft()
                
                l += 1
            maxl = max(maxl, r - l + 1)
        
        return maxl
