class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        dictn = defaultdict(int)
        for num in nums:
            for ch in str(num):
                dictn[ch] += 1
        
        return dictn[str(digit)]