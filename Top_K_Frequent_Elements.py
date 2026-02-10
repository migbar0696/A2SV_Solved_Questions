class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        freqe = Counter(nums)
        rsorted = sorted(freqe.items(),  key =  lambda item:item[1], reverse = True)


        res = []
        i = 1
        for num, freq in rsorted:
            print(num)
            if i <= k:
                res.append(num)
            i += 1
        
        return res



