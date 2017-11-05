def add(num1, num2):
	print ("The sum is " + str(num1 + num2) + ".")
	return

def sub(num1, num2):
	print ("The difference is " + str(num1 - num2) + ".")
	return

def mul(num1, num2):
	print ("The product is " + str(num1 * num2) + ".")
	return

def div(num1, num2):
	print ("The quotient is " + str(num1 / num2) + ".")
	return

def mod(num1, num2):
	print ("The remainder is " + str(num1 % num2) + ".")
	return

done = False

while not done:
	print('')
	quit = input("Do you want to continue ('yes' or 'no'): ")
	if quit == "yes":
		n1 = int(input("Enter an integer: "))
		n2 = int(input("Enter another integer: "))
		print("")
		add(n1, n2)
		sub(n1, n2)
		mul(n1, n2)
		div(n1, n2)
		mod(n1, n2)
	elif quit == "no":
		done = True
		print("You're done!")
	else:
		print("Type 'yes' or 'no'.")

