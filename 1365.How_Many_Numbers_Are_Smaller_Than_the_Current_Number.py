class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        dictnums = Counter(nums)

        sorteddictnums = sorted(dictnums.items())
        dictans = defaultdict(int)
        sumv = 0
        for num, val in sorteddictnums:
            dictans[num] = sumv

            sumv += val
        
        for num in nums:
            res.append(dictans[num])

        return res
