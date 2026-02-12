matrix = []
for i in range(5):
    lists = list(map(int, input().split()))
    matrix.append(lists)

flag = False
for row in range(5):
    for col in range(5):
        if matrix[row][col] != 0:
            flag = True
            break
    if flag:
        break
print(abs(row - 2) + abs(col - 2))
