arr = [
    [1, 2, 3, 0],
    [4, 0, 6, 9],
    [7, 8, 9, 11],
    [7, 8, 9, 11],
    [7, 8, 9, 11]
    ]

row_set = set()
col_set = set()

i = 0
for x in arr:
    j=0
    for y in x:
        if y == 0:
            row_set.add(i)
            col_set.add(j)
        j+=1
    i+=1

for x in row_set:
    for i in range(len(arr[x])):
        arr[x][i] = 0

for y in col_set:
    for j in range(len(arr)):
        arr[j][y] = 0


print(f'row set: {row_set}  col set: {col_set}  arr: {arr}')