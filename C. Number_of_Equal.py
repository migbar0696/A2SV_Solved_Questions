from collections import Counter
n, m = map(int, input().split())
listn = list(map(int, input().split()))
listm = list(map(int, input().split()))

freqn = Counter(listn)
freqm = Counter(listm)

suma = 0
for key in freqn:
    suma += freqn[key] * freqm[key]


print(suma)
