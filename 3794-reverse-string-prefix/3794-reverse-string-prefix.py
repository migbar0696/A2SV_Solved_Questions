class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        lstn = list(s)
        lstn[:k] = lstn[:k][::-1]

        return "".join(lstn)