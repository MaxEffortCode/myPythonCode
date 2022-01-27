arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

rows, cols = (len(arr), len(arr))
arr_new = [[0 for i in range(cols)] for j in range(rows)]
#print(arr_new)

j=0
for x in arr:
    i=0
    for y in x:
        #print(arr)
        print(f'num: {y} i: {i}')
        
        arr_new[(len(arr)-1-i)][j] = y

        print(f'arr old: {arr} arr new: {arr_new}')
        #print(arr)
        i+=1
    j+=1

print(f'arr old: {arr} arr new: {arr_new}')