strn = input()
strcmp = ''

i = 0
count = 1
for char in strn:
    if (i+1 <= len(strn)-1) and (char == strn[i+1]):
        count += 1
    else:
        strcmp = strcmp + char + str(count)
        count = 1
    
    i+=1

if len(strn) <= len(strcmp):
    print(strn)
else:
    print(strcmp)