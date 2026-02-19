import math
n = int(input())
 
listn = sorted(list(map(int, input().split())))
print(listn[math.ceil((n / 2)) - 1 ])
