class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        from collections import Counter
        freqw1 = Counter(word1)
        freqw2 = Counter(word2)
        freqvalue1 = Counter(freqw1.values())
        freqvalue2 = Counter(freqw2.values())

        return set(word1) == set(word2) and freqvalue1 == freqvalue2

    


        # if set(word1) == set(word2) and sorted(freqw1.values()) == sorted(freqw2.values()):
        #     return True
        # else:
        #     return False
