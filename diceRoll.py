import random

def roll():
	x = 0
	while x == 0:
		try:
			print("How many dice: ")
			numOfDice = int(input())
			print("How many faces per dice: ")
			numOfPoss = int(input())
			x = 1
		except ValueError:
			x = 0
			print("Sorry that was not an integer. \n")


	for dice in range(0,numOfDice):
		outCome = random.randrange(numOfPoss)
		print(outCome+1)

roll()