colors = ["blue","red","orange","yellow"]
your_color = input("Enter your favorite color: ")
colors.insert(0, your_color)

for color in colors:
	if color == your_color:
		print(color +" is my favorite.")
	else:
		print(color + " is also a color.")