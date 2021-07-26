

def isUnique(word):
    letter=[-1 for i in range(26)]
    for char in word:
        if(letter[ord(char)%26]==-1):
            letter[ord(char)%26]=1
        else:
            return False
    return True

print(isUnique("hello\n"))
print(isUnique("abcdefg"))
