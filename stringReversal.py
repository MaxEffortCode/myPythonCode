def reverseString(string):
	string = string
	string = list(string)
	revString = ""
	y = len(string)-1
	x = 0
	while x <= y:
		temp = string[x]
		string[x] = string[y]
		string[y] = temp
		x+=1
		y-=1

	for char in string:
		revString = revString + char

	return revString


print(reverseString("this string is now reversed"))