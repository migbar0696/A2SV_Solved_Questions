class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        listn = []

        stnum = "123456789"
        n = 9

        for i in range(9):
            for j in range(n - 1):
                listn.append(int(stnum[j:n]))
            n -= 1
        listn.sort()
        return listn[bisect_left(listn, low):bisect_right(listn, high)]
        
