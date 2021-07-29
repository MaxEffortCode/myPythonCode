def palinPerm(word):
	word = word.upper()
	word = word.replace(" ", "")
	letarr = [0]*26

	for letter in word:
		if letarr[(ord(letter)%26)]==1:
			letarr[ord(letter)%26]-=1
		else:
			letarr[ord(letter)%26]+=1

	if sum(letarr) == 0 or sum(letarr) ==1:
		return True

	return False



print(palinPerm("atco cta"))
print(palinPerm("abc xyz"))
print(palinPerm("racecar"))
print(palinPerm("race           car"))
print(palinPerm("race212321car"))
