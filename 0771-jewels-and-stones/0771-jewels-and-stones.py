class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        for ch in jewels:
            ans += stones.count(ch)
        return ans
        