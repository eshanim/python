glass = 0
glassEmpty = True

while glassEmpty:
	
	print("The glass is still only " + str(glass) + "/50 full.")
	print("Let's fill the glass.")
	
	num = int(input("Pick a number to decide how much water to add to the glass: "))
	print("")
	glass += num
	
	if glass >= 50:
		print("The glass is " + str(glass) + "/50 full.")
		print("Yay, you're done!")
		glassEmpty = False