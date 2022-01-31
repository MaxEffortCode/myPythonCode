str1 = "waterbottle"
str2 = "erbottlewat"

def isSubstring(str1, str2):
    i = 0
    for char in str1:
        print(f"i: {i}")
        if char == str2[0]:
            len_str = 1
            for char2 in str2:
                print(f"char2: {char2} str1_pos: {str1[(i%(len(str2)))]}")
                if char2 == str1[(i%(len(str2)))]:
                    i+=1
                    len_str+=1
                    if len_str == len(str1):
                        return True
                    continue
                else:
                    break
        i+=1
    return False


#could have made more efficient by contatinating str2 with str2 and check if str1 is a substring of str2 

if __name__ == '__main__':
    print(isSubstring(str1, str2))