class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        freqc = Counter(answers)

        ans = 0

        for key, val in freqc.items():
            ans += ceil(val /( key + 1)) * (key + 1)
        
        return ans