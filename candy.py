candy = {}

candy = {
		"snickers": 100,
		"skittles": 50,
		"twix": 20,
		"M&Ms": 200,
		"dum-dums": 1200
		}

# if the candy we want to add is NOT already a key:
	#add the candy and give it a value
#else if it IS already a key
	#increment


ncandy = input("Enter a candy: ")
num = input("How many do you want to add: ")

if ncandy not in candy.keys():
	candy[ncandy] = num
else:
	candy[ncandy] += num

print("")
print("Your candy storgae has:")
for k, v in candy.items():
	print(k, v)