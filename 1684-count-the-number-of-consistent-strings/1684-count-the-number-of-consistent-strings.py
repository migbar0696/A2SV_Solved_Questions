class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        cnt = 0
        for each in words :
            if all(ch in allowed for ch in each):
                cnt += 1
        
        return cnt

            