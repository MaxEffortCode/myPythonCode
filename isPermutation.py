def isPermutation(word, wtc):
    if len(wtc) != len(word):
        return False
    wtc = sorted(wtc)
    word = sorted(word)
    if wtc==word:
        return True
    return False

print(isPermutation("abcd", "dcba"))
print("\n")
print(isPermutation("abcd", "aabc"))

    
