import random
import time


for x in range(1,10000):
	if x%3 == 0 and x%5 == 0:
		print("FIZZBUZZ")

	elif x%3 == 0:
		print("FIZZ")

	elif x%5 == 0:
		print("BUZZ")

	else:
		print(x)


#the better way. Thanks Tom Scott

for x in range(1,10000):
	output = ""

	if x%3 == 0:
		output += "FIZZ"

	if x%5 ==0:
		output += "BUZZ"

	if output == "":
		print(x)

	else:
		print(f"{output}")


