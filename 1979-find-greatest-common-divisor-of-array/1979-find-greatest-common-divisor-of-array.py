class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minn = min(nums)
        maxn = max(nums)
        sets = set()
        setl = set()

        for i in range(1, maxn + 1):
            if minn % i == 0:
                sets.add(i)
            if maxn % i == 0:
                setl.add(i)
        newst = sets.intersection(setl) 

        return max(newst)
