from random import randint
hangman = ["jazz",
           "boutique",
           "computer",
           "whiteboard",
           "projector",
           "notebook",
           "window",
           "carpet",
           "elephant"]

correct_letters = []
letters_left = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r",
				"s","t","u","v","w","x","y","z"]

hang_length = len(hangman)

index = randint(0, hang_length - 1)

word = hangman[index]
wrong_guesses = 0

print("HANGMAN")

while(wrong_guesses <= 6):
	print("Here are your correct guesses: ")
	for each in correct_letters:
		print(each)
	print("")
	print("You have guessed incorrectly " + str(wrong_guesses) + " times. You have 7 tries.")
	guess = input("Guess a letter (type in lowercase) to start: ")

	if guess in word and guess in letters_left:
		letters_left.remove(guess)
		correct_letters.extend([guess])
		print("Yes! That letter is in the word")
		print("")
		
	elif guess not in word and guess in letters_left:
		letters_left.remove(guess)
		print("No! Sorry that's not in the word")
		print("")
		wrong_guesses += 1
		
	elif guess not in letters_left:
		print("Guess again please. You've already guessed this.")
		print("")
		
print("The correct word was " + word + ".")
