from hashlib import *

done = False

def hashPassword(password):
	return sha256(password).hexdigest()

def login(members):
	userinput = input("Enter your username: ")
	passinput = input("Enter your password: ").encode('utf-8')
	
	if userinput in members.keys():
		hashedpas = hashPassword(passinput)
		if hashedpas == members.get(userinput):
			print("You're in!")
		else:
			print("Incorrect password.")
	else:
		print("Your information is not in our system. Please sign up.")
		newuserinput = input("Enter your new username: ")
		newpassinput = input("Enter your new password: ").encode('utf-8')
		members[newuserinput] = hashPassword(newpassinput)
		
members = {}

while not done:
	quit = input("Would you like to login ('yes' or 'no'): ")
	if quit == "yes":
		login(members)
	elif quit == "no":
		done = True
		print("Thank you!")
	else:
		print("Please enter 'yes' or 'no'.")