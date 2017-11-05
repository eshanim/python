from random import randint
real = randint(1,50)
guess = 0
done = False

while not done:
	number = int(input("Guess my favorite number (1-50): "))
	
	if(number == real):
		guess += 1
		print("You got it! Good job!")
		print("It took you " + str(guess) + " tries.")
		done = True
	elif(number < real):
		print("Try again. Your guess is too low.")
		guess += 1
	elif(number > real):
		print("Try again. Your guess is too high.")
		guess += 1
	else:
		print("Please enter a number.")