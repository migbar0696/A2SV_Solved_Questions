class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        cnt = 0

        for patt in patterns:
            if patt in word:
                cnt += 1
        return cnt