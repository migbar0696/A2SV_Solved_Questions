# print(pre_sum)

pre_sum1 = [[0 for i in range(w + 1)] for j in range(h + 1)]

for i in range(h):
    for j in range(w):
        if i > 0:
            if arr[i][j] == "." and arr[i - 1][j] == ".":
                pre_sum[i][j] += 1
        
        if j > 0:
            if arr[i][j] == "." and arr[i ][j - 1] == ".":
                pre_sum[i][j] += 1

for i in range(1, h + 1):
    for j in range(1, w + 1):
        pre_sum1[i][j] = pre_sum1[i - 1][j] + pre_sum1[i][j - 1] - pre_sum1[i - 1][j - 1] + pre_sum[i - 1][j - 1]




# print(pre_sum)
# print(pre_sum1)


for r1, c1, r2, c2 in arri:
    cnt = 0
    if r1 - 1 > 0:
        for i in range(c1 - 1, c2):
            if arr[r1 - 1][i] == "." and arr[r1 - 2][i] == ".":
                cnt += 1
    if c1 - 1 > 0:
        for j in range(r1 - 1, r2):
            if arr[j][c1 - 1] == "." and arr[j][c1 - 2] == ".":
                cnt += 1
    # print("cnt", cnt)
    
    sumn = pre_sum1[r2][ c2] - pre_sum1[r1 - 1][c2] - pre_sum1[r2][ c1 - 1] + pre_sum1[r1 - 1][c1 - 1]
    
    print(sumn - cnt )