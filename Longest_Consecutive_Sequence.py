class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxc = float("-inf")
        setnum = set(nums)
        cnt = 1

        for num in setnum:
            cnt = 1
            if num - 1 not in setnum:
                while True:
                    setans.add(num)
                    if num + cnt in setnum   :
                        cnt += 1
                    else:
                        break
                maxc = max(maxc, cnt)
        return maxc if maxc != float("-inf") else 0
                
