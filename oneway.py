def oneway(word, wtc):
	if len(word)-len(wtc)>1 or len(word)-len(wtc)<-1:
		return False

	word = word.lower()
	wtc = wtc.lower()
	wdarr = [0]*26

	for letter in word:
		wdarr[ord(letter)%26]+=1

	for letter in wtc:
		if wdarr[ord(letter)%26] >= 1:
			wdarr[ord(letter)%26]-=1
	
	if sum(wdarr) <= 1 or sum(wdarr) <= -1:
		return True

	return False

print(oneway("test", "tst"))
print(oneway("pales","pale"))
print(oneway("pale","bale"))
print(oneway("pale","bake"))