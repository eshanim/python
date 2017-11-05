from random import randint

syl5 = ["Flying in the sky",
		"Laptop keys clicking",
		"Stars shining at night",
		"The sunshine is bright",
		"An old silent pond",
		"Long walk to water",
		"Long snakes slithering",
		"A cricket chirping",
		"Loud ducks are quacking",
		"Small cows are mooing",
		"A fat bee stings me"]

syl7 = ["Dead rats lying on the road",
        "Loud chattering of the crowd",
        "Swimming with the cute dolphins",
        "A frog sitting on a log",
        "The pattering of rain drops",
        "Fish are going for a swim",
        "Grass covered in sheets of snow",
        "Christmas lights surround the house",
        "The fire alarm is ringing",
        "The smell of freshly baked cake",]

num = int(input("How many haikus do you want to print?: "))

syl5_length = len(syl5)
syl7_length = len(syl7)

for i in range(num):
	index5 = randint(0, syl5_length - 1)
	line1 = syl5[index5]
	syl5.remove(syl5[index5])
	syl5_length = len(syl5)
	index7 = randint(0, syl7_length - 1)
	line2 = syl7[index7]
	syl7.remove(syl7[index7])
	syl7_length = len(syl7)
	index52 = randint(0, syl5_length -1)
	line3 = syl5[index52]
	syl5.remove(syl5[index52])
	syl5_length = len(syl5)

	print("")
	print(line1)
	print(line2)
	print(line3)

print("")
name = input("Enter a name for this haiku: ")
print(name.upper())
	