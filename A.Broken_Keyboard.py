t = int(input())

for i in range(t):
    s = input()
    l = 0
    r = 0
    n = len(s)
    sets = set()
    while r < n:
        while r < n and  s[l] == s[r]:
            r += 1
        if (r - l ) % 2:
            sets.add(s[l])
        l = r
    print("".join(sorted(list(sets))))
