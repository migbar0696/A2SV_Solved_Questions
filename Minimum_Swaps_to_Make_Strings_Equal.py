class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = 0
        yx = 0

        n = len(s1)

        for i in range(n):
            if s1[i] == "x" and s2[i] =="y":
                xy += 1
            elif s1[i] == "y" and s2[i] == "x":
                yx += 1

        if xy % 2 == 0 and yx % 2 == 0:
            return xy // 2 + yx // 2
        elif xy % 2 and yx % 2:
            return (xy // 2) + (yx // 2 ) + 2
        else:
            return -1
        
