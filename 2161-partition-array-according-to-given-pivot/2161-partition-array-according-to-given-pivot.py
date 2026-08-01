class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        firs = []
        midd = []
        last = []
        for num in nums:
            if num < pivot:
                firs.append(num)
            elif num > pivot:
                last.append(num)
            else:
                midd.append(num)
        return firs + midd + last